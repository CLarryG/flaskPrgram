import random
import time
import os

def get_user_input(prompt):
    """ Prompts the user with the given prompt and waits for input. Args: prompt (str): The message to display to the user. """
    input(prompt)

def main():
    """ Main function to measure the user's perception of time. Generates a random time between 1 and 10 seconds, prompts the user to start and stop the timer, calculates the elapsed time, and records the actual and guessed times in 'data.txt'. """
    # Generate a random time between 1 and 10 seconds
    actual_time = random.randint(1, 10)
    print(f"Try to guess when {actual_time} seconds have passed.")
    
    # Ask user to press a key to start
    get_user_input("Press Enter to start...")
    
    # Start the timer
    start_time = time.time()
    
    # Ask user to press a key to stop
    get_user_input("Press Enter to stop...")
    
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    
    # Record the result
    with open("data.txt", "a") as file:
        file.write(f"{actual_time} {elapsed_time:.2f}\n")
    
    print(f"Actual time: {actual_time} seconds")
    print(f"Your guess: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()