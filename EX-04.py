# 4. Weekend Budget Planner
budget = int(input("Enter your weekend budget: "))
if budget >= 0:
    if budget > 10000:
        print("Plan: Trip")
    elif budget > 5000:
        print("Plan: Resort Stay")
    elif budget > 3000:
        print("Plan: Movie and Dinner")
    elif budget > 1000:
        print("Plan: Cafe and Shopping")
    elif budget > 500:
        print("Plan: Street Food and Park Visit")
    else:
        print("Plan: Stay Home")
else:
    print("Please don't enter negative values")
