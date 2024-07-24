# Subsection - 1
# print("[+] Subsection - 1")
# print("Check if number is even or odd")
# n = int(input("Enter the number: "))
# if n % 2 == 0:
#     print("Number is even.")
# else:
#     print("Number is odd.")
# print()


# Subsection - 2
# print("[+] Subsection - 2")
# print("Print range of numbers from 1 to 10")
# for i in range(1, 11):
#     print(i)
# print()

# Subsection - 3
# Write a program that asks the users to enter the days of a week, if the day is between 1 to 7 display the respective name.
# print("[+] Subsection - 3")
# day = eval(input("Enter the day of week: "))
# if day > 7 or day < 1:
#     print("Sorry! Day doesn't exist")
# elif day == 1:
#     print("It's Monday.")
# elif day == 2:
#     print("It's Tuesday.")
# elif day == 3:
#     print("It's Wednesday.")
# elif day == 4:
#     print("It's Thursday.")
# elif day == 5:
#     print("It's Friday.")
# elif day == 6:
#     print("It's Saturday.")
# elif day == 7:
#     print("Hurrah! It's Sunday.")
# print()

# Subsection - 4
# Write a Program to enter two numbers and perform basic arthematic operations, depending on the choice.
# print("[+] Subsection - 4")
# a = int(input("Enter the first number - "))
# b = int(input("Enter the second number - "))
# print("""Supported Operations - 
# 1. Addition
# 2. Substraction
# 3. Divison
# 4. Multiplication
# 5. Exponent""")


# choice = int(input("Enter your choice please: "))
# if choice == 1:
#     print(f"Result is : {a+b}")
# elif choice == 2:
#     print(f"Result is : {a-b}")
# elif choice == 3:
#     print(f"Result is : {a/b}")
# elif choice == 4:
#     print(f"Result is : {a*b}")
# elif choice == 5:
#     print(f"Result is : {a**b}")
# else:
#     print("Sorry! Operation isn't supported.")
# print()



# Subsection - 5
# WAP to DEMONSTRATE THE USE OF BREAK STATEMENT
# print("[+] Subsection - 5")
# upto = int(input("Enter the range upto which you want to print numbers: "))
# i = 0
# while True:
#     if i > upto:
#         break
#     print(i)
#     i+=1

# Subsection - 6
# WAP to DEMOSTRATE THE USE OF CONTINUE STATEMENT
# print("[+] Subsection - 6")
# upto = int(input("Upto which you wanna print even numbers: "))
# i = 0
# while i < upto:
#     i+=1
#     if i % 2 != 0:
#         continue
#     print(i)
# print()

# Subsection - 7
# WAP to print numbers from 1 to 20 that are divisible by 5 and find their sum using while loop
# print("[+] Subsection - 7")
# i, s = 0, 0
# while i <= 20:
#     i += 1
#     if i % 5 == 0:
#         print(i)
#         s += i
# print("Sum is ", s)

# Subscetion - 8
# Write a progfram to print factorial of a number using while loop
# print("[+] Subsection - 8")
# i = int(input("Enter number to find factorial: "))
# f = 1
# while i != 1:
#     f *= i
#     i -= 1
# print(f)