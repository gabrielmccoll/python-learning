def guessing_game():
  import random
  number = random.randint(10,30)
  guess = 0
  while guess != number:
    guess = int(input("gies a number between 10-30, meatbag  "))
    if guess == number:
        print("just right"")
    if guess > number:
        print("too high")
    if guess < number:
        print("too low")

guessing_game()