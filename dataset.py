import random
import csv


def generate_random_data(num_entries):
    data = []
    for _ in range(num_entries):
        weight = random.randint(1000, 3000)
        height = random.randint(80, 200)
        color = random.choice(['red', 'blue', 'green', 'yellow', 'black', 'white'])

        # Determine the number of wheels based on weight
        if weight <= 1000:
            no_of_wheels = 2
        elif weight > 1500:
            no_of_wheels = 4
        else:
            no_of_wheels = random.choice([2, 4])  # For weights between 1001 and 1500, random choice

        data.append([weight, height, color, no_of_wheels])
    return data


# Generate 1000 random data entries
random_data = generate_random_data(1000)

# Save the random data entries to a CSV file
with open('random_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['weight', 'height', 'color', 'no_of_wheels'])
    writer.writerows(random_data)

print("CSV file 'random_data.csv' has been created.")

