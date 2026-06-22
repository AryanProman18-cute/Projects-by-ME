import random

def play():
    # Map abbreviations to full words for cleaner display
    game_elements = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    # Define winning rules: Key beats Value
    winning_rules = {'R': 'S', 'P': 'R', 'S': 'P'}
    
    # Standardize input to uppercase
    user_choice = input("Choose (R)ock, (P)aper, or (S)cissors: ").upper()
    
    # Validate input immediately
    if user_choice not in game_elements:
        print("Invalid choice. Please select R, P, or S.")
        return

    computer_choice = random.choice(list(game_elements.keys()))
    print(f"Computer chose: {game_elements[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif winning_rules[user_choice] == computer_choice:
        print("You won!")
    else:
        print("You lost!")

if __name__ == "__main__":
    play()

