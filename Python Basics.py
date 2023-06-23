# 1. Accepting 2 numbers from the user and adding them:
try:
    a = float(input("Enter the first number "))  # Accept the first number from the user
    b = float(input("Enter the second number "))  # Accept the second number from the user
    sum = a + b  # Add the two numbers
    print("The total is ", sum)  # Print the sum
except ValueError:
    print("Invalid input. Please enter a valid numeric value.")  # Handle the exception if the input is not numeric


# 2. Deposit and Sums - Digital Piggy Bank 1.0:
total_sum = 0  # Initialize the total sum to 0
while True:
    try:
        income = input("Please enter the amount of money you wish to add or '0' to stop input: ")  # Accept the amount of money from the user
        if income == "0":
            break  # Break the loop if the input is '0'
        income = float(income)  # Convert the input to a floating-point number
        total_sum += income  # Add the income to the total sum
        print(f"The updated total sum is: {total_sum}")  # Print the updated total sum
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")  # Handle the exception if the input is not numeric


# 3. Comparing two user-input numbers and displaying the greater number:
x = float(input("Enter a number: "))  # Accept the first number from the user
y = float(input("Enter another number: "))  # Accept the second number from the user
if x > y:
    print(f"{x} is bigger")  # Print the first number if it is greater
else:
    print(f"{y} is bigger")  # Print the second number if it is greater
