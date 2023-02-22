#CRUD OPERATIONs
# create records 
# read records
# update records
# delete records  

import os 
import validation

userDbPath = "data/userRecord/"


def create_record(accountNumber, userDetails): 
    completionState = False
    try:
        # name of text file would be accountNumber.txt
        file = open(userDbPath + str(accountNumber)+".txt", "x")
    except FileExistsError:
        print("User already exit")
        # delete the already create file, and print out error, then return False 
        # check content of file before deleting
        #delete_record(accountNumber)
    else:
         # add the user details to the file 
        file.write(str(userDetails))
        completionState = True
    finally:
        file.close() 
        return completionState 

def read_record(userAccountNumber): 
    isValidAccountNumber = validation.accountNumberValidation(userAccountNumber)
    try:
        if isValidAccountNumber:
            # find the user with account number
            file = open(userDbPath + str(userAccountNumber)+".txt", "r")
        else:
            file = open(userDbPath + str(userAccountNumber),"r")

    except FileNotFoundError:
        print("User not found")
    except FileExistsError:
        print("User doesn't Exist")
    except TypeError:
        print("Invalid Account Number format")
    else:
        # read the content of the file
        return file.read()
    
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

def does_email_exist(userAccountNumber, email):
    # list of user
    allusers = os.listdir(userDbPath) 

    for user in allusers:
        print(read_record(user))
        print("\n")
    # find user record in the data folder 


# print(create_record(3521182386,['petertarue@gmail.com', 'Peter', 'Tarnue', 'passPeter', 0]))
#print(read_record(3521182386)) 
does_email_exist(3521182386, "petertarnue@gmail.com") 
#print(read_record({"one", "two"}))