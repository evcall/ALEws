import random

def get_user_choice():
    """Get the user's choice."""
    print("\n1. Rock\n2. Paper\n3. Scissors")
    user_choice = int(input("Enter your choice: "))
    while user_choice not in [1, 2, 3]:
        print("Invalid choice. Please choose 1, 2, or 3.")
        user_choice = int(input("Enter your choice: "))
    return user_choice

def get_computer_choice():
    """Get the computer's choice."""
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    """Determine the winner."""
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play the game."""
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))
    
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

    print(f"Final score: You - {user_score}, Computer - {computer_score}")

play_game()

