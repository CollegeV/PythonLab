def convert(source, sourceType, targetType):
    timeSeconds = 0.0
    if sourceType == 1: # Seconds
        timeSeconds = source
    elif sourceType == 2: # Minutes
        timeSeconds = source * 60
    elif sourceType == 3: # Hours
        timeSeconds = source * 3600
    elif sourceType == 4: # Days
        timeSeconds = source * 86400
    
    target = 0.0
    if targetType == 1: # Seconds
        target = timeSeconds
    elif targetType == 2: # Minutes
        target = timeSeconds/60
    elif targetType == 3: # Hours
        target = timeSeconds/3600
    elif targetType == 4: # Days
        target = timeSeconds/86400

    return target

def main():
    print("""Please choose your source and target:
1. Seconds
2. Minutes
3. Hours
4. Days""")
    s = int(input("Please enter choice for source: "))
    t = int(input("Please enter your choice for target: "))
    if s <= 0 or s >= 5 or t <= 0 or t >= 5:
        print("Your choice is incorrect. Please choose between 1 and 4 only.")
        return AskToContinueAgain()
    
    source = float(input("Please enter value for source: "))
    if source <= 0:
        print("It must be a positive number.")
        return AskToContinueAgain()
    
    print(f"Converted value is: {convert(source, s, t)}")
    return AskToContinueAgain()

    
def AskToContinueAgain():
    again = input("Do you wish to start again?(y/n): ")
    if again == "y":
        main()
    else:
        print("Exiting!")

# main()

#### Basic inbuilt functions for string
s1 = "Hello World"

# len() -  Returns length of characters in string
print(len(s1))

# min() - smallest character in the string
print(min(s1))

# max() - largest character in the string
print(max(s1))

# index Operator [] - The index operator is used to access the elments of the string
print(s1[0])
print(s1[-1])

# Traversal using for loop
# Evry Character
for i in s1: print(i, end="")
print()

# For every second character
for i in range(0, len(s1), 2):
    print(s1[i], end="")
print()

# Slices of string
print(s1[0:5])

# Slices of string with step size
print(s1[::2])

# Last 5
print(s1[-5:])

# entier string reversed
print(s1[::-1])

## String Methods
# to Upercase
print(s1.upper())

# to lowercase
print(s1.lower())

# find index
print(s1.find("Hello"))

# find and replace
print(s1.replace("World", "vanshit"))

# String Operators
# Concatenation - `+`
print(s1 + ", Bye!")

# Multiplication
print("*" * 30)

# in / not in
print("Hello" in s1)
print("Bye" not in s1)

# String Split Method return a list of allthe words in the string,
# sperated by the given seperator
print(s1.split(" "), s1.split(" ")[1], s1.split(" ")[0], sep="\n")

# Compaines program
compaines = "GOOGLE,TCS,INFOSYS,APPLE"
compaines = compaines.split(",")
print("## Compaines are")
for c in compaines: print("* ", c)

# String stripping methods - removes unwanted whitespace characters from starting or trailing
print("   \t     Hello      \n\n\n     ".strip())

#