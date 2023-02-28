

# take user input
def guessing_number(user_guess):
    # store the number to guess
    over_favorate_num = 10
    if type(user_guess) == str:
        user_guess = int(user_guess) 

    if user_guess == over_favorate_num:
        print("Congrat. You guess our wining number " + str(over_favorate_num))
    elif user_guess < over_favorate_num:
        print("Hmmm.... Your gues is too low. Please try again") 
    elif user_guess > over_favorate_num:
        print("Hmmm..... your guess is too high. Please try again") 

print("Thank you")
guessing_number(12)


    