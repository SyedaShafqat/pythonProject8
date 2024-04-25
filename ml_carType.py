def identify_vehicle(color, height, weight, no_of_wheels):
    weight_grams = weight * 1000  # Convert weight to grams
    if no_of_wheels == 2 and weight <= 1000:
        return "bike"
    elif no_of_wheels == 4 and weight >= 1500:
        return "car"
    else:
        return "Unknown"

def main():
    while True:
        color = input("Enter color: ")
        height = int(input("Enter height (in cm): "))
        weight_kg = float(input("Enter weight (in kg): "))  # Take weight in kg
        no_of_wheels = int(input("Enter number of wheels: "))

        # Identify the vehicle
        vehicle_type = identify_vehicle(color, height, weight_kg, no_of_wheels)

        # Show the output
        if vehicle_type == "bike" or vehicle_type == "car":
            print("The identified vehicle type is:", vehicle_type)
        else:
            print("Unknown")

        choice = input("Do you want to enter another vehicle? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
