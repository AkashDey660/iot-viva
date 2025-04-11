import random
import time
from datetime import datetime
import csv

# Simulate a patient with vital signs
class PatientMonitor:
    def __init__(self, patient_id, name):  # Fixed __init__
        self.patient_id = patient_id
        self.name = name

    def read_vitals(self):
        return {
            "timestamp": datetime.now(),
            "patient_id": self.patient_id,
            "name": self.name,
            "heart_rate": random.randint(50, 130),      # bpm
            "bp_systolic": random.randint(90, 160),     # mmHg
            "bp_diastolic": random.randint(60, 100),    # mmHg
            "temperature": round(random.uniform(35.5, 40.5), 1),  # °C
            "spo2": random.randint(85, 100)             # %
        }

# Analyze data and trigger alerts
def analyze_data(vitals):
    alerts = []
    if vitals["heart_rate"] > 110 or vitals["heart_rate"] < 50:
        alerts.append("⚠ Abnormal Heart Rate")
    if vitals["bp_systolic"] > 140 or vitals["bp_diastolic"] > 90:
        alerts.append("⚠ High Blood Pressure")
    if vitals["temperature"] > 38.0:
        alerts.append("⚠ High Temperature")
    if vitals["spo2"] < 92:
        alerts.append("⚠ Low Oxygen Level")
    
    for alert in alerts:
        print(f"🚨 ALERT for {vitals['name']} ({vitals['patient_id']}): {alert}")
    
    # Actuator Simulation: Dispense medication if high BP
    if "⚠ High Blood Pressure" in alerts:
        print(f"💊 Auto-dispensing BP medication for {vitals['name']}")
    
    return alerts

# Save vitals to CSV (simulate cloud transmission)
def log_data(vitals):
    with open("patient_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            vitals["timestamp"], vitals["patient_id"], vitals["name"],
            vitals["heart_rate"], vitals["bp_systolic"], vitals["bp_diastolic"],
            vitals["temperature"], vitals["spo2"]
        ])

# Main simulation loop
def main():
    patients = [
        PatientMonitor("P001", "Amit"),
        PatientMonitor("P002", "Sneha"),
        PatientMonitor("P003", "Ramesh")
    ]

    print("🏥 Smart Healthcare Monitoring Started...\n")

    # Create log file with headers
    with open("patient_log.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Patient ID", "Name", "Heart Rate", "BP Sys", "BP Dia", "Temperature", "SpO2"])

    while True:
        for patient in patients:
            vitals = patient.read_vitals()
            print(f"📊 Vitals for {vitals['name']}: HR={vitals['heart_rate']} bpm, Temp={vitals['temperature']}°C, BP={vitals['bp_systolic']}/{vitals['bp_diastolic']}, SpO2={vitals['spo2']}%")
            analyze_data(vitals)
            log_data(vitals)
            print("-" * 50)
        time.sleep(10)

if __name__ == "__main__":
    main()
