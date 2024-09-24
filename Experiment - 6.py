T1 = ()
T2 = (42,) # Note: a Comma "," is mandatory here.
T3 = (22, 'abc')
T4 = ((1,2), [1,2,3], [1,2,3,4], 2.5)
T5 = (1,33,44,543,55,4)

print (T1)
print (T2)
print (T3)
print (T4)

# Operators
print (T4[0])
print (T5[2:6:2])
print(T2 + T5) # concat
print(T2 * 5) # repetition
print(str(T5), type(str(T5))) #str

# Find Index
print (T4.index(2.5))

# Count of particular element
print (T4.count(1))

# Length. Minimum, Maximum, Summition
print(len(T4))
print(min(T5))
print(max(T5))
print(sum(T5))

# List to tuple, and vice-versa
L1 = [1,22,34,55,667]
T6 = tuple(L1)
L2 = list(T3)
print(T6)
print(L2)

# Sorting by converting to list
L3 = list(T5)
L3.sort()
T5 = tuple(L3)
print (T5)

# Directly
print(sorted(T5), type(sorted(T5)))

# Returning multiple values # Note: Will return as tuple
def call_val(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b if b != 0 else None
    return add, subtract, multiply, divide

results = call_val(5, 3)
print(results)











