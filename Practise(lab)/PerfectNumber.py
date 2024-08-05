def  checkPerfect(n):
    s = 0
    for i in range(1,n): s += (i if n%i == 0 else 0)
    return s == n

def main():
    n = int(input("please enter any number: "))
    if n < 0:
        print("the number should be positive")
    else:
        nott = ' not' if not checkPerfect(n) else ""
        print(f"n is{nott} perfect")
    again = input("do you wish to start again?(y/n): ")
    main() if again == "y" else 0

main()