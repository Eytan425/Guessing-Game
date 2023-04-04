import os
import json
tries = 0

# Load existing data from the JSON file if it exists and is not empty
if os.path.exists("users.json") and os.stat("users.json").st_size != 0:
    with open("users.json", "r") as f:
        data = json.load(f)
else:
    data = {}

# Function to check if username is available
def is_username_available(username):
    for key in data:
        if key == username:
            return False
    return True

# Get input from the user
user_type = input("Are you a new user? (y/n): ")


                

if user_type == "y":
    while True:
        username = input("Enter a username: ")
        email = input("Enter your email: ")
        if not is_username_available(username):
            print("The username is already taken. Please enter a new username.")
            continue
        password = input("Enter a password: ")
        confirm_password = input("Enter your password again: ")
        
        # Check if the username is already taken
        
        
        if password == confirm_password:
            break
        else:
            print("Passwords do not match, please try again.")
    
    security = input("What is your grandmas name? ")

    coins = 100
    data[username] = {"Password": password, "Coins": coins, "Security Question": security, "Email": email}

    with open("users.json", "w") as f:
        json.dump(data, f)
    print("Congratulations! Your account has been created with {} coins".format(coins))



elif user_type == "n":
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in data and data[username]["Password"] == password:
            print("Welcome back, {}! You have {} coins".format(username, data[username]["Coins"]))
            break
        else:
            print("Username or password incorrect, please try again.")
            tries += 1
            
            if (tries == 5):
                forget = input("Have you forgotten your password? (y/n): ")
                if(forget.lower() == "y"):
                    security1 = input("What is your grandmas name? ")
                        
                    if username in data and data[username]["Security Question"] == security1:
                        print("Welcome back, {}! You have {} coins".format(username, data[username]["Coins"]))
                        break
                    else:
                        print("Wrong, restart the game and sign in again.")
                        break
else:
    print("Invalid input. Please enter 'y' or 'n'.")                        


def find_coins_for_username(username):
    # Load the current data from the JSON file
    with open("users.json", "r") as f:
        data = json.load(f)

    # Find the user and return their coin balance
    if username in data:
        return data[username]["Coins"]
    else:
        return None

def update_coins_for_username(user):
    # Load the current data from the JSON file
    with open("users.json", "r") as f:
        data = json.load(f)

    # Find the user and update their coin balance
    for username in data:
        if username == user["user"]:
            data[username]["Coins"] = user["Coins"]
            break

    # Write the updated data back to the JSON file
    with open("users.json", "w") as f:
        json.dump(data, f)       