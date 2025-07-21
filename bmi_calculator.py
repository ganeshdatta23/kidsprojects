
def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (or 0 to quit): "))
            if weight == 0:
                break
            height = float(input("Enter your height in meters: "))

            if height <= 0:
                print("Height cannot be zero or negative. Please try again.")
                continue

            bmi = weight / (height ** 2)
            print(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                print("Status: Underweight")
            elif 18.5 <= bmi < 24.9:
                print("Status: Normal weight")
            elif 25 <= bmi < 29.9:
                print("Status: Overweight")
            else:
                print("Status: Obesity")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    bmi_calculator()
