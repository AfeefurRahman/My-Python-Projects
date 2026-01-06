import math 
import random 

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < randomNumber:
            print("Your guess is less than the number I am expecting. Please try again.")
        elif guess > randomNumber:
            print("Your guess is too high than the number that I am expecting. Please try again.")
    print(f"You have figured out the number! Congratulations! The number is {randomNumber}")
        
def computerGuess(y):
    lowBound = 1
    highBound = y
    feedback = ''
    count = 0
    while feedback != "correct":
        guess = random.randint(lowBound,highBound)
        feedback = input(f"Is my guess: {guess}, high, low or correct? (type in all lowercase):")
        if feedback == "high":
            highBound = guess - 1
        elif feedback == "low":
            lowBound = guess + 1 
        count += 1
    print(f"I have figured out your secret number which is {guess}. Congratulations! And you too {count} tries!")

computerGuess(100000000)
