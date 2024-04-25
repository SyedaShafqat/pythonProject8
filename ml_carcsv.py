import csv

def identify_vehicle_type(no_of_wheels):
    if no_of_wheels == 2:
        return "bike"
    elif no_of_wheels == 4:
        return "car"
    else:
        return "Unknown"

# Read data from the current CSV file
data = []
with open('random_data.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        row['vehicle_type'] = identify_vehicle_type(int(row['no_of_wheels']))
        data.append(row)

# Write data to a new CSV file
with open('updated_data.csv', 'w', newline='') as outfile:
    fieldnames = ['weight', 'height', 'color', 'no_of_wheels', 'vehicle_type']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("CSV file 'updated_data.csv' has been created.")
