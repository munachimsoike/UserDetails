
import string
import random



random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
container = {}
num = 1
str(num)


def user():
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    email = input("Enter email: ")
    combination = firstName[0:2] + lastName[0:2]
    conditon = True
    
    
    #Generate password
    def password_generator(val):
        return val + random 


    password = password_generator(combination)
    print("Your Password is: " + password)
    details = [firstName,lastName,email,password]
    
    
    #Checking for password
    def check_password(password):
        if len(password) < 7:
            return False
        else:
            return True
 
 
    #create your  password    
    def create_personal_password():
        conditon = True   
        while conditon:
            password = input("Enter password of choice greater than 7 chatracter: ")  
            if check_password(password):
                conditon = False
            else:
                conditon = True
        return password   

    while(conditon):
        passwordResponse = input("Are you satified with password Yes/No: ").lower()
      
        if passwordResponse == "yes":
            print("Your Details are:\n Name:"+ firstName + " " + lastName + "\n Email: "+ email )
            container["User" + str(num)] =  details
            conditon = False
        elif passwordResponse == "no":
             password = create_personal_password()
             details = [firstName,lastName,email,password]
             container["User" + str(num)]  =  details
             print("Your Details are:\nName:"+ firstName + " " + lastName + "\nEmail: "+ email ) 
             conditon = False       
        else:
            print("You Enterned a wrong Command, Kindly Enter Yes or No")

    print(("Congratulation Account Registered Succefully").upper())



cont = True
while cont: 
    askUser = input("Hello!!, Are you a new user Yes/No: ").lower()
    if askUser == "yes":      
       user()
       num = num + 1
    elif askUser == "no":
        cont = False
        print(container)
        # for item in container:
        #     print(container.get(item))   
    else:
        print("You Enterned a wrong Command, Kindly Enter Yes or No")
    



    
    

