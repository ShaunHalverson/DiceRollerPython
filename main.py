import random

print("Welcome to the World's greatest dice roller")
print("-------------------------------------------")

print("How many dice would you like to roll?")
### Validate input
while True:
  try:
    numberPicked = int(input("Type an integer between 1 and 10: "))
    if(numberPicked > 0 and numberPicked < 10):
      break
    else:
      print("Invalid input. Try again.")
  except:
    print("Please provide an integer")

def rollDice(amountOfDice):
  totalSum = 0
  possibleFaces = [1,2,3,4,5,6]
  for die in range(amountOfDice):
    roll = random.choice(possibleFaces)
    print("Die ", die + 1, ": ", roll)
    totalSum += roll
  average = totalSum / amountOfDice
  print("Total sum: ", totalSum)
  print("Average roll: ", average)


rollDice(numberPicked)
