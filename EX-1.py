# 1. Student Grade Checker
marks = int(input("Enter marks: "))
if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("Grade: A")
        print("Remark: Outstanding!")
    elif marks >= 80:
        print("Grade: B")
        print("Remark: Excellent!")
    elif marks >= 70:
        print("Grade: C")
        print("Remark: Good")
    elif marks >= 60:
        print("Grade: D")
        print("Remark: Fair, Needs Improvement")
    elif marks >= 50:
        print("Grade: E")
        print("Remark: Poor, Needs Serious Improvement")
    else:
        print("Grade: F")
        print("Remark: Failed, Needs to Reappear")
else:
    print("Invalid marks entered")
