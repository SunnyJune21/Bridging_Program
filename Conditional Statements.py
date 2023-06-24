# 1. Age comparison
nameA = input("Enter the first person's name ")
ageA = input("Enter the first person's age ")

nameB = input("Enter the second person's name ")
ageB = input("Enter the second person's age ")

if ageA > ageB:
  print(nameA, "is", int(ageA) - int(ageB), "years older than", nameB)
else:
  print(nameB, "is", int(ageB) - int(ageA), "years older than", nameA)


# 2. Number comparison
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
  print(num1, "is bigger")
elif num1 < num2:
  print(num2, "is bigger")
else:
  print(num1, "and", num2, "are equal")


# 3. Check if a number is odd or even
a = float(input("Please enter a number: "))
if a%2 != 0:
  print(a, "is an odd number")
else:
  print(a, "is an even number")


# 4. Find out even numbers
a = float(input("Please input the 1st number: "))
b = float(input("Please input the 2nd number: "))
c = float(input("Please input the 3rd number: "))
d = float(input("Please input the 4th number: "))
e = float(input("Please input the 5th number: "))

thelist = [a, b, c, d, e]

for x in thelist:
  if x%2 == 0:
    print(x, "is an even number")
  else:
    continue


# 5. Counting vowels in a word
word = input("Enter a word: ")
vowelCount = 0
lowerCase = word.lower()

if "a" in lowerCase or "e" in lowerCase or "i" in lowerCase or "o" in lowerCase or "u" in lowerCase:
    vowelCount = lowerCase.count("a") + lowerCase.count("e") + lowerCase.count("i") + lowerCase.count("o") + lowerCase.count("u")
    print("There are", vowelCount, "vowels in", word)
else:
    print("There are no vowels in", word)


# 6. Add, subtract, multiply or divide calculator
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

operation = input("Enter a choice of calculation (add, subtract, multiply or divide): ")

if operation == "add":
  result = x + y
elif operation == "subtract":
  result = x - y
elif operation == "multiply":
  result = x * y
elif operation == "divide":
  result = x/y
  mod = x%y
  div = x//y
  print(div, "remainder", mod)
else:
  print("Error, that was not an option")
print("When we", operation, x, "and", y, "we get", result)


# 7. Grading
x=float(input("Enter the result: "))
if x in range(80, 101):
  print("Your grade is A")
elif x in range(70, 80):
  print("Your grade is B")
elif x in range(60, 70):
  print("Your grade is C")
elif x in range(50, 60):
  print("Your grade is D")
elif x in range(0, 50):
  print("Your grade is F")
else:
  print("Invalid result")


# 8. Rock-Paper-Scissors game:
import random

user_input = input("Enter a choice (rock, paper, scissors): ")
choices = ["rock", "paper", "scissors"]
computer_input = (random.choice(choices))
print(f"You chose, {user_input.lower()}, and the computer chose {computer_input}")

if user_input.lower() == computer_input:
  print("It's a tie!")
elif user_input.lower() == "rock":
  if computer_input == "scissors":
    print("Rock smashes scissors. You win!")
  else:
    print("Paper covers rock. You lose >.<")
elif user_input.lower() == "paper":
  if computer_input == "rock":
    print("Paper covers rock. You win!")
  else:
    print("Scissors cut paper. You lose >.<")
elif user_input.lower() == "scissors":
  if computer_input == "paper":
    print("Scissors cut paper. You win!")
  else:
    print("Rock smashes scissors. You lose >.<")
else:
  print("Error, that was not an option")
  

# 9. Hangman game
guess = input("Guess a letter in A_ _L_ _")
guess = guess.upper()
gletters = " "
if guess in "PES":
  print("Yes,", guess, "is in the word! Two more letters to guess.")
else:
  print(guess, "is not in the word. You have two tries left")

guess = input("Guess a letter in A_ _L_ _")
guess = guess.upper()
if guess in "PES":
  if guess not in gletters:
    print("Yes,", guess, "is in the word! One more letter to guess.")
    gletters += guess
  else:
    print("You already guessed this letter. One guess left")
else:
  print(guess, "is not in the word. You have one try left")

guess = input("Guess a letter in A_ _L_ _")
guess = guess.upper()
if guess in 'PES':
  if guess not in gletters:
    print("Yes,",guess,"is in the word!")
    gletters += guess
  else:
    print("You already guessed this letter.")
else:
  print(guess,"is not in the word. You have no guesses left")

print("The word was APPLES!")


# 10. Word guessing game
word = "sweet"
print("Guess the missing word.\nHow _____ are the apples?")
print("*************************************************************")

numbers = ["first", "second", "third"]

for i in range(3):
    print("Enter your", numbers[i], "guess:")
    guess = input()
    
    if guess == word:
        print("Wow! That is correct!")
        break
    else:
        print("Please try again :(")

if guess != word:
    print("Better luck next time! The word was", word)
