#BMI 2.0
while True:
    #Gettig Height and Weight from Users
    height = float(input("Enter your Height in Metres : "))
    weight = int(input("Enter your Weight in KG : "))
    #BMI calculatin
    BMI = round((weight/(height**2)))
    if BMI <= 18.5:
        print(f"{BMI}, you are Underweight")
    elif BMI >18.5 and BMI < 25:
        print(f"{BMI}, you have Normal Weight")
    elif BMI >25 and BMI < 30:
        print(f"{BMI}, You are Overweight")
    elif BMI >30 and BMI <=35:
        print(f"{BMI}, You are Obese")
    else:
        print(f"{BMI}, You are Crinically Obese")

