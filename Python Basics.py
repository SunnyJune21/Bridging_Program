# 1. Accepting 2 numbers from the user and adding them
try:
    a = float(input("Enter the first number "))
    b = float(input("Enter the second number "))
    sum = a + b
    print("The total is ", sum)
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")  # Handle the exception if the input is not numeric


# 2. Deposit and Sums - Digital Piggy Bank 1.0
total_sum = 0  # Initialize the total sum to 0
while True:
    try:
        income = input("Please enter the amount of money you wish to add or '0' to stop input: ")
        if income == "0":
            break  # Break the loop if the input is '0'
        income = float(income)
        total_sum += income  # Add the income to the total sum
        print(f"The updated total sum is: {total_sum}")  # Print the updated total sum
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")  # Handle the exception if the input is not numeric


# 3. Comparing two user-input numbers and displaying the greater number
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
if x > y:
    print(f"{x} is bigger")  # Print the first number if it is greater
else:
    print(f"{y} is bigger")  # Print the second number if it is greater


# 4. Convert centimeters (cm) to meters (m)
cm = float(input("Please enter cm: "))
print(cm, "cm equal to", cm/100, "m")


# 5. Convert from Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = c*9/5+32
print(c, "Celsius =",f,"Fahrenheit")
