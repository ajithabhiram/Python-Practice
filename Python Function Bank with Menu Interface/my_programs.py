"""
Python Function Bank with Menu Interface
This file contains 14 Python program functions.
Each function displays:
1. Program Code
2. Sample Test Cases
3. Explanation
4. User Input
"""
# Program 1 : Swap Two Numbers

def swap_two_numbers():
    """
Program : Swap Two Numbers

Code:

def swap(a, b):
    a, b = b, a
    return a, b

Test Case 1
Input : swap(10, 20)
Expected Output : (20, 10)

Test Case 2
Input : swap(5, -1)
Expected Output : (-1, 5)

Logic:
This program swaps two numbers using tuple unpacking.
It swaps the values without using a temporary variable.
"""
    print(swap_two_numbers.__doc__.strip())
    print("\nUser Execution")
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    a, b = b, a
    print("After Swapping :", a, b)

# Program 2 : GCD of Two Numbers

def gcd_two_numbers():
    """
Program : GCD of Two Numbers

Code:
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

Test Case 1
Input : gcd(12, 18)
Expected Output : 6

Test Case 2
Input : gcd(20, 8)
Expected Output : 4

Logic:
This program finds the Greatest Common Divisor of two numbers.
It uses the Euclidean Algorithm by repeatedly finding the remainder.
"""

    print(gcd_two_numbers.__doc__.strip())

    print("\nUser Execution")
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    x = a
    y = b

    while y != 0:
        x, y = y, x % y

    print("GCD =", x)

# Program 3 : Fibonacci Series

def fibonacci_series():

    print("Program : Fibonacci Series")
    print()

    print("Code:")
    print("""
def fibonacci_series(n):

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
""")

    print("Test Case 1")
    print("Input : 5")
    print("Expected Output : 0 1 1 2 3")
    print()

    print("Test Case 2")
    print("Input : 8")
    print("Expected Output : 0 1 1 2 3 5 8 13")
    print()

    print("Logic:")
    print("This program generates the Fibonacci series.")
    print("Each number is the sum of the previous two numbers.")

    print("\nUser Execution")

    n = int(input("Enter the Number of Terms : "))

    a = 0
    b = 1

    print("Fibonacci Series :")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()

# Program 4 : Reverse a Number

def reverse_number():
    """
Program : Reverse a Number

Code:

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

Test Case 1
Input : reverse_number(1234)
Expected Output : 4321

Test Case 2
Input : reverse_number(9876)
Expected Output : 6789

Logic:
This program reverses a number by taking one digit at a time.
Each digit is added to the reversed number until the original number becomes 0.
"""

    print(reverse_number.__doc__.strip())

    print("\nUser Execution")
    num = int(input("Enter a Number : "))

    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    print("Reversed Number :", reverse)


# Program 5 : Sum of Digits

def sum_of_digits():

    print("Program : Sum of Digits")
    print()

    print("Code:")
    print("""
def sum_of_digits(num):

    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total
""")

    print("Test Case 1")
    print("Input : sum_of_digits(1234)")
    print("Expected Output : 10")
    print()

    print("Test Case 2")
    print("Input : sum_of_digits(567)")
    print("Expected Output : 18")
    print()

    print("Logic:")
    print("This program finds the sum of all digits in a number.")
    print("It extracts each digit and adds it to the total.")

    print("\nUser Execution")

    num = int(input("Enter a Number : "))

    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    print("Sum of Digits :", total)


# Program 6 : Count Vowels in a String

def count_vowels():

    print("Program : Count Vowels in a String")
    print()

    print("Code:")
    print("""
def count_vowels(text):

    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1

    return count
""")

    print("Test Case 1")
    print("Input : count_vowels('Python')")
    print("Expected Output : 1")
    print()

    print("Test Case 2")
    print("Input : count_vowels('Education')")
    print("Expected Output : 5")
    print()

    print("Logic:")
    print("This program counts the number of vowels in a string.")
    print("It checks each character one by one.")

    print("\nUser Execution")

    text = input("Enter a String : ")

    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1

    print("Number of Vowels :", count)

# Program 7 : Reverse a String

def reverse_string():

    print("Program : Reverse a String")
    print()

    print("Code:")
    print("""
def reverse_string(text):

    reverse = ""

    for ch in text:
        reverse = ch + reverse

    return reverse
""")

    print("Test Case 1")
    print("Input : Python")
    print("Expected Output : nohtyP")
    print()

    print("Test Case 2")
    print("Input : Codegnan")
    print("Expected Output : nangedoC")
    print()

    print("Logic:")
    print("This program reverses a string using a loop.")
    print("Each character is added to the beginning of the new string.")

    print("\nUser Execution")

    text = input("Enter a String : ")

    reverse = ""

    for ch in text:
        reverse = ch + reverse

    print("Reversed String :", reverse)

# Program 8 : Convert String to Title Case

def title_case():

    print("Program : Convert String to Title Case")
    print()

    print("Code:")
    print("""
def title_case(text):

    words = text.split()

    result = ""

    for word in words:
        result = result + word.capitalize() + " "

    return result.strip()
""")

    print("Test Case 1")
    print("Input : title_case('python programming')")
    print("Expected Output : Python Programming")
    print()

    print("Test Case 2")
    print("Input : title_case('hello world')")
    print("Expected Output : Hello World")
    print()

    print("Logic:")
    print("This program converts the first letter of every word to uppercase.")

    print("\nUser Execution")

    text = input("Enter a Sentence : ")

    words = text.split()

    result = ""

    for word in words:
        result = result + word.capitalize() + " "

    print("Title Case :", result.strip())


# Program 9 : Check for Palindrome

def palindrome():

    print("Program : Check for Palindrome")
    print()

    print("Code:")
    print("""
def palindrome(text):

    reverse = ""

    for i in text:
        reverse = i + reverse

    if text == reverse:
        return True
    else:
        return False
""")

    print("Test Case 1")
    print("Input : palindrome('madam')")
    print("Expected Output : True")
    print()

    print("Test Case 2")
    print("Input : palindrome('python')")
    print("Expected Output : False")
    print()

    print("Logic:")
    print("This program reverses the string and compares it with the original string.")

    print("\nUser Execution")

    text = input("Enter a String : ")

    reverse = ""

    for i in text:
        reverse = i + reverse

    if text == reverse:
        print("It is a Palindrome.")
    else:
        print("It is not a Palindrome.")

# Program 10 : Check for Prime Number

def prime_number():

    print("Program : Check for Prime Number")
    print()

    print("Code:")
    print("""
def prime_number(num):

    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True
""")

    print("Test Case 1")
    print("Input : prime_number(7)")
    print("Expected Output : True")
    print()

    print("Test Case 2")
    print("Input : prime_number(10)")
    print("Expected Output : False")
    print()

    print("Logic:")
    print("This program checks whether the number is divisible by any value other than 1 and itself.")

    print("\nUser Execution")

    num = int(input("Enter a Number : "))

    if num <= 1:
        print("It is not a Prime Number.")

    else:
        flag = True

        for i in range(2, num // 2 + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            print("It is a Prime Number.")
        else:
            print("It is not a Prime Number.")


# Program 11 : Find Factorial of a Number

def factorial():

    print("Program : Find Factorial of a Number")
    print()

    print("Code:")
    print("""
def factorial(num):

    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact
""")

    print("Test Case 1")
    print("Input : factorial(5)")
    print("Expected Output : 120")
    print()

    print("Test Case 2")
    print("Input : factorial(4)")
    print("Expected Output : 24")
    print()

    print("Logic:")
    print("This program finds the factorial of a given number.")
    print("It multiplies all numbers from 1 to the given number.")

    print("\nUser Execution")

    num = int(input("Enter a Number : "))

    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial =", fact)


# Program 12 : Convert Decimal to Binary

def decimal_to_binary():

    print("Program : Convert Decimal to Binary")
    print()

    print("Code:")
    print("""
def decimal_to_binary(num):

    binary = ""

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    return binary
""")

    print("Test Case 1")
    print("Input : decimal_to_binary(10)")
    print("Expected Output : 1010")
    print()

    print("Test Case 2")
    print("Input : decimal_to_binary(15)")
    print("Expected Output : 1111")
    print()

    print("Logic:")
    print("This program converts a decimal number into binary.")
    print("It repeatedly divides the number by 2.")

    print("\nUser Execution")

    num = int(input("Enter a Decimal Number : "))

    binary = ""

    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2

    print("Binary Number :", binary)

# Program 13 : Find the Largest of Three Numbers

def largest_of_three():

    print("Program : Find the Largest of Three Numbers")
    print()

    print("Code:")
    print("""
def largest_of_three(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c
""")

    print("Test Case 1")
    print("Input : largest_of_three(10, 25, 15)")
    print("Expected Output : 25")
    print()

    print("Test Case 2")
    print("Input : largest_of_three(50, 30, 40)")
    print("Expected Output : 50")
    print()

    print("Logic:")
    print("This program compares three numbers.")
    print("It returns the largest among them.")

    print("\nUser Execution")

    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    c = int(input("Enter Third Number : "))

    if a >= b and a >= c:
        print("Largest Number :", a)

    elif b >= a and b >= c:
        print("Largest Number :", b)

    else:
        print("Largest Number :", c)

# Program 14 : Find Maximum and Minimum in a List

def max_min_list():

    print("Program : Find Maximum and Minimum in a List")
    print()

    print("Code:")
    print("""
def max_min_list(numbers):

    maximum = numbers[0]
    minimum = numbers[0]

    for i in numbers:

        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i

    return maximum, minimum
""")

    print("Test Case 1")
    print("Input : [10, 20, 5, 30]")
    print("Expected Output : Maximum = 30, Minimum = 5")
    print()

    print("Test Case 2")
    print("Input : [50, 15, 70, 25]")
    print("Expected Output : Maximum = 70, Minimum = 15")
    print()

    print("Logic:")
    print("This program finds the maximum and minimum values in a list.")
    print("It compares each element with the current maximum and minimum.")

    print("\nUser Execution")

    data = input("Enter the numbers : ")

    data = data.replace("[", "")
    data = data.replace("]", "")

    if "," in data:
        numbers = list(map(int, data.split(",")))
    else:
        numbers = list(map(int, data.split()))

    maximum = numbers[0]
    minimum = numbers[0]

    for i in numbers:

        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i

    print("Maximum Value :", maximum)
    print("Minimum Value :", minimum)
