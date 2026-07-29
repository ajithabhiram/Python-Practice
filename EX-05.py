# 5. ATM Withdrawal System
card = input("Is the card valid? (yes/no): ")
correct_pin = 1234
balance = 5000
if card == "yes":
    pin = int(input("Enter your PIN: "))
    
    if pin == correct_pin:
        amount = int(input("Enter withdrawal amount: "))
        
        if amount <= balance:
            print("Withdrawal Successful")
            print("Remaining Balance:", balance - amount)
        else:
            print("Insufficient Balance")
    else:
        print("Incorrect PIN")
else:
    print("Invalid Card")
