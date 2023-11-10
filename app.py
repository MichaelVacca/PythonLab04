import Adafruit_DHT as DHT
import threading
import time
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

sensor_data = {
    'temperature': [],
    'humidity': []
}

def read_sensor_data():
    with open("dataLab.txt", "r") as file:
        csv_reader = csv.reader(file)
        labels = []
        temperature_data = []
        humidity_data = []
        for row in csv_reader:
            labels.append(row[0])  # Date and time
            temperature_data.append(row[1])  # Temperature
            humidity_data.append(row[2])  # Humidity
        return labels, temperature_data, humidity_data

@app.route('/data', methods=['GET'])
def data():
    try:
        with open('dataLab.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                _, temperature, humidity = last_line.strip().split(',')
                temperature = float(temperature)
                humidity = float(humidity)
            else:
                temperature = 0
                humidity = 0
    except IOError:
        temperature = 0
        humidity = 0
        print("Error reading from file.")

    return jsonify({
        'temperature': temperature,
        'humidity': humidity
    })

@app.route('/environment', methods=['GET'])
def environment_data():
    timestamps = []
    temp_data = []
    humid_data = []

    try:
        with open('dataLab.txt', 'r') as file:
            for line in file:
                timestamp, temperature, humidity = line.strip().split(',')
                timestamps.append(timestamp)
                temp_data.append(float(temperature))
                humid_data.append(float(humidity))
    except IOError:
        print("Error reading from file.")

    return render_template(
        'environment_graphs.html',
        timestamps=timestamps,
        temp_data=temp_data,
        humid_data=humid_data
    )


@app.route('/index', methods=['GET'])
def Index():
    return render_template('index.html')



@app.route('/Sales', methods=['GET'])
def chart_page():  
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

