def calculateBMI():
    weight = float(input("Please enter your weight(in kg): "))
    height = float(input("Please enter your height(in meters): "))
    if weight <= 0 or height <= 0:
        print("Please make sure your input is correct.")
        if input("Do you wanna start again? (y/n)") == "y":
            calculateBMI()
        return
    
    bmi = weight / (height**2)
    category = ""
    if bmi <= 18.5:
        category = "Underwight"
    elif bmi <= 24.9:
        category = "Normal"
    elif bmi <= 29.9:
        category = "Overwight"
    else:
        category = "Obesity"

    print(f"Your BMI is {round(bmi, 1)} and BMI category is {category}")
    again = input("Do you wanna calculate for another person? (y/n):  ")
    if again == "y": calculateBMI()

calculateBMI()