# Python Project Description
I generated two files, and each employs a different method to identify cars and bikes.

## User Input Vehicle Identification File

**Description:**
This Python project takes input from the user regarding the color, weight, height, and number of wheels of a vehicle. It then identifies whether the vehicle is a car or a bike based on the provided weight and number of wheels.

**Key Features:**
- Utilizes user input to gather vehicle information.
- Determines the vehicle type (car or bike) based on weight and number of wheels.

**code**
```
 if no_of_wheels == 2 and weight <= 1000:
        return "bike"
    elif no_of_wheels == 4 and weight >= 1500:
        return "car"
    else:
        return "Unknown"
```

  ## Output Screenshot
![Screenshot](https://github.com/SyedaShafqat/pythonProject8/blob/master/car_type.png)

## Random Data Generation and Vehicle Identification File

**Description:**
In this Python project, random data for car color, weight, height, and number of wheels is generated. The program then creates a query to read from a CSV file containing this random data. It adds a "vehicle" column to the CSV file and identifies each entry as either a car or a bike based on the number of wheels.

**Key Features:**
- Generates random data for car color, weight, height, and number of wheels.
- Creates a query to read data from a CSV file and identifies vehicles based on the number of wheels.

**code**

```
def identify_vehicle_type(no_of_wheels):
    if no_of_wheels == 2:
        return "bike"
    elif no_of_wheels == 4:
        return "car"
    else:
        return "Unknown"
```

  ## Output Screenshot of Random Data Generated
![Screenshot](https://github.com/SyedaShafqat/pythonProject8/blob/master/dataset.png)

  ## Output Screenshot: Data Identifies Vehicles Based on the Number of Wheels
![Screenshot](https://github.com/SyedaShafqat/pythonProject8/blob/master/updateddataset.png)
