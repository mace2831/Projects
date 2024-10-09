
import random

def main():
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty Type 'easy' or 'hard':").lower()
    guesses = 10

    if difficulty == 'easy':
        guesses = 10
    elif difficulty == 'hard':
        guesses = 5

    correctnum = random.randint(1, 100)

    while guesses > 0:
        print('You have ', guesses, 'attempts remaining to guess the number')
        guess = int(input('Make a guess'))

        if guess == correctnum:
            print('Dang you got it!')
            break
        elif guess > correctnum:
            print('Too high.')
            guesses -= 1
        else:
            print('Too low.')
            guesses -= 1





if __name__ == '__main__':
    main()