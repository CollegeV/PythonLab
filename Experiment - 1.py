## Sub-Section 1
print("Welcome to python lab!")
print()


## Sub-Section 2
radius = 20
area = 3.14 * radius * radius
print("Area of circle is ", area, "Square Units")
print()


## Sub-Section 3
n1 = int(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print("Sum is ", n1+n2)
print()

## Sub Section 4
a = 1
b = 1.0
c = True
d = 1 + 1j
e = "Hello"
f = [True, "A List"]
g = ("A Tuple", True)
h = {"it's": "dictionary"}

def printTypeAndId(val, name):
    print("Type of ", name, " is ", type(val))
    print("Id of ", name, " is ", id(val))
    print()

printTypeAndId(a, "a")
printTypeAndId(b, "b")
printTypeAndId(c, "c")
printTypeAndId(d, "d")
printTypeAndId(e, "e")
printTypeAndId(f, "f")
printTypeAndId(g, "g")
printTypeAndId(h, "h")