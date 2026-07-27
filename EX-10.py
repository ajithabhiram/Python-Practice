BMI_results = {
    "name": [],
    "BMI_values": []
}

# Number of users validation
while True:
    try:
        count = int(input("Enter number of users: "))
        if count > 0:
            break
        else:
            print("Number of users must be greater than 0.")
    except ValueError:
        print("Please enter a valid integer.")

for i in range(count):
    print(f"\nUser {i+1}")

    # Name validation
    while True:
        person = input("Enter name: ").strip()
        if person:
            break
        else:
            print("Name cannot be empty.")

    # Weight validation
    while True:
        try:
            kg = float(input("Enter weight (kg): "))
            if kg > 0:
                break
            else:
                print("Weight must be greater than 0.")
        except ValueError:
            print("Please enter a valid weight.")

    # Height unit validation
    while True:
        unit = input("Enter height unit (cm/feet/inches): ").lower().strip()

        if unit == "cm":
            while True:
                try:
                    value = float(input("Enter height in cm: "))
                    if value > 0:
                        metres = value / 100
                        break
                    else:
                        print("Height must be greater than 0.")
                except ValueError:
                    print("Please enter a valid height.")
            break

        elif unit == "feet":
            while True:
                try:
                    value = float(input("Enter height in feet: "))
                    if value > 0:
                        metres = value * 0.3048
                        break
                    else:
                        print("Height must be greater than 0.")
                except ValueError:
                    print("Please enter a valid height.")
            break

        elif unit == "inches":
            while True:
                try:
                    value = float(input("Enter height in inches: "))
                    if value > 0:
                        metres = value * 0.0254
                        break
                    else:
                        print("Height must be greater than 0.")
                except ValueError:
                    print("Please enter a valid height.")
            break

        else:
            print("Invalid height unit! Please enter cm, feet, or inches.")

    # BMI Calculation
    bmi_value = round(kg / (metres ** 2), 2)

    BMI_results["name"].append(person)
    BMI_results["BMI_values"].append(bmi_value)

    # BMI Category
    if bmi_value < 18.5:
        print(person, "is Underweight")
    elif bmi_value < 25:
        print(person, "has Normal Weight")
    elif bmi_value < 30:
        print(person, "is Overweight")
    else:
        print(person, "is Obese")

# Display stored results
print("\nStored BMI Details")
print(BMI_results)