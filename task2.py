#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5  # Adjust this value as needed

    print("Welcome to the Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number ({secret_number}) correctly in {attempts + 1} attempts.")
            break

        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()


# In[ ]:




