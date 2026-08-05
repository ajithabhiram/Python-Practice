import random
from datetime import datetime

def welcome():
    print("Welcome to MovieMate AI!")
    print()

def choose_genre():

    print("Choose Genre:")
    print("1. Action")
    print("2. Comedy")
    print("3. Horror")
    print("4. Romance")

    choice = input("Enter your choice: ")

    if choice == "1":
        return "Action"

    elif choice == "2":
        return "Comedy"

    elif choice == "3":
        return "Horror"

    elif choice == "4":
        return "Romance"

    else:
        print("Invalid Choice!")
        return None


def show_movies(genre):

    if genre == "Action":
        movies = ["Leo", "Vikram", "Jailer", "SpiderMan"]

    elif genre == "Comedy":
        movies = ["Jathi Ratnalu", "MAD", "F2", "Venky"]

    elif genre == "Horror":
        movies = ["Masooda", "Virupaksha", "Arundhati", "Mohini"]

    else:
        movies = ["Hi Nanna", "Sita Ramam", "Arjun Reddy", "Love Today"]

    print("\nAvailable Movies:")

    for i in range(len(movies)):
        print(i + 1, ".", movies[i], sep="")

    return movies


def book_ticket(name, movie):

    timings = ["10:00 AM", "1:30 PM", "4:30 PM", "7:30 PM", "10:00 PM"]

    show_time = random.choice(timings)

    booking_date = datetime.now().strftime("%d-%b-%Y")

    print("\nBooking Confirmed!\n")

    print("Customer     :", name)
    print("Movie        :", movie)
    print("Show Time    :", show_time)
    print("Booking Date :", booking_date)

    print("\nEnjoy your movie!")


welcome()

name = input("Enter your name: ")

genre = choose_genre()

if genre != None:

    movies = show_movies(genre)

    movie = input("\nEnter movie: ")

    if movie in movies:

        book_ticket(name, movie)

    else:

        print("Movie not available.")
