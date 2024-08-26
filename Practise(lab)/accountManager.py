
initial_value = 1000000000

def open_account(name: str, initial_deposit: float) -> str:
    global initial_value
    initial_value += 1
    return str(initial_value)


def main():
    name = input("Please enter your name: ")
    deposit = float(input("Please enter your initial deposit amount: "))
    print("Your account no. is: ", open_account(name, deposit))

    if input("Do you want to start again? (y/n) - ") == "y": main()

main()