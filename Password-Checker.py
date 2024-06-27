
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
    lowerAndCap = False 
    number = True

    for character in userPasswordList:
        if character.islower():
            if character.islower():
                lowerAndCap = True
            else:
                lowerAndCap = lowerAndCap
        else:
            lowerAndCap = lowerAndCap
    
    for character in userPasswordList:
        if character.isnumeric:
            number = True
        else:
            number = number
   
    if 8 > len(userPasswordList) < 15:
        print("Rejected!")
    else:
        if lowerAndCap == True:
            if number = True:
                #NEEDS COMPLETION 
        else:
            print("Rejected")
            
    


