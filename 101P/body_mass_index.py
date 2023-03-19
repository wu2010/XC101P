weight, height = map(float, input().split())

BMI = weight / height ** 2

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:  # not BMI < 18.5, i.e. 18.5 <= BMI
    print("Normal")
elif BMI < 30:
    print("Overweight")
elif BMI < 35:
    print("Obesity class1")
elif BMI < 40:
    print("Obesity class 2")
else:  # not BMI < 40, i.e. BMI >= 40
    print("Obesity class 3")
