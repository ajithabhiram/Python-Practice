import random
import smtplib
from email.mime.text import MIMEText

#ROCK PAPER SCISSORS

def rock_paper_scissors():
    print("\n Rock Paper Scissors ")
    choices = ["rock", "paper", "scissors"]
    player = input("Enter Rock, Paper or Scissors: ").lower()
    if player not in choices:
        print("Invalid Choice")
        return
    computer = random.choice(choices)
    print("Computer Choice:", computer)

    if player == computer:
        print("It's a Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You Win!")

    else:
        print("Computer Wins!")

#  STORY GENERATOR

def story_generator():
    print("\nStory Generator")

    when = [
        "Yesterday",
        "Last Sunday",
        "One Morning",
        "Last Night"
    ]

    who = [
        "Rahul",
        "A Teacher",
        "A Little Boy",
        "My Friend"
    ]

    where = [
        "at School",
        "in Hyderabad",
        "near the Beach",
        "inside a Forest"
    ]

    what = [
        "found a treasure",
        "met an alien",
        "won a competition",
        "saved a puppy"
    ]

    how = [
        "with great courage.",
        "using smart ideas.",
        "with the help of friends.",
        "by accident."
    ]
    print("\nGenerated Story:\n")
    print(
        random.choice(when),
        random.choice(who),
        random.choice(where),
        random.choice(what),
        random.choice(how)
    )


#OTP EMAIL

def otp_generator():
    print("\n OTP Generator")

    sender = input("Enter Sender Gmail: ")
    receiver = input("Enter Receiver Gmail: ")
    app_password = input("Enter Gmail App Password: ")

    otp = random.randint(100000, 999999)

    subject = "OTP Verification"

    body = f"Your OTP is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender, app_password)

        server.sendmail(sender, receiver, msg.as_string())

        server.quit()

        print("OTP Sent Successfully!")
        print("Generated OTP:", otp)

    except Exception as e:
        print("Error:", e)


#BMI CALCULATOR

def bmi_calculator():

    print("\n BMI Calculator")

    name = input("Enter Name: ")

    weight = float(input("Enter Weight (kg): "))

    height = float(input("Enter Height (m): "))

    if weight <= 0 or height <= 0:
        print("Invalid Input")
        return

    bmi = weight / (height ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print(name, "- Underweight")

    elif bmi < 25:
        print(name, "- Normal Weight")

    elif bmi < 30:
        print(name, "- Overweight")

    else:
        print(name, "- Obesity")


#MAIN MENU

while True:

    print("\n")
    print("      GAME GENERATOR MENU")
    print("")
    print("1. Rock Paper Scissors")
    print("2. Story Generator")
    print("3. OTP Generate to Email")
    print("4. BMI Calculator")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        rock_paper_scissors()

    elif choice == "2":
        story_generator()

    elif choice == "3":
        otp_generator()

    elif choice == "4":
        bmi_calculator()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice. Try Again.")
