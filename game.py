# Put your code here
import random
#greet player
#get player name
#choose random number between 1 and 100
#repeat forever:
    #get guess
    #if guess is incorrect:
        #give hint
        #increase number of guesses
    #congratulate player

def guessing_game():
    print("Howdy, Whats your name?")
    name = input("(Type in your name) ")
    print(f"{name}, I'm thinking of a number between 1 - 100.")
    num = random.randint(1,100)
    print("Try to guess my number")
    count_tries=0
    while True:
        number_guess = input("Your guess? ")
        if number_guess.isnumeric() == False:
            print("Your guess has to be a number.")
        elif number_guess.isnumeric() == True:
            number_guess = int(number_guess)
            if number_guess not in range(1,100):
                print("Enter a valid number")
            elif num != number_guess:
                count_tries += 1
                if num > number_guess:
                    print("Your guess is too low, try again.")
                elif num < number_guess:
                    print("Your guess is too high, try again.")
            elif num == number_guess:
                print(f"Well done, {name}. You found my number in {count_tries} tries!")
                break
guessing_game()
