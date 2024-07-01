
isPasswordwordAccepted = False

while isPasswordwordAccepted == False:
#    userPassword = input("Enter your password... ")
    

#    if userPassword.find("z") != -1:
#        print("True")
#        if userPassword[-1] == "!" :
#            print("True")
#            if userPassword[0].isupper():
#                print("Accept.")
#                isPasswordwordAccepted = True
#            else:
#                print("Reject!")
#        else:
#            print("Reject!")
#    else:
#        print("Reject!")
   

    userPassword = input("Enter your password... ")
    userPasswordList = list(userPassword)
    hasLower = False 
    hasUpper = False
    number = False
    hasSymbol = False

    print(userPassword)

    for character in userPassword:
        if character.islower():
            hasLower = True
        else:
            hasLower = hasLower
    

    for character in userPassword:
        if character.isupper():
            hasUpper = True
        else: 
            hasUpper = hasUpper
      
    for character in userPassword:
        if character.isnumeric():
            number = True
        else:
            number = number

    for character in userPassword:
        if character.isalnum():
            hasSymbol = hasSymbol
        else:
            hasSymbol = True
            
   
    if 8 > len(userPasswordList) < 15:
        print("Rejected!")    
    else:
        if hasLower == True and hasUpper == True:
            if number == True:
                if hasSymbol == True:
                    print("Accepted")
                else:
                    print("Rejected!")
            else:
                print("Rejected!")
        else:
            print("Rejected!")
            
    


