# realtime_logger.py
# Reads DHT11 data from Arduino and creates a real-time plot
# Run using: python realtime_logger.py --port COM3  (or /dev/ttyUSB0)

import serial
import argparse
import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

START_TIME = None

def parse_line(raw):
    parts = raw.strip().split(",")
    if len(parts) != 3:
        return None
    
    ms = int(parts[0])
    temp = float(parts[1])
    hum = float(parts[2])

    timestamp = START_TIME + timedelta(milliseconds=ms)
    return timestamp, temp, hum


def main(port, baud=9600):
    global START_TIME
    START_TIME = datetime.now()

    ser = serial.Serial(port, baud, timeout=1)
    print(f"Connected to {port}")

    csv_file = open("sensor_log.csv", "a", newline="")
    writer = csv.writer(csv_file)

    if csv_file.tell() == 0:
        writer.writerow(["timestamp", "millis", "temperature_C", "humidity_percent"])

    times = deque(maxlen=100)
    temps = deque(maxlen=100)
    hums = deque(maxlen=100)

    plt.style.use("default")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax1.set_ylabel("Temperature (°C)")
    ax2.set_ylabel("Humidity (%)")
    ax2.set_xlabel("Time")

    line1, = ax1.plot([], [], linewidth=2)
    line2, = ax2.plot([], [], linewidth=2)

    def update(frame):
        raw = ser.readline().decode("utf-8", errors="ignore").strip()
        if not raw or raw.startswith("START") or "ERROR" in raw:
            return line1, line2

        parsed = parse_line(raw)
        if not parsed:
            return line1, line2

        ts, temp, hum = parsed

        writer.writerow([ts.isoformat(), raw.split(",")[0], temp, hum])
        csv_file.flush()

        times.append(ts)
        temps.append(temp)
        hums.append(hum)

        line1.set_data(times, temps)
        line2.set_data(times, hums)

        ax1.relim()
        ax1.autoscale_view()
        ax2.relim()
        ax2.autoscale_view()

        print(f"{ts}  Temp={temp}°C  Hum={hum}%")
        return line1, line2

    ani = FuncAnimation(fig, update, interval=1000)
    plt.tight_layout()
    plt.show()

    csv_file.close()
    ser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True, help="Serial port (e.g., COM3 or /dev/ttyUSB0)")
    parser.add_argument("--baud", default=9600, type=int)
    args = parser.parse_args()

    main(args.port, args.baud)
