import random

score = ["leaderboard"]

def game():
    print('')
    difficulty = (input("Please choose a difficultly 1,2 or 3: "))

    if difficulty == '1':
        maxNumber = 10
    elif difficulty == '2':
        maxNumber = 20
    elif difficulty == '3':
        maxNumber = 30

    number = random.randint(1, maxNumber)
    lives = 6

    myName = input ("what is your name? ")
    print(f"Well, {myName}, I am thinking of a number between 1 and {str(maxNumber)}")

    for guessTaken in range(lives):
        print(f"You have {str(lives - guessTaken)} guesses left.")
        guess = input("Take a guess: ")
        guess = int(guess)

        if guess == number:
            print("Good job you won!")
            break
        elif guess < number:
            print("Your guess is too small!")
        elif guess > number:
            print("You're guess is too high")
        elif guess > maxNumber:
            print("You did not read the max number")

    if guess != number:
        number = str(number)
        print(f"Nope. That number is not what I was thinking of. I was thinking of: {number}")
        game_over(myName)
    elif guess == number:
        print("you guessed correct")
        game_over(myName)

def game_over(myName):
    replay = input("Do you wan't to play again? Y/N: ")
    if replay == "y" or replay == "Y":
        game()
    elif replay == "n" or replay == "N":
        print(f"thank you for playing {myName}")
    else:
        print("Invalid input")
        game_over()
game()
