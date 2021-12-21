import random 

print("Welcome to the Number Guessing Game!!!!!!!!")

n = random.randint(1,9)

chances = 0

print("Guess a Number Between 1 and 9!!! ")

while chances<5 :
    
    guess = int(input("Enter Your Guess!!!!! "))

    if guess == n:
        print("Congrats! YOU GUESSED IT!!!!!")
        break

    elif guess < n:
        print("Your GUESS IS VERY LOW!!!!!!!!  Guess a higher number than ", guess)

    else:
        print("Your GUESS IS TOO HIGH!!!!!!!  Guess a lower number than ", guess)

    chances += 1


    if chances > 5:
        print("YOU DIDN'T GUESS IT LOSER!!!!! The answer was " , n)



