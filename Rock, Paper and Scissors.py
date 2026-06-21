import random
def play():
  choice=str(input("What your choice among 'R' for rock, 'P' for paper, and 'S' for scicssor- "))
  computer=random.choice(['R', 'P', 'S']) 

  if choice == computer:
    print("It's a tie!")
  else:
    win(choice, computer)

def win(choice, opponent):
  if (choice == 'R' and opponent == 'S') or (choice == 'P' and opponent == 'R') or (choice == 'S' and opponent == 'P') :
    print("You Won!")
  else:
    print("You Lost!")
play()
