import serial
import time
import csv
from datetime import datetime

# Configure the serial connection (adjust COM port and baud rate as needed)
ser = serial.Serial('COM5', 9600, timeout=1)  # Replace 'COM3' with your port

# Open a CSV file for writing
with open('hc_sr04_data.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    while True:
        try:
            # Read data from serial port
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    # Get current timestamp
                    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                    # Print data and timestamp to the command line
                    print(f"Timestamp: {timestamp}, Data: {line}")
                 
                    # Write timestamp and data to CSV
                    csv_writer.writerow([timestamp, line])
                    csvfile.flush()
                
        except KeyboardInterrupt:
            # Exit loop on Ctrl+C
            print("Data collection stopped.")
            break

# Close serial connection
ser.close()

