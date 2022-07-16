print("Welcome! Congratulations for taking your first step on your journey to better health")
weight = input("Let's start by getting your weight\n")
height = input("What is your height? Insert height in meters = 1.75\n")
bmi = int(weight) / float(height) ** 2
bmiFinal = int(bmi)
print("Your BMI is " + str(bmiFinal))
