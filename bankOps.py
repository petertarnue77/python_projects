import auth
# BANK OPERATION
def bankOperation(user):
    print("Welcome %s %s" % (user[1], user[2])) 

    selectedOption = int(input("What Wound you like to do 1(withdrawal) 2(deposit) 3(logout) 4(Exit): \n"))
    if (selectedOption == 1):
        depositOperation()

    elif (selectedOption == 2):
        withdrawalOperation() 

    elif (selectedOption == 3):
        auth.logout()

    elif (selectedOption == 4):
        exit()
    else:
        print("Invalid Option Selected")
        bankOperation(user)


def withdrawalOperation():
    # get current balance
    # get amount to withdral
    # check if current balance > withdral amount
    # deduct withdrawal amount from current balance
    # display current balance
    pass

def depositOperation():
    print("deposit operation") 
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance 
    # display current balance

def complaint():
    print("complaint") 