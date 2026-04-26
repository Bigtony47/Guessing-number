import random
def play_game():

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    print("Guess the number between 1 and 100.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt{attempts+1}: Enter your guess: "))
            attempts += 1
        
            if guess == secret_number:
                print(f"Correct! You guessed it in {attempts} attempts ")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")

    if attempts == max_attempts and guess != secret_number:
        print(f"Out of attempts! The number was {secret_number}.")

play_game()