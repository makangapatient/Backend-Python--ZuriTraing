#register
#- first_name, last_name, password, email
#- generate user account

#login
#- account number and password

#bank operations

#Initializing the system
import random
import re #import regular expression
from datetime import datetime

now = datetime.now()
database = {} #dictionary
balance = 200 #current account balance

# Make a regular expression for validating an Email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def init():

   # isValidOperationSelected = False
    print('Welcom to bankPHP')
    #while isValidOptionSelected == False:

    haveAccount = int(input('Do you have account with us: 1 (yes) 2 (no) \n'))

    if(haveAccount == 1):
            #isValidOptionSelected = True
        login()    
    elif(haveAccount == 2):
            #isValidOptionSelected = True
        register()

    else:
        print('You have selected invalid option, Please try agian!')
        print()
        print('=== ====== ====== ===== ====== ===== ====== ===== ==')
        init ()      

#login function
def login():
    print('== === Login === ==')
        
    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
        
                bankOperation(userDetails) #call bankOperation function
                    #isLoginSuccessful = True
                                    
    print('Invalid account or password')
    print()
    print('=== ====== ===== ==== == ==')
    print()
    login() #call the login function

#register function
def register():

    print('****** Register ******')
    
    #validate email
    email = check()
    first_name = firstNameCheck() ##firstname is only constituted of letter
    last_name = lastNameCheck() ##lastname is only constituted of letter
    password = checkPassword() #call check password function

    #generate user account number
    accountNumber = generationAccountNumber()
    print()
    
    #generate PIN number
    pinNumber = generatePin()
    print()
    
    #save all the user information into a dictionary that we use as database
    database[accountNumber] = [first_name, last_name, email, password, pinNumber]
    
    print('Your Account Has been created!')
    print('== ==== ====== ===== === == ===')
    print('Your Account Number is: %d' % accountNumber) #display Account Number
    print('Your PIN number is: %d' % pinNumber) #display PIN number
    print('Your password is {}'.format(password))
    print('Make sure you keep them safe')
    print('== ==== ====== ===== === === ===')
    print()

    #return database
    #call the login function
    login() 
    #return database

#function to print bank operation
def bankOperation(user):
    print('Welcom %s %s' % (user[0], user[1]))

    #Displaying date time
    print('Current date and time: ') 
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    print()
              
    #Ask user to select one bank Operation
    SelectedOption = int(input('What would you like to do? (1) deposit (2) withdrawal (3) complaint (4) logout \n'))

    if(SelectedOption == 1):
        #Call deposit Operation
        depositOperation()

    elif(SelectedOption == 2):       
        #Call withdrawal Operation
        withdrawalOperation()

    elif(SelectedOption == 3):
        #call complaint function
        complaint()

    elif(SelectedOption == 4):
        logout()

    else:
        print('Invalid Option Selected!')
        bankOperation(user)

def withdrawalOperation():
     print('How much would you like to withdraw? \n')
     amount = int(input('Enter the Amounths: \n')) #user input the amounths

     balance = 200
     
     if amount > balance:
        print('Insufficient Balanace')
     else:
        balance = balance - amount
        
        print('== ===== ====== ===== ===== ===== ')
        print('Take your cash {} '.format(amount)) #invite the user to take the cash
        print('You have a balance amounth of {}'.format(balance))
        print('== ===== ====== ===== ===== ===== ')
        print()
     
        bankOperation2 = int(input('Do you want to continue with bank operations? (1) Yes (2) NO \n'))
     
        while bankOperation2 == 1:
        
            Options = int(input('What would you like to do? (1) deposit (2) withdrawal (3) Complaint \n'))
             
            if(Options == 1):
                #Call deposit Operation
                depositOperation()

            elif(Options == 2):       
                #Call withdrawal Operation
                withdrawalOperation()
                
            elif(Options == 3):
                complaint()#call complaint function

            else:
                print('Invalid option, Please try again')
                        
            
        print('Thank you and see you soon!')
        login() #call login function    
     
#deposit function    
def depositOperation():
    print('How much would you like to deposit? \n')
    amount = int(input('Please enter the amounth: \n'))
    first_name = firstNameCheck() #firstname is only constituted of letter
    last_name = lastNameCheck()#lastname is only constituted of letter
    phone_number = input('Enter your phone number:  \n')
    refNumber = input('Enter a referrence number: \n')
    balance = 0
            
    balance = balance + amount #calculate the current balance
    
    print('=== ===== ====== ====== =====')
    print('You deposit the amounth of {}'.format(amount))
    print('Current balance is {}'.format(balance))
    print('=== ===== ====== ====== =====')
    print()
    
    bankOperation2 = int(input('Do you want to continue with bank operations? (1) Yes (2) NO \n'))
     
    while bankOperation2 == 1:
        
        Options = int(input('What would you like to do? (1) deposit (2) withdrawal (3) Complaint \n'))
             
        if(Options == 1):
            #Call deposit Operation
            depositOperation()

        elif(Options == 2):       
            #Call withdrawal Operation
            withdrawalOperation()

        elif(options == 3):
            complaint()   
        
        else:
            print('Invalid option, Please try again')        
            
    print('Thank you and see you soon!')
    login() #call login function 
    
#user's complaint function
def complaint():
    
            print('What issue will you like to report? \n')
            report = input('Please enter the issue: \n')
            print('Thank you for contacting us')
            
            bankOperation2 = int(input('Do you want to continue with bank operations? (1) Yes (2) NO \n'))
     
            while bankOperation2 == 1:
        
                Options = int(input('What would you like to do? (1) deposit (2) withdrawal (3) Complaint \n'))             
                if(Options == 1):
                    #Call deposit Operation
                    depositOperation()

                elif(Options == 2):       
                    #Call withdrawal Operation
                    withdrawalOperation()

                elif(options == 3):
                    #call complaint function
                    complaint()   
        
                else:
                    print('Invalid option, Please try again')        
            
            print('Thank you and see you soon!')
            login() #call login function 
                   
#logout function
def logout():
    exit()
    
#function to check email
def check():
    # pass the regular expression
    # and the string in search() method
    count =0
    while count < 3:
        email = input('Please enter your email address? \n')
        if(re.search(regex, email)):
            #print('Valid Email')
            break
        else:
            print('Invalid Email, please enter a valid email')
            count +=1
            logout()#exit your profile
    return email


#function to check that first_name  not a numeric value
def firstNameCheck():
    count = 0
    while count < 3:
        first_name=input("What is your first_name? \n").lower()
        if first_name.isalpha():
                break
        else:
             print ("invalid first_name please try again")
             count +=1
             logout()#exit your profile
    return first_name
    
 
 
#function to check that last_name  not a numeric value             
def lastNameCheck():
    count=0
    while count < 3:
        last_name=input("What is your last_name? \n").lower()
        if last_name.isalpha():
                break
        else:
             print ("invalid last_name please try again")
             count +=1
             logout()#exit your profile
    return last_name


#function to generate account number
def generationAccountNumber():

    return random.randrange(1111111111,9999999999) #generate an account randomly 10 number  
    

#function togenerate 5 digits PIN number
def generatePin():

    return random.randrange(11111,99999) #generate five digit pin number
 

#Python program to check validation of password
#Module of regular expression is used with search()
#Password must minum lenght of 8 characters, capital and small letters,
#numbers, specials characters     
def checkPassword():

    password = input('Please enter your password: ')
    flag = 0
    while True:
            if (len(password)<8):
                    flag = -1
                    break
            elif not re.search("[a-z]", password):
                    flag = -1
                    break
            elif not re.search("[A-Z]", password):
                    flag = -1
                    break
            elif not re.search("[0-9]", password):
                    flag = -1
                    break
            elif not re.search("[_@$]", password):
                    flag = -1
                    break
            elif re.search("\s", password):
                    flag = -1
                    break
            else:
                    flag = 0
                    print("Valid Password")
                    break
    if flag ==-1:
        print("Not a Valid Password")
    return password

init ()
