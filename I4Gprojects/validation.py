def accountNumberValidation(accountNumber):
    # Check if account number is not empty 
    if accountNumber:
        # check if account number is 10 digits
        try:
            int(accountNumber) 
            if len(str(accountNumber)) == 10: 
                return True  
        except ValueError:
            return False
        except TypeError:
            return False
    return True

