import random

def guess_max(x):
    guess = 0
    random_number=random.randint(1,x)
    print(f"Find something in between 1 and {x}")   
    
    while guess!=random_number:
      guess= int(input("Guess a number- "))
      if guess>random_number:
        print("Too High")
      elif guess<random_number:
        print("Too Low")
    print("You guessed it!!")
guess_max(100)
