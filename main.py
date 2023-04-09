print("Hello and welcome to the number guessing game!!")
print("Made By: Eytan Benittah")
import sign_in_sign_up
from sign_in_sign_up import find_coins_for_username
from sign_in_sign_up import username
import random

def load_hints(number):
    # Create a list of hints
    hints = [
        f"The number is between 1 and {number}",
        f"The number is between {number} and 100",
        "The number is even" if number % 2 == 0 else "The number is odd",
        "The number is a multiple of 3" if number % 3 == 0 else "The number is not a multiple of 3",
        "The number is a multiple of 5" if number % 5 == 0 else "The number is not a multiple of 5",
        "The number is a prime number" if all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)) else "The number is not a prime number"
    ]
    
    return hints

def play_game(coins):
    lives = 3
    number = random.randint(1, 100)
    print(number)
    hints = load_hints(number)
    print(f"You have {coins} coins and {lives} lives. Guess the number between 1 and 100.")
    
    while lives > 0:
        
        guess = input("Guess: ")
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        guess = int(guess)
        if guess == number:
            print("You guessed it! Congratulations, you won 100 coins.")
            coins += 100
            if play_again():
                number = random.randint(1, 100)
                hints = load_hints(number)
                lives = 3
                print("A new number has been generated.")
                continue
            else:
                update_user_balance(coins)
                print(f"Thanks for playing! You finished with {coins} coins.")
                return
        else:
            lives -= 1
            print(f"Wrong. You have {lives} lives left.")
            if lives > 0:
                hint = input("Do you want a hint? (costs 10 coins) [y/n] ")
                if hint.lower() == 'y':
                    if coins >= 10:
                        coins -= 10
                        print(f"You have {coins} coins left")
                        print(hints.pop(0))
                    else:
                        print("You don't have enough coins for a hint.")
            else:
                print(f"Game over. The number was {number}.")
                # Deduct 20 coins from the user's balance for losing the game
                coins -= 20
                if play_again():
                    number = random.randint(1, 100)
                    hints = load_hints(number)
                    lives = 3
                    print("A new number has been generated.")
                    continue
                else:
                    update_user_balance(coins)
                    print(f"Thanks for playing! You finished with {coins} coins.")
                    return
        
    update_user_balance(coins)
    print(f"Thanks for playing! You finished with {coins} coins.")


def update_user_balance(updated_coins):
    user = {"user": username, "coins": updated_coins}
    sign_in_sign_up.update_coins_for_username(user)
    print(f"Balance of user {username} updated to {updated_coins} coins.")


def play_again():
    while True:
        choice = input("Do you want to play again? [y/n] ")
        if choice.lower() == 'y':      
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


coins = find_coins_for_username(username)
play_game(coins)