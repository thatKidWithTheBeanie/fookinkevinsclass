import time
import random
#### shhh top secret codes!!1!
staffCode = "abcd"
adminCode = "1234"
#### Make it shiny
def gap():
    print ("")
    print ("")
#### List of books in the libary at the moment
booksIn = ("The Danish Girl", "Animal Farm", "Coding for dummies", "The Communist Manifesto")
#### List of books out at the moment
booksOut = ("Me but as a book")

############# People here #######################
class people(object):

    def __init__(self, username, password, privLvl, nowOut):
        self.username = username
        self.privLvl = 1
        self.password = password
        
        self.maxOut = privLvl
        self.nowOut = None

    def withdraw(self, bookName, privLvl, username, nowOut):
        #### are they a dirty book whore?
        if len(self.nowOut) >= self.maxOut:
            print ("I'm sorry you need to return a book before you take it out")
        #### if not then they should remove the book from the shelf and add it to their bookbag
        else:
            nowOut.append(bookName)
            booksOut.append(bookName)
            booksIn.remove(bookName) #### Check this is right
            
    def returnbook(self, bookName, privLvl, username, nowOut):
       print("something here")
       
############################################
def start():
    global name
    global pword
    whoopsie = 0
    print ("@-----------------------@")
    print ("|Welcome to the Library!|")
    print ("@-----------------------@")
    gap()
    loopIt = True
    while loopIt == True:
        print ("Would you like to login or sign up?")
        answer = input("")

        ####################################
        ########### Sign up ################
        ####################################
        if answer == "sign up":
            
            loopIt = False
            print ("What is your name?")                        #### username
            name = input ("")
            print ("Enter a password")                          #### password
            pword = input ("")                                  #### Privilage escelation
            print ("Do you have a privilage code? yes or no")
            answer = input ("")
            if answer == "yes":
                while answer == "yes":                          #### fail checking
                    print ("What is your code?")
                    code = input ("")
                    if code == adminCode:
                        priv = 3                                #### isn't that an indentation and a half?
                        print ("it works")                      #### it's 5 am i hope i remeber i wrote this
                        break
                    elif code == staffCode:
                        priv = 2
                        print ("it works")
                        break
                    else:
                        print ("incorrect code, try again? yes or no")
                        answer = input ("")
            else:
                priv = 1
            #### and here we actually create the user
            (name) = people((name),(pword), (priv), []) #### need to make this global
            print ("Your username is " + (name).username + " and your password is " + (name).password)

        ####################################
        ########### Log in #################
        ####################################
        if answer == "login":
            loopIt = False       
            while whoopsie < 4:
                print ("What is your username")
                name = input ("")
                print ("What is your password?")
                pword = input ("")
                print ("Your username is " + (name).username + " and your password is " + (name).password)
                print (pword)
                if (pword) == ((name).password):
                    whoopsie = 0
                    print ("Thank you for logging in, have a nice day")################## HERE #################################################################################################################################
                    print ("Your username is " + (name).username + " and your password is " + (name).password)
                    menu()
                else:
                    whoopsie + 1
                    print ("Incorrect username and password combination")           
def menu():
    global name
    gap()
    gap()
    print ("      Menu")
    print ("")
    print ("1. Withdraw a book")
    print ("2. Return a book")
    print ("3. Admin options")
    print ("4. Search for a book")
    print ("5. Log out")
    gap()
    test = True
    while test == True:
        print ("Please enter 1, 2, 3, 4 or 5")
        answer = input ("")

        if answer == "1":
            test = False
            withdraw()
        if answer == "2":
            test = False
            returnbook()

        if answer == "3":
            if (name).privLvl == 3:
                test = False
                print (" Admin Menu")
                print ("")
                print ("1. Add a book")
                print ("2. Remove a user")
                print ("3. List all books")
                gap()
                print ("Please enter 1, 2 or 3")
                adminAn = input ("")
                    if adminAn == "1":
                        gap()
                        print ("What is the title of the book?")
                        newbook = input ("")
                        if book in booksIn or book in booksOut:
                            print ("This book is already in the library")
                        else:
                            x = True
                            while x == True
                            print ("Are you sure you want to add " + newbook + " to the library? yes or no")
                            yorn = input ("")
                            if yorn = "yes":
                                x = False
                                booksIn.append(newbook)
                                print ("You have added " + newbook + " to the library")
                                gap()
                            if yorn = "no":
                                x = False
                                print ("Addition cancelled")
                                gap()
                    if adminAn == "2":
                        gap()
                        print ("What user would you like to remove?")
                                
                            
            else:
                print ("You do not have permission to do this")

        if answer == "4":
            if (name).privLvl == 3 or (name).privLvl == 2:
                test = False
                gap()
                print ("What book would you like to search?")
                search = input ("")
                if search in booksIn:
                    print ("This book is available right now")
                if search in booksOut:
                    print ("This book is not available right now")
                else:
                    print ("This book is not listed")
                
                
                
            
        
    
    
############################ Hard coded users #########################
sam = people("sam", "p@assword", 3, [])
aaron = people("aaron", 2, "boringNpractical",[])
james = people("james", 1, "memez4godz",[])
#######################################################################    
print (sam.password)
print (aaron.username)
gap()
start()
menu()
