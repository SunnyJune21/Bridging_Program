# 1. Addition Function
def add(a, b):
  sum = a + b
  print("The sum is", sum)

add(3, 5)
add(15, 30)


# 2. Youngest Sibling - Keyword Arguments
def siblings(child4, child2, child1, child3):
  print("The youngest is", child4)

siblings("Jasmine", "Cinderella", "Ariel", "Belle")


# 3. Youngest Child - Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emily", "Tobias", "Belle", "Linus", "Alice")


# 4. Child Information - Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# 5. The Pass Statement
def my_function():
  pass


# 6. Triangular Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)


# 7. Grade Function with Loop
def grades():
  marks = input("Enter your marks ")
  print("You got", marks, "score")

for i in range(3):
  grades()


# 8. Grade Function with Arguments
def grades(name, mark):  # parameters
  x = mark / 10
  print(name + ", you got", x, "score")

# Main code
name1 = input("Enter your name: ")
mark1 = int(input("Enter your mark: "))

name2 = input("Enter your name: ")
mark2 = int(input("Enter your mark: "))
print()

print("Final results/grades")
grades(name1, mark1)  # argument
grades(name2, mark2)


# 9. Character Count
def counts(word):
  print("The sentence/word has", len(word), "character(s)")

# Main code
userinput = input("Enter a sentence/word: ")
while userinput.lower() != "quit":  # Converted user input to lowercase for case-insensitive comparison
  counts(userinput)
  userinput = input("Enter a sentence/word or 'quit' to end: ")
else:
  print("Thank you")


# 10. Passing a List as an Argument
def my_function(fruits):
  for x in fruits:
    print(x)

fruits = ["apple", "orange", "cherry"]
my_function(fruits)


# 11. Arithmetic Calculator
def add(a, b):
  sum = a + b
  print("The result is", sum)

def sub(a, b):
  sub = a - b
  print("The result is", sub)

def mul(a, b):
  mul = a * b
  print("The result is", mul)

def div(a, b):
  div = a / b
  print("The result is", div)

# Main code
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
operation = input("Enter a choice of calculation (add, subtract, multiply or divide): ")

if operation == "add":
  add(x, y)
  print("When we", operation, x, "and", y, "we get", x + y)
elif operation == "subtract":
  sub(x, y)
  print("When we", operation, x, "and", y, "we get", x - y)
elif operation == "multiply":
  mul(x, y)
  print("When we", operation, x, "and", y, "we get", x * y)
elif operation == "divide":
  div(x, y)
  mod = x % y
  div = x // y
  print(div, "reminder", mod)
  print("When we", operation, x, "and", y, "we get", x / y)
else:
  print("Error, that was not an option")


# 12. Arithmetic Calculator using while loop
def add(a, b):
  sum = a + b
  print("The result is", sum)

def sub(a, b):
  sub = a - b
  print("The result is", sub)

def mul(a, b):
  mul = a * b
  print("The result is", mul)

def div(a, b):
  remainder = a % b
  quotient = a // b
  print(quotient, "remainder", remainder)
  print("The result is", quotient)

# Main code
operation = None

while operation != "0":
  x = float(input("Enter a number: "))
  y = float(input("Enter another number: "))
  operation = input("Enter a choice of calculation (add, subtract, multiply or divide) or '0' to quit: ")

  if operation == "add":
    add(x, y)
    print("When we", operation, x, "and", y, "we get", x + y)
  elif operation == "subtract":
    sub(x, y)
    print("When we", operation, x, "and", y, "we get", x - y)
  elif operation == "multiply":
    mul(x, y)
    print("When we", operation, x, "and", y, "we get", x * y)
  elif operation == "divide":
    div(x, y)
    print("When we", operation, x, "and", y, "we get", x / y)
  elif operation == "0":
    print("Thank you for using the calculator. Have a great day!")
  else:
    print("Error, that was not an option")
    break
  print()


# 13. Square Calculation - Without argument and returning the result
def square():
  userinput = float(input("Enter a number: "))
  total = userinput*userinput
  return total

# Main code
square_result = square()
print("The result is", square_result)


# 14. Square Calculation - Without argument and printing the result
def square():
  userinput = float(input("Enter a number: "))
  total = userinput*userinput
  print("The result is", total)
  return total

# Main code
square()


# 15. Square Calculation - With argument
def square(x):
  total = x * x
  return total

# Main code
userinput = float(input("Enter a number: "))
result = square(userinput)
print("The result is", result)


# 16. Function to calculate the 5th power of a number
def p(x):
  s=x**5
  return s

# Main code
userinput = float(input("Please enter a number: "))
power = p(userinput)
print("The 5th power of", userinput, "is", power)


# 17. Function to calculate the power of a number
def p(x, y):  #parament
  return pow(x, y)  # x = number, y = power

# Main code
userinput1 = float(input("Please enter a number: "))
userinput2 = float(input("Please enter the number of power: "))
power = p(userinput1, userinput2)
print("The power", userinput2, "of your number", userinput1, "is", power)


# 18. Function to display a message without arguments
def msg():
  message = input("Enter the message you wish to display: ")
  print(message)

# Main code
msg()  # Calling the function without arguments


# 19. Function to display a message with an argument
def msg(text):
  print("Your message is:", text)

# Main code
userinput = input("Please leave a message: ")
msg(userinput) # Calling the function with an argument


# 20. Function to print a message about a pet
def myPet(typePet, namePet):
  print("Your", typePet, namePet, "is adorable!")

# Main code
myPet(typePet = "dog", namePet = "Coco")
myPet(namePet = "Honey", typePet = "cat")

myPet("kitty",namePet="Melowrd")
print()

x = input("Enter the name of your rabbit: ")
myPet("rabbit", namePet = x)


# 21. Function to print a message about a pet
def myPet(namePet, typePet = 'dog'):
  print("Your", typePet, namePet, "is adorable!")

# Main code
myPet("Silly", "cat")
myPet("Wooly")   # Call the function with only namePet specified, typePet defaults to 'dog'


# 22. Function to convert Celsius to/from Fahrenheit
# Function to convert Celsius to Fahrenheit
def oF(x):
  f = x * 1.8 + 32
  return f

# Function to convert Fahrenheit to Celsius
def oC(x):
  c = (x - 32) / 1.8
  return c

# Main code
operation = input("Type 'c' to convert from Celsius or 'f' to convert from Fahrenheit: ")

if operation.lower() == "f":
  a = float(input("Enter value in Fahrenheit: "))
  print(a, "°F is equate to", oC(a), "°C")
elif operation.lower() == "c":
  a = float(input("Enter value in Celsius: "))
  print(a, "°C is equate to", oF(a), "°F")
else:
  print("Error, that was not an option")


# 23. Function to simulate toddler's mood and wants
def toddler(mood, want = "candy"):
  print("The baby is", mood + " and wants", want +".")

# Main code
operation = input("What's the baby's mood (happy, sad, crying): ")

if operation.lower() == "happy":
  toddler("happy")
  print("Sure, you can have candy.")
elif operation.lower() == "sad":
  toddler("sad", want = "a bear")
  print("This will help you stop crying.")
elif operation.lower() == "crying":
  toddler("crying", want = "a hug")
  print("I will give you a hug.")
else:
  print("Sorry, I didn't recognize that mood.")


# 24. Function to find the maximum of two numbers
def maximum(x, y):
  return max(x, y)

# Main code
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

print("The maximum number is", maximum(a, b))


# 25. Function to find the maximum of three numbers
def max_num(x, y, z):
  return max(x, y, z)

# Main code
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
c = float(input("Enter the 3rd number: "))

print("The maximum number is", max_num(a, b, c))


# 26. Write a code to find even or odd numbers using function
def num(i):
  if i % 2 == 0:
    print("This is an even number.")
  if i % 2 != 0:
    print("This is an odd number.")

# Main code
n = float(input("Enter the number: "))
num(n)


# 27. Function to split the input time into hours, minutes, and AM/PM
def split_Time(time):
  t, ampm=time.split()
  h, m=t.split(":")
  return get_24hr_format(h, ampm), m

def get_24hr_format(hh, ampm):
  hh = int(hh)
  if ampm == "pm":
    if hh != 12:
      hh = hh + 12
  elif hh == 12:
    hh = "00"
  return hh

# Main code
answer = 'yes'
while answer == "yes":
  time = input("Enter time in 12-hour format (HH:MM AM/PM): ")
  hours_24hr, minutes = split_Time(time)
  print("The time in 24-hour format is:", hours_24hr, "hours", minutes, "minutes")
  answer = input("Do you want to convert another time (yes/no)? ").lower()


# 28. Function to calculate the BMI category
def bmi_calc(w,h):
  bmi = round(w/(h**2), 4)
  return bmi

def bmi_category(bmi):
  if bmi <= 18.5:
    return "underweight"

  elif bmi <= 24.9:
    return "normal"

  elif bmi <= 29.9:
    return "overweight"

  else:
    return "obese"

# Main code
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = bmi_calc(weight, height)
print("Your BMI is", bmi)
print("Your BMI category is", bmi_category(bmi))


# 29. BMI Calculator and BMI List
def bmi_calc(w,h):
  bmi = round(w/pow(h, 2), 4)

  if bmi <= 18.5:
    return "Your BMI shows you are underweight"

  elif bmi <= 24.9:
    return "Your BMI shows you are normal"

  elif bmi <= 29.9:
    return "Your BMI shows you are overweight"

  else:
    return "Your BMI shows you are obese"

# Main code
bmi_list = []
userinput = "yes"
while userinput.lower() == "yes":
  weight = float(input("Enter your weight in kg: "))
  height = float(input("Enter your height in m: "))
  bmi_result = round(weight / (height**2), 4)

  print("Your BMI is", bmi_result)
  print(bmi_calc(weight, height))

  bmi_list.append(bmi_result)
  print(bmi_list)
  print()
  user_input = input("Do you want to calculate another BMI (yes/no)? ")

if userinput.lower() == "no":
  print("The final BMI list is", bmi_list)
