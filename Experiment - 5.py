"""
*** List ***
A list is a sequenece of items or elements, the elements can be of any data type.
"""

def printListSpecial(myl):
    for i in myl: print(i, end=" ")
    print()

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

# Random SAhuffling
import random
newList = [1,2,3,4,5,6,7,8,9]
random.shuffle(newList)
print(newList)


# Append - element at end
myList.append(400)
print(myList)


#Insert - element at index
myList.insert(2, 666)
print(myList)

#EXtends - Iterable at the end
myList.extend(newList)
print(myList)

# Remove - Remove The given elemnt
myList.remove(666)
print(myList)

#Pop - removes the toppest/last element
print(myList.pop())
print(myList)


# Reverse
myList.reverse()
print(myList)

# sort
myList.sort()
print(myList)

# copy
xyzList = myList.copy()
printListSpecial(xyzList)

#clear
xyzList.clear()
print(xyzList)

# WAP to check whether list is a plaindrome or not

def isPalindrome(l1: list):
    return l1 == l1[::-1]

l1 = [14, 3, 5, 1, 2, 4, 6, 5, 43, 78, 33, 11, 15, 77, 45, 23]
l2 = [1,2,3,2,1]
print(l1, "IsPalindrome:", isPalindrome(l1))
print(l2, "IsPalindrome:", isPalindrome(l2))

# WAP to return prime numbers from list

def primeList(l1: list):
    onlyPrime = l1.copy()
    for i in l1:
        if not isPrime(i):
            onlyPrime.remove(i)
    return onlyPrime


def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    

# WAP to assign grades based on marks in a list

def getGrades(l: list) -> list:
    for i in range(len(l)+1):
        if l[i] >= 90: l[i] = 'A'
        elif l[i] >= 80: l[i] = 'B'
        elif l[i] > 65: l[i] = 'C'
        elif l[i] > 40: l[i] = 'D'
        else: l[i] = 'F'


print(getGrades([78, 90, 34, 56, 39]))