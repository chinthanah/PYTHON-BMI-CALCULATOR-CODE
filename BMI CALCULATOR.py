	BMI CALCULATOR PYTHON CODE

name=input('Enter your name:')
weight=int(input('enter your weight in pounds:'))
height=int(input('enter your height in inches:'))
BMI = (weight * 703)/(height * height)
print(BMI)
if BMI>0:
    if BMI<18.9:
        print(name+', you are Underweight')
    elif BMI<24.9:
        print(name+', you are Normal weight')
    elif BMI<29.9:
        print(name+', you are Overweight')
    elif BMI<34.9:
        print(name+', you are Obese')
    elif BMI<39.9:
        print(name+', you are Severly Obese')
    else:
        print(name+', you are Morbidly Obese')







