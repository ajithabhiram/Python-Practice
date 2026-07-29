# Build a Simple Choice Chooser

BMI_results = {
    "name": [],
    "BMI_values": []
}
pin = 1234
balance = 5000
transaction = []

# Factorial using recursion
def factorial(n):
    if n < 0:
        return "Enter a positive number"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Sum of numbers using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

# Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

while True:

    print("\n------ Choice Chooser ------")
    print("1 Factorial")
    print("2 Sum of Numbers")
    print("3. BMI Calculator")
    print("4 Fibonacci Series")
    print("5 ATM Usecase")
    print("6 Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        n = int(input("Enter a number: "))
        print("Factorial is:", factorial(n))

    elif choice == 2:

        n = int(input("Enter a number: "))
        print("Sum is:", sum_numbers(n))

    elif choice == 3:

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

            print("\nUser", i + 1)

            while True:
                person = input("Enter name: ").strip()
                if person:
                    break
                else:
                    print("Name cannot be empty.")

            while True:
                try:
                    kg = float(input("Enter weight (kg): "))
                    if kg > 0:
                        break
                    else:
                        print("Weight must be greater than 0.")
                except ValueError:
                    print("Please enter a valid weight.")

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
                    print("Invalid height unit!")

            bmi_value = round(kg / (metres ** 2), 2)

            BMI_results["name"].append(person)
            BMI_results["BMI_values"].append(bmi_value)

            if bmi_value < 18.5:
                print(person, "is Underweight")
            elif bmi_value < 25:
                print(person, "has Normal Weight")
            elif bmi_value < 30:
                print(person, "is Overweight")
            else:
                print(person, "is Obese")

        print("\nStored BMI Details")
        print(BMI_results)

    elif choice == 4:

        n = int(input("Enter number of terms: "))

        print("Fibonacci Series")
        for i in range(n):
            print(fibonacci(i), end=" ")
        print()

    elif choice == 5:

        name = input("Enter Account Holder Name: ")

        count = 0

        while count < 3:

            user_pin = int(input("Enter PIN: "))

            if user_pin == pin:

                print("Login Successful")

                while True:

                    print("\n------ ATM MENU ------")
                    print("1. Check Balance")
                    print("2. Add Money")
                    print("3. Deposit")
                    print("4. Withdraw")
                    print("5. Transactions")
                    print("6. Exit")

                    option = int(input("Enter your choice: "))

                    if option == 1:
                        print("Your Balance is:", balance)

                    elif option == 2:
                        money = float(input("Enter amount to add: "))
                        balance = balance + money
                        transaction.append("Money Added : " + str(money))
                        print("Money Added Successfully")

                    elif option == 3:
                        dep = float(input("Enter deposit amount: "))
                        balance = balance + dep
                        transaction.append("Deposited : " + str(dep))
                        print("Deposit Successful")

                    elif option == 4:
                        wd = float(input("Enter withdraw amount: "))

                        if wd <= balance:
                            balance = balance - wd
                            transaction.append("Withdrawn : " + str(wd))
                            print("Please collect your cash")
                        else:
                            print("Insufficient Balance")

                    elif option == 5:

                        if len(transaction) == 0:
                            print("No Transactions")
                        else:
                            print("Transaction History")
                            for i in transaction:
                                print(i)

                    elif option == 6:
                        print("Thank You")
                        break

                    else:
                        print("Invalid Choice")

                break

            else:
                count = count + 1
                print("Wrong PIN")
                print("Remaining Attempts:", 3 - count)

        if count == 3:
            print("Card Blocked")

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
