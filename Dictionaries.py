# 1. Coffee Menu
coffee_menu = {
  'coffee': '$12',
  'tea': '$7',
  'iced coffee': '$13',
  'bagel': '$5',
  'hashbrown': '$2'
  }

for x, y in coffee_menu.items():
  print(x.title() + ": " + y.title())
print()

for x in coffee_menu.keys():
  print(x.title())
print()

for y in coffee_menu.values():
  print(y)


# 2. Polling for favorite programming languages
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  'laya': 'javascript',
  'josh': ' ',
  'david': ' ',
  'becca': ' '
  }

for x, y in favorite_languages.items():
  if y.strip():  # Check if the language value is not empty or just whitespace
    print(x.title() + ", thank you for taking the poll.")
  else:
    print(x.title() + ", what's your favorite programming language?")


# 3. Polling for favorite programming languages
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  'laya': 'javascript',
  }

coders = ["phil", "josh", "david", "becca", "sarah", "matt", "danielle"]

for x in coders:
  if x in favorite_languages.keys():
    print("Thank you for taking the poll, " + x.title() + "!")
  else:
    print(x.title() + ", what's your favorite programming language?")


# 4. Code to display the relationship between rivers and the countries they flow through
river_countries = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for x, y in river_countries.items():
  print("The " + x.title() + " flows through " + y.title() + ".")
print()

for x, y in sorted(river_countries.items()):
  print("The " + x.title() + " flows through " + y.title() + ".")


# 5. City information - Dictionaries within dictionaries
cities = {
    "toronto": {
      "city": "toronto",
      "country": "canada",
      "population": "7 milion",
      "fact": "Toronto is the 3rd largest city for English theatre in the world.",
      },
    "taipei": {
      "city": "taipei",
      "country": "taiwan",
      "population": "2.5 million",
      "fact": "The city is full of night markets",
      },
    "tokyo": {
      "city": "tokyo",
      "country": "japan",
      "population": "37 million",
      "fact": "Tokyo was called Edo for a very long time",
      },
    }

for x, y in cities.items():
  print("City: " + x.title())
  country = y["country"]
  population = y["population"]
  fact = y["fact"]
  print("\tCountry: " + x.title() + " is in " + country.title())
  print("\tPopulation: " + population)
  print("\tFun fact: " + fact)
  print()


# 6. Code to display user information - Dictionaries within dictionaries
users = {
    "aeinstein": {
      "first name": "albert",
      "last name": "einstein",
      "location": "princeton",
      },
    "mcurie": {
      "first name": "marie",
      "last name": "curie",
      "location": "paris",
      },
    }
for x, y in users.items():
  print("Username: " + x)
  full_name = y["first name"] + " " + y["last name"]
  location = y["location"]
  print("\tFull name: " + full_name.title())  # .title() method is used to capitalize the first letters of each word
  print("\tLocation: " + location.title())
  print()


# 7. Favorite places
favorite_places = {
    'ellision': ['new york', 'washington', 'new jersey'],
    'emma': ['tokyo', 'fukuoka', 'osaka'],
    'sophia': ['seoul', 'busan', 'jeju'],
    }

for x, y in favorite_places.items():
  print(x.title() + " likes the following places: ")
  for place in y:
    print("- " + place.title())
  print()


# 8. Favorite numbers
favorite_numbers = {
    "mandy": [42, 39, 56],
    "micah": [42, 17],
    "gus": [7, 12],
    "hank": [1000000, 100],
    "maggie": [0, 1],
    }

for x, y in favorite_numbers.items():
    print(x.title() + " likes the following numbers:")
    for number in y:
        print("- " + str(number))
    print()


# 9. Alien sightings
alien1 = {"name": "bantaf", "color": "green", "height": "7.19 meters"}
alien2 = {"name": "lemwin", "color": "gray", "height": "6.23 meters"}
alien3 = {"name": "jastyn", "color": "blue", "height": "7.12 meters"}

userinput = input("What color was the alien you spotted? ")

if userinput in alien1["color"]:
  print("Kid spotted", alien1["name"].title() + " - a friendly", alien1["color"], "alien!")
elif userinput in alien2["color"]:
  print("Kid spotted", alien2["name"].title() + " - a friendly", alien2["color"], "alien!")
elif userinput in alien3["color"]:
  print("Kid spotted", alien3["name"].title() + " - a friendly", alien3["color"], "alien!")

Aliens = [alien1, alien2, alien3]

print("\nAliens spotted!")
for alien in Aliens:  # Looping through the list of aliens
  print("\t-", alien["name"].title(), "is", alien["color"], "and is", alien["height"], "long.")


# 10. Pet information
Momo = {
  "name": "momo",
  "type": "dog",
  "owner": "Olivia",
  }
Tata = {
  "name": "tata",
  "type": "cat",
  "owner": "Wendy",
  }
Kiki = {
  "name": "kiki",
  "type": "rabbit",
  "owner": "Ella",
  }

pets = [Momo, Tata, Kiki]

for x in pets:
  print("Pet: " + x["name"].title())
  print(x["name"].title(), "is a", x["type"], "and the owner is", x["owner"] + ".")
  print()


# 11. Pet information
pets = []  # Create an empty list to store the pets in

# Create individual pets and store each one in the list
python = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(python)

chicken = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(chicken)

dog = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(dog)

print(pets) # Display the list of pets

# Display information about each pet
for p in pets:
    print("\nHere's what I know about " + p['name'].title() + ":")
    for key, value in p.items():
        print("\t" + key.title() + ": " + str(value).title())
