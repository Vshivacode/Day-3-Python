# Advance BMI Calculator
# BMI = weight / height ** 2
weight_in_kg = float(input("enter your weight in kg: "))
height_in_feet = float(input("enter your height in feet: "))
meters = height_in_feet * 0.3048  # 1 feet = 0.3048 meters
bmi = round(weight_in_kg / meters ** 2, 2)
if bmi < 18.5:
    print(f'Your BMI is {bmi}, and Your are "Underweight"')
elif bmi < 25:
    print(f'Your BMI is {bmi}, and Your are "Normal weight"')
elif bmi < 30:
    print(f'Your BMI is {bmi}, and Your are "Slightly Overweight"')
elif bmi < 35:
    print(f'Your BMI is {bmi}, and Your are "Overweight"')
elif bmi >= 35:
    print(f'Your BMI is {bmi}, and Your are "Obese"')


# Output:
# Sample - 1
# enter your weight in kg: 80
# enter your height in feet: 6.2
# Your BMI is 22.4, and Your are "Normal weight"

# Sample - 2
enter your weight in kg: 90
enter your height in feet: 5.8
Your BMI is 28.8, and Your are "Slightly Overweight"
