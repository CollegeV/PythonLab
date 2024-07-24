# Arthematic Operators
# +, -, /, %, *
# Boolean Operators
# and, or, not
# Relational Operators
# >, <, <=, >=, ==, !=
# Bitwise operatators
# &, |, ~, <<, >>

# WAP to calculate the sum between 1 to 30 that are divisible by 2, 3 or 5.

print(sum([i if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else 0 for i in range(31)]))

# WAP to read two nmbers from the user and dsiplay the result using bitwise and operator and or operator and XOR

a = int(input("Input first Number: "))
b = int(input("Input second Number: "))
print("OR", a | b)
print("XOR", a ^ b)
print("AND", a & b)