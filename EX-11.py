while True:
    try:
        name = input("Enter the name: ")
        weight = int(input("Enter the weight in kgs.. "))
        height = float(input("Enter the height in metres.. "))

        if weight > 0 and height >= 0:

            bmi = weight / (height ** 2)
            break

        else:
            print("Make sure to enter only +ve values, no Negative values")

    except ValueError:
        print("Invalid input. Only integer for weight and float for height, enter properly")

    except ZeroDivisionError:
        print("Height cannot be zero")

if bmi < 18.5:
    print(f"{name} --> You are underweight as BMI is {bmi}")
elif 18.5 <= bmi < 24.9:
    print(f"{name} --> You are in Perfect shape, BMI is {bmi}")
elif 25 <= bmi < 29.9:
    print(f"{name} --> You are overweight, need to maintain diet, BMI is {bmi}")
elif bmi >= 30:
    print(f"{name} --> Obesity, Your BMI is {bmi}")
