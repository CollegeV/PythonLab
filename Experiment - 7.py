# creating sets
names = {"sohag", "krishna", "vanshit", "strawberry"}
fruits = set(["apple", "banana", "strawberry"])
print("Names are", names)
print("Fruits are", fruits)

# set operations
unionSet = names.union(fruits)
intersectionSet = names.intersection(fruits)
difference = names.difference(fruits)
symettericDifference = names.symmetric_difference(fruits)
print("Union of fruits and names", unionSet)
print("Intersection of fruits and names", intersectionSet)
print("Names - Fruits == ",difference)
print("Symmetric Difference is", symettericDifference)

# Adding and Removing element
names.add("Ghost")
print("Names with a ghost", names)
names.remove("strawberry")
print("Names without strawberry", names)

# Len, Maximum, Minimum, Sum
numbers = {2,54,3,6,34,35,65}
print("Numbers are", numbers)
print("Count of numbers(length of set)", len(numbers))
print("Maximum", max(numbers))
print("Minimum", min(numbers))
print("Sum", sum(numbers))

#Converting to list, maybe for sorting/custom ordering/repetive elements
numList = list(numbers)
print("List representsion", numList)

print("\n\n\n\n Dictionary \n\n\n\n")
# creating dictionary
myDict = {
    "name": "Vanshit",
    "age": 20,
    "nationality": "Indian"
}
nameToState = dict(vanshit="Punjab", sohag="Kolkata", krishna="Jammu")

print("My Dict is", myDict)
print("name to state mappping", nameToState)

# Accessing and Modifying particular elenets
print("Name is", myDict.get("name"))
print("Age is", myDict["age"])

# Modification
myDict["nationality"] = "American"
print("After modification", myDict)

# Adding new key-value pair
myDict["college"] = "CU"
print("After adding new kv pair", myDict)

#Dictionary MEthods
print("Keys are", myDict.keys())
print("Values are", myDict.values())
print("Items are", myDict.items())

# Delete item from dict
myDict.pop("nationality")
print(myDict)