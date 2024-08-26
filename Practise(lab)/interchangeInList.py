# WAP to interchgange first anfd last element in the list

myList = list()
num = int(input("Enter the number of elements: "))

for i in range(num):
    myList.append(input(f"Enter the element for index {i}: "))

temp = myList[0]
myList[0] = myList[-1]
myList[-1] = temp

print("After interchaging: ")

for i in range(num): print(myList[i], end="\t")

print("\nAfter reversing: ")
myList = myList[::-1]
for i in range(num): print(myList[i], end="\t")