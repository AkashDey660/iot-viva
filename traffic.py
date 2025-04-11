import random
import time
import csv
from datetime import datetime

# Simulate traffic data for each intersection
class TrafficSensor:
    def __init__(self, location):  # Fixed constructor
        self.location = location
        self.vehicle_count = 0
        self.avg_speed = 0
        self.density = 0  # Vehicles per km

    def read_data(self):
        self.vehicle_count = random.randint(10, 150)
        self.avg_speed = random.randint(20, 80)  # km/h
        self.density = round(self.vehicle_count / random.uniform(0.5, 2.0), 2)  # vehicles/km

    def get_data(self):
        return {
            "location": self.location,
            "vehicle_count": self.vehicle_count,
            "avg_speed": self.avg_speed,
            "density": self.density,
            "timestamp": datetime.now()
        }

# Actuator to control signal time
def control_signal(t_data):
    if t_data["vehicle_count"] > 100 or t_data["density"] > 80:
        signal_time = 90
    elif t_data["vehicle_count"] > 50:
        signal_time = 60
    else:
        signal_time = 30
    print(f"🚦 [{t_data['location']}] Signal GREEN for {signal_time} seconds (Traffic: {t_data['vehicle_count']}, Speed: {t_data['avg_speed']} km/h)")
    return signal_time

# Logging
def log_data(data):
    with open("traffic_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data["timestamp"], data["location"],
            data["vehicle_count"], data["avg_speed"], data["density"]
        ])

# Main system
def main():
    sensors = [
        TrafficSensor("Jaydev Vihar"),
        TrafficSensor("Rupali Square"),
        TrafficSensor("CRP Square"),
    ]

    print("🚗 Smart Traffic Monitoring Started...\n")

    # Create log file
    with open("traffic_log.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Location", "Vehicle Count", "Avg Speed", "Density"])

    while True:
        for sensor in sensors:
            sensor.read_data()
            data = sensor.get_data()
            control_signal(data)
            log_data(data)
            print("-" * 50)
        time.sleep(10)

if __name__ == "__main__":
    main()
