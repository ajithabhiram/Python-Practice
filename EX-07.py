# Scenario:
# Every student in the college has a Smart ATM Card provided by the college bank.
# Students use this card to withdraw money for their daily expenses.
# To withdraw money, they must enter the correct PIN.
# They get only 3 chances to enter the PIN.
# If all 3 attempts are wrong, the account is locked for 24 hours.
# If the PIN is correct, the student can withdraw money and the remaining balance is displayed.
pin = "111"
balance = 5000
count = 3
print("Welcome to College ATM")
while count > 0:
    print("Chances Left :", count)
    enter_pin = input("Enter Your PIN : ")
    if enter_pin == pin:
        print("PIN Matched")
        print("Your Balance is :", balance)
        withdraw = int(input("Enter Amount to Withdraw : "))
        if withdraw <= balance:
            balance = balance - withdraw
            print("Please Collect Your Cash")
            print("Remaining Balance :", balance)
        else:
            print("Insufficient Balance")
        break
    else:
        count = count - 1
        if count > 0:
            print("Wrong PIN")
            print("Please Try Again")
else:
    print("Your Account is Locked for 24 Hours")
