import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

answer = random.randint(1,100)

def attempts(remaining):
    guess = 0
    
    while guess != answer and remaining > 0:
        guess = int(input("Make a guess: "))
        if guess > answer:
            remaining -= 1
            if remaining == 0:
                print("You've run out of guesses. Refresh the page to run again.")
            else: 
                print(f"Too high. Guess again. You have {remaining} attempts remaining to guess the number.")
        elif guess < answer:
            remaining -= 1
            if remaining == 0:
                print("You've run out of guesses. Refresh the page to run again.")
            else:
                print(f"Too low. Guess again. You have {remaining} attempts remaining to guess the number.")
        elif guess == answer:
            print("You got it!!!")
         
        
    
if difficulty_level == 'easy':
    remaining = 10
    attempts(remaining)

elif difficulty_level == 'hard':
    remaining = 5
    attempts(remaining)


