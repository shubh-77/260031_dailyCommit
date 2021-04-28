
#Functions to calculate BMI and BMR
def calculate_bmi():
    height = float(input("Enter your height in cms: "))
    weight = float(input("Enter your weight in kgs: "))
    BMI = weight / (height/100)**2
    formatted_float_bmi = "{:.2f}".format(BMI)

    print(f"You Body Mass Index is {formatted_float_bmi}")

    if BMI <= 18.4:
        print("You are underweight.")
    elif BMI <= 24.9:
        print("You are healthy.")
    elif BMI <= 29.9:
        print("You are over weight.")
    elif BMI <= 34.9:
        print("You are severely over weight.")
    elif BMI <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")


# Basal Metabolic Rate Calculator
def calculate_bmr():
    weight = int(input("Enter your weight in kgs: \n"))
    height = int(input("Enter your height in cms: \n"))
    age = int(input("Enter age in years: \n"))
    isMale = str(input("Are you male? (y/n)"))

    if isMale == "y" or isMale == 'Y':
        isMale = True
    elif isMale == "n" or isMale == 'N':
        isMale = False
    else:
        print("Error")
        quit()

    # Mifflin St. Jeor Equation for males
    if isMale:
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    else:
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    bmr = round(bmr)
    print(bmr)
