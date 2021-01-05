#Guess the number game

import random

secretNumber = random.randint(1, 20)

for guessessTaken in range(1, 7):
    print('Take a guess time ' + str(guessessTaken))
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good Job you guessed secret Number in ' + str(guessessTaken) + ' guesses!')
else:
    print('Nope. secret Number is ' + str(secretNumber))


