# Arthematic Operators
# +, -, /, %, *
# Boolean Operators
# and, or, not
# Relational Operators
# >, <, <=, >=, ==, !=
# Bitwise operatators
# &, |, ~, <<, >>

# WAP to calculate the sum between 1 to 30 that are divisible by 2, 3 or 5.

# print(sum([i if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else 0 for i in range(31)]))

# WAP to read two nmbers from the user and dsiplay the result using bitwise and operator and or operator and XOR

# a = int(input("Input first Number: "))
# b = int(input("Input second Number: "))
# print("OR", a | b)
# print("XOR", a ^ b)
# print("AND", a & b)

# WAP to demonstrate the use of function to print a message
# def printMessage():
#     print("Hello World@")

# printMessage()

# WAP to add sum of digits from 1 to 25 then from 50 to 75 then from 80 to 100

# s = 0
# for i in range(1, 26):
#     s+=i
# print(s)

# s=0
# for i in range(50, 76):
#     s+=i
# print(s)

# s=0
# for i in range(80, 101):
#     s+=i
# print(s)

# def printSumRange(x,y):
#     print(sum([i for i in range(x, y+1)]))


# printSumRange(1,25)
# printSumRange(50,75)
# printSumRange(80,100)


# WAP to demonstrate the use of return statement by retuyrning the min of two numbers.
# def minTwo(a,b):
#     return min(a,b)

# print(minTwo(100,85))



# WAP to calculate factorial of a number
# def factorial(n):
#     if n <= 1:
#         return n
#     else:
#         return n * factorial(n-1)

# print(factorial(int(input("Enter number: "))))


# Lambda function
# cube = lambda x: x**3
# print(cube(3))

a = int(input("Enter the number of rows: "))

for i in range(a): # i from 0 to 4
    for j in range(a, i, -1): # j from 5 to 1 then 5 to 4
        print(j, end='')
    for j in range(i):
        print("*",  end='')
    print(i, end='')
    print(a+i,  end='')
    print()

