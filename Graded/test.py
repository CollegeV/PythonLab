vowels = "aeiouAEIOU"

inp = "Hello World"
count = 0
for c in inp:
    if c in vowels: count+=1
print(count)
