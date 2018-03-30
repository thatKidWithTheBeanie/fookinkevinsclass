import time
import random
staffCode = "abcd"
adminCode = "1234"
#### List of books in the libary at the moment
booksIn = ("The Danish Girl", "Animal Farm", "Coding for dummies", "The Communist Manifesto")
#### List of books out at the moment
booksOut = ("Me but as a book")

############# People here #######################
class people(object):

    def __init__(self, username, privLvl, password, nowOut):
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

############################ Hard coded users #########################
sam = people(username="sam", privLvl=3, password="p@assword", nowOut=[])
aaron = people("aaron", 2, "boringNpractical",[])
james = people("james", 1, "memez4godz",[])
#######################################################################

############################################
def start():
    print ("Welcome to the Library!")
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
            password = input ("")                               #### Privilage escilation
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
            (name) = people(username = (name), privLvl = (priv), password = (password), nowOut = []) 
            print ("Your username is " + (name).username + " and your password is " + (name).password)

        ####################################
        ########### Log in ################
        ####################################
        if answer == "login":
            loopIt = False
            print ("What is your username?")
            name = input ("")
            print ("What is your password?")
            password = input ("")
        


start()
