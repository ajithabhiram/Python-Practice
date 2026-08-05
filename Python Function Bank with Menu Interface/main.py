from my_programs import (
    swap_two_numbers,
    gcd_two_numbers,
    fibonacci_series,
    reverse_number,
    sum_of_digits,
    count_vowels,
    reverse_string,
    title_case,
    palindrome,
    prime_number,
    factorial,
    decimal_to_binary,
    largest_of_three,
    max_min_list
)

while True:

    print("\n------ FUNCTION MENU ------")
    print("1. Swap Two Numbers")
    print("2. GCD of Two Numbers")
    print("3. Fibonacci Series")
    print("4. Reverse a Number")
    print("5. Sum of Digits")
    print("6. Count Vowels in a String")
    print("7. Reverse a String")
    print("8. Convert String to Title Case")
    print("9. Check for Palindrome")
    print("10. Check for Prime Number")
    print("11. Find Factorial of a Number")
    print("12. Convert Decimal to Binary")
    print("13. Find the Largest of Three Numbers")
    print("14. Find Maximum and Minimum in a List")
    print("0. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        swap_two_numbers()

    elif choice == 2:
        gcd_two_numbers()

    elif choice == 3:
        fibonacci_series()

    elif choice == 4:
        reverse_number()

    elif choice == 5:
        sum_of_digits()

    elif choice == 6:
        count_vowels()

    elif choice == 7:
        reverse_string()

    elif choice == 8:
        title_case()

    elif choice == 9:
        palindrome()

    elif choice == 10:
        prime_number()

    elif choice == 11:
        factorial()

    elif choice == 12:
        decimal_to_binary()

    elif choice == 13:
        largest_of_three()

    elif choice == 14:
        max_min_list()

    elif choice == 0:
        print("Exiting the Program...")
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please enter a number between 0 and 14.")
