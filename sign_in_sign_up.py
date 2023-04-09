import os
import json
tries = 0
coins = 0

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


# question1 = input("Where were you born? ")
# question2 = input("What is your grandmas name? ")
# question3 = input("What is your highschool called: ")

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
    
    # security = input("What is your grandmas name? ")

    print("1. Where were you born?")
    print("2. What is your grandmas name?")
    print("3. What is your highschool called? ")
    choice = input("What question would you like to answer? (1/2/3/4) ")
    if choice in ('1' , '2',  '3' , '4'): 
        if choice == '1':
            question1 = input("Where were you born? ")
            coins = 100
            data[username] = {"Password": password, "Coins": coins, "Security Question": question1, "Email": email}
        elif choice == '2':
            question2 = input("What is your grandmas name? ")
            coins = 100
            data[username] = {"Password": password, "Coins": coins, "Security Question": question2, "Email": email}
        elif choice == '3':
             question3 = input("What is your highschool called: ")
             coins = 100
             data[username] = {"Password": password, "Coins": coins, "Security Question": question3, "Email": email}
    else:
        print("Wrong Input!")
    # coins = 100
    # data[username] = {"Password": password, "Coins": coins, "Security Question": security, "Email": email}

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