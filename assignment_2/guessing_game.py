import random

random_number = random.randint(1, 20)

# Default try set to 1 in case guessed on first try. 
incorrect_guesses = 1
user_number = 0
while user_number == 0:
    try:
        user_number += int(input("Enter a number between 1 and 20: "))
        if random_number == user_number:
            print(f"Random number guessed correctly after {incorrect_guesses} attempt(s)!")
        elif incorrect_guesses <=11:
            print("Sorry, try again.")
            user_number = 0
            incorrect_guesses += 1
        else:
            print(f"Sorry, you've reached the guess limit! The number was {random_number}!")

    except:
        print("Please enter a number.")