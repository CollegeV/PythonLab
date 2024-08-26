"""
A language learning app needs a function to reverse wordorder in sentences for translation excercirse. Implement
a function reverse_function(s: str) -> str that reverses the order of words in a sentences.
"""

def reverse_str_words(s):
    return " ".join(s.split(" ")[::-1])

def main():
    s = input("Please enter a string: ")
    print("Reversed is: ")
    print(reverse_str_words(s))

    again = input("Do you want to start again?(y/n): ")
    if again == "y": main()

main()