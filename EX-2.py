# 2. Even or Odd Number Checker
number = int(input("Enter a number: "))
if number == 0:
    print("Zero is neither even nor odd")
else:
    if number > 0:
        if number % 2 == 0:
            print("Positive Even Number")
        else:
            print("Positive Odd Number")
    else:
        if number % 2 == 0:
            print("Negative Even Number")
        else:
            print("Negative Odd Number")
