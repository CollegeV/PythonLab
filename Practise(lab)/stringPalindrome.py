# WAP to check if string is Palindrome or Not

def main():
    inp = input("Please enter the string: ")
    notp = " not" if inp[::-1] != inp else ""
    print(f"The string is{notp} Palindrome.")

main()

