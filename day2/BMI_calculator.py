# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_squared = float(height) * float(height)
BMI = float(weight) / height_squared
print(BMI)

if BMI < 18.5:
    print("You are Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You have a normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("You are overweight")
elif BMI >= 30 and BMI <= 39.9:
    print("You are obesed")
else:
    print("Yor are fatally obesed")