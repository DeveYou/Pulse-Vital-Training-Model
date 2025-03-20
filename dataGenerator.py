import csv
import random

# Set the number of rows you want
num_rows = 2000

# Define the CSV header
header = ["blood pressure", "heart rate", "diabetes value", "age", "output"]

with open("synthetic_health_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    
    for _ in range(num_rows):
        # Randomly choose a risk category with some weights
        risk = random.choices(["Low", "Medium", "High"], weights=[0.4, 0.35, 0.25])[0]
        
        if risk == "Low":
            bp = random.randint(100, 120)
            hr = random.randint(60, 75)
            diabetes = random.randint(80, 100)
            age = random.randint(20, 40)
        elif risk == "Medium":
            bp = random.randint(121, 140)
            hr = random.randint(76, 90)
            diabetes = random.randint(101, 130)
            age = random.randint(35, 55)
        else:  # High risk
            bp = random.randint(141, 180)
            hr = random.randint(91, 110)
            diabetes = random.randint(131, 200)
            age = random.randint(50, 80)
            
        writer.writerow([bp, hr, diabetes, age, risk])

print("CSV file 'synthetic_health_data.csv' with 2000 rows has been generated.")
