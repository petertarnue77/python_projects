# Register
# -- firstName, lastName, password, email
# --generate user account

# login 
# -- account number & passowrd 

# BANK OPERATIONS


# INITIALIZING 
import random
import validation  
import bankOps
import database 
from getpass import getpass

def init():
    print("Welcome to BankPython")
    haveAccount = int(input("Do you have an account with us?: 1 (yes) 2 (No) \n"))
    if (haveAccount == 1): 
        login() 
    elif (haveAccount == 2):
        print(register())
    else:
        print("You have selected an invalid option. Please try again")
        init()


def login():
    print("******LOGIN********") 

    accountNUmberFromUser = input("What is your account number: \n")

    # validate account number
    isValidAccountNumber = validation.accountNumberValidation(accountNUmberFromUser) 
    try:
        if isValidAccountNumber:
            password = getpass("What is your password: \n")
            user = database.autheticated_user(accountNUmberFromUser, password) 
            if user:
                bankOps.bankOperation(user)
            print("Invalid Account or password: ")
            login()
    except Exception as e:
        print(e, "Please check properly")
    else:
        print('Account Number Invalid. Check that you have upto 10 degits and only integer')
        init() 


def register():
    print("********* REGISTER ACCOUNT ********")
    # user information
    email = input("What is your email address: \n")
    firstName = input("What is your first name: \n") 
    lastName = input("What is your last name: \n") 

    password = getpass("Create a password for yourself: \n")  

    # generate account number for user
    accountNumber = generateAccountNumber() 
    
    prepareUserDetails = firstName + ',' + lastName +','+ email + ',' + password, str(0)

    isUserCreated = database.create_record(accountNumber, prepareUserDetails) 
    if isUserCreated:
        print("Your Account has been Created")
        print(" ====== ==== ==== ==== ")
        print("your Account Number is: %d" % accountNumber)
        print("Make sure you keep it safe") 
        print(" ==== ==== ==== ==== ==== ")

        login()
    else:
        print("Something went wrong") 
        register()

def logout():
    bankOps.login()


def generateAccountNumber():
    accountNumber = random.randrange(1111111111, 9999999999) 
    return accountNumber 


def accountBalance(userDetails):
    return userDetails[0]
 
#=======ACTUAL BANKING SYSTEM========
init()