BMI_results = {
    "name": [],
    "BMI_values": []
}

def bmi_calc(**kwargs):

    bmi = kwargs["weight"] / (kwargs["height"] ** 2)
    bmi = round(bmi, 2)

    BMI_results["name"].append(kwargs["name"])
    BMI_results["BMI_values"].append(bmi)

    if bmi < 18.5:
        print(f'{kwargs["name"]} --> You are Underweight as BMI is {bmi}')
    elif bmi < 25:
        print(f'{kwargs["name"]} --> You are in Perfect shape, BMI is {bmi}')
    elif bmi < 30:
        print(f'{kwargs["name"]} --> You are Overweight, need to maintain diet, BMI is {bmi}')
    else:
        print(f'{kwargs["name"]} --> Obesity, Your BMI is {bmi}')

while True:
    try:
        count = int(input("Enter the number of users: "))
        if count > 0:
            break
        else:
            print("Enter a positive number.")
    except ValueError:
        print("Invalid input.")

for i in range(count):

    while True:
        try:
            name = input("Enter the Name: ").strip()
            weight = float(input("Enter the weight in kgs: "))

            unit = input("Enter height unit (cm/feet/inches): ").lower()

            if unit == "cm":
                height = float(input("Enter the height in cm: "))
                height = height / 100

            elif unit == "feet":
                height = float(input("Enter the height in feet: "))
                height = height * 0.3048

            elif unit == "inches":
                height = float(input("Enter the height in inches: "))
                height = height * 0.0254

            else:
                print("Invalid unit.")
                continue

            if weight > 0 and height > 0:
                break
            else:
                print("Weight and height must be positive.")

        except ValueError:
            print("Invalid input.")

    bmi_calc(
        name=name,
        weight=weight,
        height=height
    )

print("\nStored BMI Details")
print(BMI_results)
