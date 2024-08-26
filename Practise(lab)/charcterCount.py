# WAP that asks tha user, to enter a string, and print the count of each character.
inp = input("Enter a string: ")
counts = dict()

for c in inp:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

for k in counts:
    print(f"Count of {k} in string is {counts[k]}")