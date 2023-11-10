import Adafruit_DHT as DHT
import time
from datetime import datetime

def read_sensor():
    print("Sensor reading started.")
    while True:
        humidity, temperature = DHT.read_retry(DHT.DHT11, 4)
        if humidity is not None and temperature is not None:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            data_line = f"{current_time},{temperature},{humidity}\n"
            print(f"Data: {data_line.strip()}")
            try:
                with open("dataLab.txt", "a") as file:
                    file.write(data_line)
            except IOError as e:
                print(f"Error writing to file: {e}")
        else:
            print("Sensor read failed or returned None.")
        time.sleep(1)

read_sensor()
