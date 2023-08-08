# 1. Message Class - Printing a Message
class Message:
  msg = "Hello, World!"

  def print_message(self):
      print(self.msg)

# Main code
obj = Message()
obj.print_message()


# 2. Bike Class - Bike with Name
class Bike:
  def __init__(self, name = ""):
      self.name = name

# Main code
bike1 = Bike("Mountain Bike")
print(bike1.name)


# 3. Car Class - Car with Brand and Color
class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color

  def say_detail(self):
    print("The car", self.brand, "is", self.color, "in color")

# Main code
c1 = Car("BMW", "blue")
c2 = Car("Toyota", "red")
c1.say_detail()
c2.say_detail()


# 4. Person Class - A Simple Person Representation
class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is', self.name)

# Main code
p1 = Person('Emma')
p1.say_hi()


# 5. Animal Class
class Animal:
  def set_name(self, name):
      self.name = name

  def speak(self):
      pass

class Dog(Animal):
  def speak(self):
      print("Woof!")

class Cat(Animal):
  def speak(self):
      print("Meow!")

# Main code
dog = Dog()
dog.set_name("Buddy")
dog.speak()

cat = Cat()
cat.set_name("Whiskers")
cat.speak()


# 6. Dog class
class Dog():
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.breed = "husky"
    print("testing")

  def printInfo(self):
    print("Your dog", self.name, " is ", self.age, "years old.")
    print("Your dog is a",self.breed,".")

  def sit(self):
    print(self.name, "is now sitting.")

# Main code
dogA = Dog("Poppy", 2)
dogA.breed = "Puppy"
print(dogA.breed)


# 7. Addition class - Addition of two values
class Addition:
  # Constructor (init method) without parameters
  def __init__(self):
    self.v1 = 30
    self.v2 = 70

  def add(self):
    print("The sum is", self.v1 + self.v2)

# Main code
p1 = Addition()
p1.add()


# 8. Addition class - Addition of two user-input numbers
class Addition:
  # Constructor (init method) that takes user input to initialize "v1" and "v2"
  def __init__(self):
    self.v1 = int(input("Enter a number: "))
    self.v2 = int(input("Enter another number: "))

  def add(self):
    print("The sum is", self.v1 + self.v2)

# Main code
p1 = Addition()
p1.add()


# 9. Triangle class - Area of a triangle
class Triangle:
  def area(self):
    b = float(input("Enter the base: "))
    h = float(input("Enter the height: "))
    self.area = round(0.5 * b * h, 4)
    print("The area of the triangle is", self.area)

# Main code
tri2 = Triangle()
tri2.area()


# 10. Triangle class - Area of a triangle using the side lengths provided by the user
class Triangle:
  def area(self):
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))
    s = (a + b + c) / 2
    self.area = round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 4)
    print("The area of the triangle is", self.area)

# Main code
tri1 = Triangle()
tri1.area()


# 11. Triangle class - Area of a triangle using side lengths provided by the user
class Triangle:
  def __init__(self):
    self.a = float(input("Enter first side: "))
    self.b = float(input("Enter second side: "))
    self.c = float(input("Enter third side: "))

  def area(self):
    self.s = (self.a + self.b + self.c)/2
    self.area = round((self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5, 4)
    print("The area of the triangle is", self.area)

# Main code
tri3 = Triangle()
tri3.area()


# 12. Square class - Area and perimeter of a square using the side length provided by the user
class square:
  def __init__(self):
    self.a = int(input("Enter a side of a square: "))

  def area(self):
    area = self.a ** 2
    print("The area of the square is", area)

  def perimeter(self):
    p = self.a * 4
    print("The perimeter of the square is", p)

# Main code
s1 = square()
s1.area()
s1.perimeter()


# 13. Square class - Perimeter and area of a square using the side length provided by the user
class sq:
  def __init__(self):
    self.a = int(input("Enter the side length of the square: "))

  def area(self):
    perimeter = 4 * self.a
    area = self.a ** 2
    print("The perimeter of the square is", perimeter)
    print("The area of the square is", area)

# Main code
p1 = sq()
p1.area()


# 14. Circle Class - Area and Perimeter Calculator
class Circle():

    def __init__(self):
        self.radius = float(input("Enter the radius in cm: "))

    def area(self):
        self.area = round(2 * 3.14 * self.radius, 2)
        print("The area of a circle is", self.area, "cm²")

    def perimeter(self):
        self.perimeter = round(3.14 * self.radius ** 2, 2)
        print("The perimeter of a circle is", self.perimeter, "cm")

# Main code
c1 = Circle()
c1.area()
c1.perimeter()
print()

c2 = Circle()
c2.area()
c2.perimeter()


# 15. Restaurant class - To describe the restaurant and display that it's open
class Restaurant:
  def __init__(self):
    self.restaurant_name = input("Enter the restaurant's name: ")
    self.cuisine_type = input("Enter the cuisine type: ")

  def describe_restaurant(self):
    print("The restaurant,", self.restaurant_name, ", serves a famous dish called", self.cuisine_type)

  def open_restaurant(self):
    print("The restaurant,", self.restaurant_name, ", is open.")

# Main code
r1 = Restaurant()
r1.describe_restaurant()
r1.open_restaurant()


# 16. Restaurant class - To describe the restaurant and display that it's open
class Restaurant():
  def __init__(self, n, ct):
    self.restaurant_name = n
    self.cuisine_type = ct

  def describe_restaurant(self):
    print(self.restaurant_name.title() + " serves wonderful " + self.cuisine_type + ".")

  def open_restaurant(self):
    print(self.restaurant_name.title() + " is open. Come on in!")

# Main code
restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type)
print()
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 17. User class - User's information
class User:
  def __init__(self, first_name, last_name, username, email):
    self.first_name = first_name.title()
    self.last_name = last_name.title()
    self.username = username
    self.email = email

  def describe_user(self):
    print(self.first_name, self.last_name + ":")
    print(" Username:", self.username)
    print(" Email address:", self.email)

  def greet_user(self):
    print("\nWelcome back,", self.first_name + ":) \n")

# Main code
u1 = User("emma", "watson", "emmawatson", "ew@gmail.com")
u1.describe_user()
u1.greet_user()

u1 = User("tom", "cruise", "tomcruise", "tc@gmail.com")
u1.describe_user()
u1.greet_user()


# 18. User class - User's information and login attempts
class User:
    def __init__(self, first_name, last_name, username, email, password, login_attempts):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)

    def greet_user(self):
        print("\nWelcome back, " + self.last_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Main code
eric = User("eric", "matthes", "ematthes", "e_matthes@example.com", "em123", 0)
willie = User("Willie", "Burger", "wburger", "wb@example.com", "wb567", 0)

max_attempts = 3
username_attempts = 0
while username_attempts < max_attempts:
    username_input = input("Please enter your username: ")
    if username_input == eric.username or username_input == willie.username:
        break
    else:
        username_attempts += 1
        remaining_attempts = max_attempts - username_attempts
        print(f"Incorrect username. Attempt {username_attempts} of {max_attempts}. "
              f"Remaining attempts: {remaining_attempts}")
else:
    print("Too many incorrect attempts. Please double check your username.")
    exit()

if username_input == eric.username:
    while eric.login_attempts < max_attempts:
        password_input = input("Please enter the password: ")
        if password_input == eric.password:
            print("Logged in successfully!")
            eric.describe_user()
            eric.greet_user()
            break
        else:
            eric.increment_login_attempts()
            remaining_attempts = max_attempts - eric.login_attempts
            print(f"Incorrect password. Attempt {eric.login_attempts} of {max_attempts}. "
                  f"Remaining attempts: {remaining_attempts}")

    if eric.login_attempts >= max_attempts:
        print("Too many incorrect attempts. Please check your password.")
        eric.reset_login_attempts()

if username_input == willie.username:
    while willie.login_attempts < max_attempts:
        password_input = input("Please enter the password: ")
        if password_input == willie.password:
            print("Logged in successfully!")
            willie.describe_user()
            willie.greet_user()
            break
        else:
            willie.increment_login_attempts()
            remaining_attempts = max_attempts - willie.login_attempts
            print(f"Incorrect password. Attempt {willie.login_attempts} of {max_attempts}. "
                  f"Remaining attempts: {remaining_attempts}")

    if willie.login_attempts >= max_attempts:
        print("Too many incorrect attempts. Please check your password.")
        willie.reset_login_attempts()


# 19. Planet class - A planet and its properties
class Planet:
  def __init__(self):
      self.diameter = float(input("Enter the diameter: "))
      self.color = input("Enter the color: ")

  def getArea(self):
      area = float(round(3.14 * (self.diameter ** 2), 2))
      print("The area of the planet is", area, "km²")

  def getDiameter(self):
      print("The diameter of the planet is", self.diameter, "km")

# Main code
p1 = Planet()
print("A new planet is born:", p1.color, "and", p1.diameter, "km in size")
p1.getArea()
print()

p2 = Planet()
print("A new planet is born:", p2.color, "and", p2.diameter, "km in size")
p2.getArea()
print()

if p1.diameter > p2.diameter:
  print('The ' + p1.color + ' planet is larger.')
elif p2.diameter > p1.diameter:
  print('The ' + p2.color + ' planet is larger.')
else:
  print('They are the same size.')


# 20. Employee Class - Manages Employee Information
class Employee:
    def __init__(self, name, id, salary, dept):
        self.name = name.title()
        self.id = id
        self.salary = salary
        self.department = dept.title()

    def calculate_emp_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))
        print(self.name, "total salary for the month is", self.salary)

    def emp_assign_department(self, emp_department):
        self.department = emp_department.title()
        print(self.name, "is now changed to", self.department, "department")

    def print_employee_details(self):
        print(" Name:", self.name, "\n Employee ID:", self.id, "\n Monthly Salary:", self.salary, "\n Department:",
              self.department, "\n")

# Main code
print("The original employee's details are: ")
adams = Employee("adams", "E7876", 50000, "accounting")
adams.print_employee_details()

jones = Employee("jones", "E7499", 45000, "research")
jones.print_employee_details()

martin = Employee("martin", "E7900", 50000, "sales")
martin.print_employee_details()

smith = Employee("smith", "E7698", 55000, "operations")
smith.print_employee_details()

# Change the departments of an employee
adams.emp_assign_department("IT")
jones.emp_assign_department("Tax")
print()

# Calculate monthly salary & overtime pay for specific employees
adams.calculate_emp_salary(50000, 52)
smith.calculate_emp_salary(55000, 60)
print()

# Print the updated details of employees
print("The updated employee's details are: ")
adams.print_employee_details()
jones.print_employee_details()
martin.print_employee_details()
smith.print_employee_details()


# 21. Inheritance - University class - A university, employee and student's information
# Base class: University
class University:
    def __init__(self, name, id):
        print("A new object is created\n")
        self.name = name
        self.id = id

    def getID(self):
        return self.id

    def firstName(self):
        fname, lname = self.name.split()
        return fname

    def fullName(self):
        return self.name

# Subclass: Employee (inherits from University)
class Employee(University):
    def __init__(self, name, id, salary, title):
        super().__init__(name, id)
        self.salary = salary
        self.title = title

    def printAnnualSalary(self):
        print(self.name, "earns", self.salary * 12, "per year")

    def fullName(self):
        return self.title + ". " + self.name

# Subclass: Student (inherits from University)
class Student(University):
    def __init__(self, name, id, courselist):
        super().__init__(name, id)
        self.courseList = courselist

    def numCourses(self):
        return len(self.courseList)

# Main Code
A = University("Albert Einstein", 1788)
print("A is an employee named", A.firstName())

B = University("Hareem Nisar", 1200)
print("B is a student with ID", B.getID())

C = Employee("Aysha Mansoor", 8597, 5000, "Prof")
print(C.firstName())
print(C.fullName())
C.printAnnualSalary()

D = Student("Mandeep", 11, ["Python", "Java", "C++"])
print(D.getID())
print("You are taking", D.numCourses(), "courses")
print(D.fullName())

E = University("John Doe", 1155)
print(E.fullName())

F = Employee("Majid Maqbool", 567, 5000, "Dr")
print(F.fullName())


# 22. Inheritance - Polygon and Triangle Calculator
# Polygon Class - Base Class for Polygons
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + ": ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])

# Triangle Class - Subclass of Polygon
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)

# Main code
# Create a Triangle object (t)
t = Triangle()

# Input the side lengths of the triangle
t.inputSides()

# Display the entered side lengths of the triangle
t.dispSides()

# Calculate and print the area of the triangle
t.findArea()
