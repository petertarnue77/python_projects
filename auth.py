# Register
# -- firstName, lastName, password, email
# --generate user account

# login 
# -- account number & passowrd 

# BANK OPERATIONS


# INITIALIZING 
import random

database = {

}  

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
    accountNUmberFromUser = int(input("What is your account number: \n"))
    password = input("What is your password: \n") 

    for accountNumber, UserDetials in database.items():
        if(accountNumber == accountNUmberFromUser):
            if(UserDetials[3] == password):
                bankOperation(UserDetials)
    
    print("Invalid Account or password: ")
    login()

def register():
    print("********* REGISTER ACCOUNT ********")
    # user information
    email = input("What is your email address: \n")
    firstName = input("What is your first name: \n")
    lastName = input("What is your last name: \n") 
    password = input("Create a password for yourself: \n")  

    # generate account number for user
    accountNumber = generateAccountNumber() 

    # stored user account details in database
    database[accountNumber] = [email, firstName, lastName, password] 

    print("Your Account has been Created")
    print(" ====== ==== ==== ==== ")
    print("your Account Number is: %d" % accountNumber)
    print("Make sure you keep it safe") 
    print(" ==== ==== ==== ==== ==== ")

    login()


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1])) 

    selectedOption = int(input("What Wound You Like To Do? (1)Deposit (2)Withdrawal (3)Logout (4)Exit: \n"))

    if (selectedOption == 1):
        depositOperation()

    elif (selectedOption == 2):
        withdrawalOperation() 

    elif (selectedOption == 3):
        logout()

    elif (selectedOption == 4):
        exit()
    else:
        print("Invalid Option Selected")
        bankOperation(user)


def withdrawalOperation():
    print("withdrawal operation") 

def depositOperation():
    print("deposit operation") 

def complaint():
    print("complaint") 

def logout():
    login()

def generateAccountNumber():
    accountNumber = random.randrange(1111111111, 9999999999) 
    return accountNumber 

    



#=======ACTUAL BANKING SYSTEM========
init()