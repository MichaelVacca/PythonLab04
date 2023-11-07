from flask import Flask, render_template, jsonify
import Adafruit_DHT as DHT
import threading
import time

app = Flask(__name__)

sensor_data = {
    'temperature': [],
    'humidity': []
}

def read_sensor():
    while True:
        humidity, temperature = DHT.read_retry(DHT.DHT11, 4)
        if humidity is not None and temperature is not None:
            sensor_data['temperature'].append(temperature)
            sensor_data['humidity'].append(humidity)
            sensor_data['temperature'] = sensor_data['temperature'][-50:]
            sensor_data['humidity'] = sensor_data['humidity'][-50:]
        time.sleep(1)

sensor_thread = threading.Thread(target=read_sensor)
sensor_thread.daemon = True
sensor_thread.start()

sensor_thread = threading.Thread(target=read_sensor)
sensor_thread.daemon = True
sensor_thread.start()

@app.route('/data', methods=['GET'])
def data():
    return jsonify({
        'temperature': sensor_data['temperature'][-1] if sensor_data['temperature'] else 0,
        'humidity': sensor_data['humidity'][-1] if sensor_data['humidity'] else 0
    })

@app.route('/environment', methods=['GET'])
def environment_data():
    return render_template(
        'environment_graphs.html',
        temp_data=sensor_data['temperature'],
        humid_data=sensor_data['humidity']
    )

@app.route('/index', methods=['GET'])
def Index():
    return render_template('index.html')



@app.route('/Sales', methods=['GET'])
def chart_page():  # put application's code here
    # Define Plot Data
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
    ]
    header = "This is my first line graph"
    description = "THis is a desc"
    data = [0, 10, 15, 8, 22, 18, 25]
    return render_template('line_graph_example.html',data=data , labels=labels , header=header, description=description)


if __name__ == '__main__':
    app.run()
