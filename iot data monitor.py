import random
import time
import matplotlib.pyplot as plt
from datetime import datetime

# Simulate reading from a temperature sensor
def read_sensor_data():
    temperature = random.uniform(20.0, 30.0)  # Simulate temp in Celsius
    humidity = random.uniform(30.0, 70.0)     # Simulate humidity
    return temperature, humidity

# Store data
timestamps = []
temperatures = []
humidities = []

plt.ion()  # Turn on interactive plotting
fig, (temp_ax, hum_ax) = plt.subplots(2, 1)

while True:
    temp, hum = read_sensor_data()
    now = datetime.now().strftime("%H:%M:%S")

    timestamps.append(now)
    temperatures.append(temp)
    humidities.append(hum)

    # Limit to last 20 data points
    timestamps = timestamps[-20:]
    temperatures = temperatures[-20:]
    humidities = humidities[-20:]

    # Plot temperature
    temp_ax.clear()
    temp_ax.plot(timestamps, temperatures, label="Temperature (°C)", color="red")
    temp_ax.legend()
    temp_ax.set_xticklabels(timestamps, rotation=45, ha='right')

    # Plot humidity
    hum_ax.clear()
    hum_ax.plot(timestamps, humidities, label="Humidity (%)", color="blue")
    hum_ax.legend()
    hum_ax.set_xticklabels(timestamps, rotation=45, ha='right')

    plt.tight_layout()
    plt.pause(1)
