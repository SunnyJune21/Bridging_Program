# 1. Print all letters except e and o
i = 0
word = "Hello"

while i < len(word):
  if word[i] == "e" or word[i] == "o":
    i += 1        # Skip the current letter if it is 'e' or 'o'
    continue
  print(word[i])  # Print the current letter
  i += 1


# 2.1. Remove all occurrences of item 20 using a for loop
list1 = [5, 20, 15, 20, 25, 50, 20]
newlist = []

for x in list1:
  if x != 20:
    newlist.append(x)

print(newlist)


# 2.2. Remove all occurrences of item 20 using a list comprehension
list1 = [5, 20, 15, 20, 25, 50, 20]
newlist = [x for x in list1 if x != 20]
print(newlist)


# 3. Calculate the sum and average of 5 numbers using a while loop
sum = 0
count = 0

while count < 5:
  count += 1
  number = float(input("Enter a number: "))
  sum += number

average = sum / count

print("The average of the given numbers is", average)
print("The sum of the given numbers is", sum)


# 4. Running total until user input 0
sum = 0
user_input = float(input("Enter a number: "))

while user_input != 0:
  sum += user_input
  print("So far, the sum is", sum)
  user_input = float(input("Enter a number or 0 to end: "))

print("The end. The final sum is", sum)


# 5. Number guessing game
import random

number = random.randint(0, 10)

guess = int(input("I am thinking of a number between 0 and 10. Guess what it is: "))
while guess != number:
    guess = int(input("Wrong! Guess again: "))

print(f"That's correct! It was {number}")


# 6. Number guessing game with a limit of 5 tries
import random

number = random.randint(0, 10)
guess = int(input("I am thinking of a number between 0 and 10. Guess what it is: "))
tries = 4

while tries >= 0:
    if guess == number:
        print("That's correct!")
        break
    else:
        tries -= 1
        print(f"Wrong! You have {tries} guess(es) left")
        if tries == 0:
            print(f"Better luck next time! It was {number}")
        else:
            guess = int(input("Guess again: "))


# 7. Number guessing game with tips
import random
number = random.randint(0, 10)

guess = int(input("I am thinking of a number between 0 and 10. Guess what it is: "))
while guess != number:
    if guess > number:
        guess = int(input(f"The number is lower than {guess}! Guess again: "))
    elif guess < number:
        guess = int(input(f"The number is higher than {guess}! Guess again: "))

print("That's correct! It was", number)


# 8. Word guessing game
word = "APPLES"
print("Guess the word with", len(word), "letters")
print("_ " * len(word))

tries = 3
correct_letters = set()

while tries > 0 and correct_letters != set(word):
  guess = input("Guess a letter: ")
  guess = guess.upper()

  if guess in word:
    print("Well done. ", guess, " is in the word.")
    correct_letters.add(guess)
  else:
    tries -= 1
    print(guess, "is not in the word. You have", tries, "guesses left.")
    if tries == 0:
      print("Looks like you lost. The word was", word)

if correct_letters == set(word):
  print("Well done! You have guessed it correctly. The word is", word)
else:
  print("You guessed", len(correct_letters), "letters.")


# 9. Project Point of Sale application
total = 0
sum = 0
kb = 9
mp = 7
hdmi = 20

print('*********PyShop Bill*********\n1. Gaming Keyboard................$9\n2. Mouse Pad......................$7\n3. HDMI cable.....................$20\n******************************')
userinput = int(input('Enter item number or enter 0 to total: '))

while userinput not in range(1, 4) and user_input != 0:
    userinput = int(input('Invalid entry. Enter a valid item number: '))

while userinput != 0:
    if userinput == 1:
        sum += kb
    elif userinput == 2:
        sum += mp
    elif userinput == 3:
        sum += hdmi
    userinput = int(input('Enter item number or enter 0 to total: '))

total = sum
print('The total is: $', total)


# 10. Mini bar - ordering drinks from bar menu
print("""*****Coco Bar Menu*****
1. Hot Chocolate
2. Latte
3. Chai
**********************""")
user_input = int(input("Please select a drink from the menu: "))

while user_input != 1 and user_input != 2 and user_input != 3:
  user_input = int(input("Invalid entry. Please select another option: "))

if user_input == 1:
  print("**Hot Chocolate ingredients are: Cocoa powder, sugar, chocolate, and milk")
elif user_input == 2:
  print("**Latte ingredients are: Chocolate, hot espresso shots, and steamed milk")
elif user_input == 3:
  print("**Chai ingredients are: Milk, tea, and spices")


# 11. Password checker
while True:
    pw = input("Enter a password: ")

    validations = []

    if not any(char.isalpha() for char in pw):
        validations.append("The password needs to have letters")

    if not any(char.isdigit() for char in pw):
        validations.append("The password needs to have numbers")

    if not any(char.isupper() for char in pw) or not any(char.islower() for char in pw):
        validations.append("The password needs to have both uppercase and lowercase letters")

    if any(not char.isalnum() for char in pw):
        validations.append("The password cannot have special characters")

    if len(pw) <= 7:
        validations.append("The password has to have more than 7 characters")

    if pw[0].isdigit():
        validations.append("The password cannot start with a digit")

    if not validations:
        print("The password is valid")
        break
    else:
        print("Invalid password. Please try again.")
        for validation in validations:
            print(validation)
