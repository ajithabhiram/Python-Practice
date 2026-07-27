name = input("Enter Account Holder Name: ")

pin = 1234
balance = 5000
transaction = []

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

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Your Balance is:", balance)

            elif choice == 2:
                money = float(input("Enter amount to add: "))
                balance = balance + money
                transaction.append("Money Added : " + str(money))
                print("Money Added Successfully")

            elif choice == 3:
                dep = float(input("Enter deposit amount: "))
                balance = balance + dep
                transaction.append("Deposited : " + str(dep))
                print("Deposit Successful")

            elif choice == 4:
                wd = float(input("Enter withdraw amount: "))

                if wd <= balance:
                    balance = balance - wd
                    transaction.append("Withdrawn : " + str(wd))
                    print("Please collect your cash")
                else:
                    print("Insufficient Balance")

            elif choice == 5:

                if len(transaction) == 0:
                    print("No Transactions")

                else:
                    print("Transaction History")
                    for i in transaction:
                        print(i)

            elif choice == 6:
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
