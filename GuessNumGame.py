#importing the random module
import random
#generate a random number between 1 to 10
secret_number = random.randint(1, 10)
#maximum  attempts allowed
max_attempts = 3
# function to display a welcome message
def welcome_message():
    print("\nWelcome to the number guessing game!")
    print(f"You have {max_attempts} attempts to guess the correct number.")

def guess_recursive(attempts_left):
    guess = int(input("\n Guess the number(between 1 and 10):"))
    if guess == secret_number:
        print("Congratulations! you guessed the correct number!")
    else:
        print(f"wrong guess. attempts left : {attempts_left-1}")
        if attempts_left>1:
            guess_recursive(attempts_left-1)
        else:
            print(f"\n Sorry you cannot guess the number. The correct number was {secret_number}.")

welcome_message()
guess_recursive(max_attempts)
print(f"meomory adress of Secret number {secret_number} is : {id(secret_number)}")