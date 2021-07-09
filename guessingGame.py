import random 

number = random.randint(1, 9)
chances = 5

while chances != 0 :
    guess = int(input('Try to guess the number: ') )
    chances= chances - 1

    if guess == number: 
        print('WOW! YOU WON!')
        break
    elif guess < number:
        print(number, ' is too low, try guessing something higher.')
    elif guess > number:
        print(number, ' is too high, try guessing something lower.')

if chances <= 0:
    print('YOU LOSE!! The number was ', number)

