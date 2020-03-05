# Create a game where the user has 10 tries to guess a number 1 - 100.
# Tell the user if guess is too high/low.

from random import randint


correct_number = randint(1, 100)
guesses = 10

while guesses > 0:
    while True:
        user_answer = (input('Guess a number between 1 and 100.  You have ' + str(guesses) + ' left. : '))
        if user_answer.isdigit():
            user_answer = int(user_answer)
            break
        else:
            print("Please enter a valid number!  That counts as a guess!")
            guesses -= 1

    guesses -= 1

    if user_answer == correct_number:
        if guesses == 9:
            print('You win! It only took you 1 guess!')
            exit()
        else:
            print('You win!  It took you ' + str(10 - guesses) + ' guesses!')
            exit()
    else:
        if user_answer > correct_number:
            print('Incorrect! Your guess is too high!')
        else:
            print('Incorrect! Your guess is too low!')

print('Out of guesses! You lose!')
exit()
