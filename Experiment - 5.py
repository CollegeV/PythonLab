"""
*** List ***
A list is a sequenece of items or elements, the elements can be of any data type.
"""

# Creating a empty list
myList = list()

# With elements,
myList = list([10, 20,30, 1.1])
myOtherList = ["My", "String", "Elements", "List", "Without", "Constructor"]

# Accessing by index
print(myOtherList[0])

# Accessing by negative index
print(myOtherList[-1])

# Slicing Operator
print(myOtherList[1:3])

# Slicing Operator with Step Size
print(myOtherList[::2])

# List Inbuilt Methods
# Length -> Count of elements
print(len(myList))

# Count -> Number of Appreances of specific element
print(myList.count(10))

# Index -> Find index of particulatr elements
print(myList.index(30))

# Min, Max
print(f"Minimum - {min(myList)}, Maximum - {max(myList)}")

# Sum of elements
print(sum(myList))


#print("__".join(myOtherList))

