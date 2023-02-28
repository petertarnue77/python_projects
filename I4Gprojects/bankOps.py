import auth
import database

# BANK OPERATION
def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1])) 

    selectedOption = int(input("What Wound you like to do 1(withdrawal) 2(deposit) 3(logout) 4(Exit): \n"))
    if (selectedOption == 1):
        # perform deposit operation
        depositOperation()

    elif (selectedOption == 2):
        withdrawalOperation() 

    elif (selectedOption == 3):
        auth.logout()

    elif (selectedOption == 4):
        exit()
    else:
        print("Invalid Option Selected")
        bank_operation(user)


def withdrawalOperation():
    # get current balance
    currentBalance = database.accountBalance()
    # get amount to withdral 
    withdrawalAmount = int(input("How much do you want to withdral: \n"))
    # check if current balance > withdral amount 
    if withdrawalAmount > currentBalance: 
        if withdrawalAmount > 10:
            # deduct withdrawal amount from current balance
            transact = currentBalance - withdrawalAmount
            # display current balance
            return transact
    return False

def depositOperation():
    print("deposit operation") 
    # get current balance
    balance = database.accountBalance()
    # get amount to deposit
    depositAmout = int(input("How much do you want to deposit: \n"))
    # add deposited amount to current balance 
    tota_balance = balance + depositAmout 
    # display current balance 
    return tota_balance

def complaint():
    print("complaint") 

