#CRUD OPERATIONs
# create records 
# read records
# update records
# delete records  

import os 
import validation

userDbPath = "data/userRecord/"


def create_record(accountNumber, firstName, lastName, email, password): 
    completionState = False
    userData = firstName + ',' + lastName +','+ email + ',' + password + "," +str(0) 
    if doesAccountNumberExist(accountNumber):
        print("Account Already Exist")
        return False
    if does_email_exist(email):
        print("User Already Exist")
        return False
    completionState = False
    try:
        # name of text file would be accountNumber.txt
        file = open(userDbPath + str(accountNumber)+".txt", "x")
    except FileExistsError:
        doesFileContainData = file = read_record(userDbPath + str(accountNumber)+".txt", "x")
        if not doesFileContainData:
            delete_record(accountNumber)
    else:
         # add the user details to the file 
        file.write(str(userData))
        completionState = True
    finally:
        file.close() 
        return completionState 

def read_record(userAccountNumber): 
    isValidAccountNumber = validation.accountNumberValidation(userAccountNumber)
    try:
        if isValidAccountNumber:
            # find the user with account number
            file = open(userDbPath + str(userAccountNumber)+'.txt', 'r')
        else:
            file = open(userDbPath + str(userAccountNumber),'r')

    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't Exist")
    except TypeError:
        print("Invalid Account Number format")
    else:
        # read the content of the file
        return file.read()
    return False
    
def update_record(userAccountNumber):
    print("update user record")
    # find user with accoun number
    # fetch the content of the file
    # update the content of the file
    # save the file 
    # return True

def delete_record(userAccountNumber):
    # find the user with account number
    isDeleteSuccessful = False
    if os.path.exists(userDbPath + str(userAccountNumber) + ".txt"):
        try:
            # delete user record (file)
            os.remove(userDbPath + str(userAccountNumber) + ".txt") 
            isDeleteSuccessful = True
        except FileNotFoundError:
            print("User not found") 
        finally:
            return isDeleteSuccessful 

def does_email_exist(email):
    # list of user from directory
    allusers = os.listdir(userDbPath) 
    for user in allusers: 
        user_list =str.split(read_record(user),",") 
        if email in user_list:
            return True 
    return False 

def doesAccountNumberExist(accountNumber):
    all_user = os.listdir(userDbPath)
    for user in all_user:
        if user == str(accountNumber) + ".txt":
            return True 
    return False

def autheticated_user(accountNumber, password): 
    if doesAccountNumberExist(accountNumber):
        user = str.split(read_record(accountNumber),',') 
        if password == user[3]:
            print(password)
            return user
    return False 


def accountBalance():
    # find the list of all user accounts
    all_user = os.listdir(userDbPath)
    # loop through all user account 
    for user in all_user:
        # read user account details
        read_me = str.split(read_record(user), ",")
        # return account number of user
        return int(read_me[4])
    # return false if account number not found
    return False


# print(autheticated_user(3843490151, "pass")) 
print(accountBalance())

print(doesAccountNumberExist(3843490151))

print(does_email_exist("develyn@gmail.com"))

