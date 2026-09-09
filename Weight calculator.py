Height:float = float(input("Enter your height in meters: "))
Weight:float = float(input("Enter your weight in kilograms: "))
Name:str = input("Enter your name: ")
BMI:float = Weight / (Height ** 2)  
if 18.5 <= BMI < 25:
    print(f"{Name}, your BMI is {BMI:.2f}, which is considered normal.")
elif BMI < 18.5:
    print(f"{Name}, your BMI is {BMI:.2f}, which is considered underweight.")
else:
    print(f"{Name}, your BMI is {BMI:.2f}, which is considered overweight.")