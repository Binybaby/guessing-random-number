# Biny Baby, 2018-02-18
# guessing game
# https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
from random import randint

Target = randint(0, 100)
Guess =7
print("Guess a number between 1 and 100")
while Target != Guess:
   Guess = int(input("Enter a number: "))
   if Guess == Target:
       print("Well Done")
   elif Guess < Target:
        print("Too Low")
   else:
        print("Too High")
