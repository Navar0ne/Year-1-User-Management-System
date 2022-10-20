#-------------------------------------------------------------------------------
# Name:        Assessment V.1
# Purpose:
#
# Author:      c1007956
#
# Created:     02/11/2021
# Copyright:   (c) c1007956 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import string
userDatabase = []
users = []
uNames = []

print(" : : Welcome to the User Management System : : \n -----")

uName = "admin"
pwd = "password"
keepGoing = True

userName = input("Please Input username: ")             # Prompts user for username and password
password = input("Please Input password: ")
attempt = 1
print("Attempt: ", attempt)                             # Counts the user's attempts to login
attempt+=1

checkCred = (userName==uName) and (password==pwd)       # Checks inputted credentials against admin credentials

while(not checkCred):
    userName = input("Please Input username: ")
    password = input("Please Input password: ")
    print("attempt: ", attempt)
    attempt+=1
    if (userName==uName) and (password==pwd):
        break
    if attempt == 3:
        print("\n! ! Warning, 1 attempt remaining ! !\n")
    if attempt == 4:
        print("Access Denied")
        keepGoing = False
        exit()


print("\nLogin Successful\n")

keepGoing = True                                             # Allows me to open a while loop and close it later.
#                                                            # Outputs a menu when variable is called
mainMenuString = ": : Main Menu : : \n\n\
1. Create New User \n\
2. View User \n\
3. Update User \n\
4. Quit \n\n\
Select a menu - Input a number: "

while(keepGoing):
    choice1 = input(mainMenuString)                          # Checks to make sure the input is a number
    if choice1.isdigit():
        choice1 = int(choice1)
    else:
        print("\nYou have input a non digit value. Select again.")

    if choice1 == 1:
        keepGoing2 = True
        while(keepGoing2):

            print("\n: : Creating New User : :\n")
            user1Name = input("Input first name: ")
            user2Name = input("Input second name: ")
            menu1Str1 = "\nSelect a role for the user: \n\n1. = User\n2. = Admin\n"

            keepGoing3 = True
            while(keepGoing3):

                choice2 = input(menu1Str1)
                if choice2.isdigit():
                    choice2 = int(choice2)
                else:
                    print("You have input a non digit value. Select again.")
                    continue

                if choice2 > 2:
                    print("\nThere is no option",choice2, "\n")
                    continue
                elif choice2 == 1:                              #Assignes roles based on user input
                    userRole = "User"
                elif choice2 == 2:
                    userRole = "Admin"
                else:
                    print("You have input an invalid digit value. Select again.")

                keepGoing3 = False

            menu1Str2 = "\nSelect a department for the user :\n\n1. admin\n2. operations\n3. technology\n\n"

            keepGoing4 = True
            while(keepGoing4):

               choice3 = input(menu1Str2)
               if choice3.isdigit():
                choice3 = int(choice3)
               else:                                               # Checks if input is number. If not, restarts the while loop
                print("You have input a non digit value. Select again.")
                continue

               if choice3 > 3:
                    print("\nThere is no option",choice3, "\n")
                    continue

               keepGoing4 = False

            if choice3 == 1:
                userDept = "Administrative"
            elif choice3 == 2:
                userDept = "Operations"
            elif choice3 == 3:
                userDept = "Technology"

            print("\n: : User Profile Summary : :\n\nUser first name: ", user1Name,"\nUser second name: ", user2Name, "\nUser Role: ", userRole, "\nUser Department: ", userDept, "\n")


            confUser = input("Please confirm (c) to continue with user creation. Otherwise, press any to return to the main screen.")

            if confUser == "c":

                customUser = [user1Name, user2Name, userRole, userDept]     # Puts all user details up to this point into a single list

                print("\nGenerating Username... ")                          # VVV Generates new username based on names and a random number

                randomNumber = random.randint(1,99999)
                newUserName = user1Name [:2] + user2Name[:2] + str(randomNumber)

                print("Generating Password... ")                            # VVV Generates random password by multiplying two whole numbers together

                characters = list(string.ascii_letters)
                randNum1 = random.randint(1,99999)
                randNum2 = random.randint(1,99999)

                newPassword = (randNum1*randNum2)

                tempPass = newPassword                                      # Creates hidden password by slicing original password and adding asterisks after the first 3 numbers
                tempPass = str(tempPass)
                hiddenPass = tempPass[:3] + "*****"

                print("\nYour new username is: ", newUserName)
                print("Your new password is: ", newPassword, "\n")



                user1 = [newUserName, newPassword, hiddenPass]               # Adds the username, password, and hidden password to a list
                fullList = customUser + user1                                # Adds the two lists holding all of the user information together into one big list


                if user1 in userDatabase:                                    # Checks the main database list for a user with a duplicate username
                    print("This user is already in the system. Creating new User.")

                    randomNumber2 = random.randint(1,99)                     # If a duplicate username is found, generate a new one.
                    if randomNumber2 == randomNumber:                        # If new username happens to be the same as the old one, this increments it by 1
                        randomNumber2 +=1
                    newUserName = user1Name [:3] + user2Name[:3] + str(randomNumber2)


                    users.append(user1)                                      # Appends the temporary "user1" to the permenant "users" list

                else:
                    users.append(user1)

                userDatabase.append(fullList)                                # Appends the "fullList" list to the final "userDatabase" list



                finishedCreation = input("User creation complete. Press (q) to exit. Otherwise press any other to return to menu.")

                if finishedCreation == "q":
                    exit()

                else:
                    break

            else:

                break


    elif choice1 == 2:

        print(userDatabase)


        print("\n: : Viewing Users : : \n\n\
        -----\n\
        List of users\n\
        -----\n\n")

        if len(userDatabase) == 0:                                           # Counts the amount of records in the "userDatabase" list and displays them
            print("There are no records")
        else:
            print("There is/are: ", len(userDatabase), "records\n")


        recordCounter = 1                                                    # Sets a counter
        for i in userDatabase:                                               # Counts through all elements in the list and allows them to be called


            print("Record: ", recordCounter, "\n\nFirst Name: ", i[0],"\nLast Name: ", i[1], "\nRole: ", i[2],"\nDepartment: ", i[3], "\nUsername: ", i[4], "\nPassword: ", i[6], "\n") # Displays a table of all user info (with a hidden password)
            recordCounter +=1                                                # Increments the counter by 1 every time the loop is repeated

        finishedViewing = input("(Press (q) to see the user passwords\n\
        Warning user password view should get permissions from super admin!)\n\
        Press anything to go back to main menu")

        if finishedViewing == "q":

            recordCounter = 1
            for i in userDatabase:

                print("Record: ", recordCounter, "\n\nFirst Name: ", i[0],"\nLast Name: ", i[1], "\nRole: ", i[2],"\nDepartment: ", i[3], "\nUsername: ", i[4], "\nPassword: ", i[5], "\n") # Displays a table of all user info (with a hidden password)
                recordCounter +=1

        else:
            break



    elif choice1 == 3:
        print("Updating User\n\n")

        counter = 0

        confUpdate = input("Input username to edit (press 1 to return to main menu)") # Prompts user to input a preexisting username to edit the information of the profile associated with it
        if confUpdate == 1:
            break
        else:
            for checkUser in userDatabase:                                   # Begins a for loop that looks through the user database
                if confUpdate in checkUser:                                  # Checks if the inputted username is found by checkUser

                    print("User", userDatabase[counter][0], "found!")        # Prints that the program has found the user and prompts admin to update a field
                    updateMenu = input("\nWhich field would you like to update?\n1. First Name\n2. Last Name\n3. Role\n4. Department\nPress (q) to return to the previous menu.")


                    if updateMenu == "1":
                        print("Updating First Name\n")

                        newUser1Name = input("Please input a new first name")
                        userDatabase[counter][0] = newUser1Name              # Changes the chosen item in the list to whatever the admin inputs


                    elif updateMenu == "2":
                        print("Updating Last Name\n")

                        newUser2Name = input("Please input a new first name")
                        userDatabase[counter][1] = newUser2Name

                    elif updateMenu == "3":
                        print("Updating Role\n")

                        newRoleInput = input("What would you like to update the role to?\n\
                        1. user\n\
                        2. admin")

                        if newRoleInput == "1":
                            userDatabase[counter][2] = "User"                # Changes the chosen item in the list to whatever the admin inputs
                        elif newRoleInput == "2":
                            userDatabase[counter][2] = "Admin"


                    elif updateMenu == "4":
                        print("Updating Department\n")

                        newDeptInput = input("What would you like to update the Department to?\n1. admin\n2. operations\n3. technology\n")

                        if newDeptInput == "1":                              # Changes the chosen item in the list to whatever the admin inputs
                            userDatabase[counter][3] = "Admin"
                        elif newDeptInput == "2":
                            userDatabase[counter][3] = "Operations"
                        elif newDeptInput == "3":
                            userDatabase[counter][3] = "Technology"


                    elif updateMenu == "q":                                   # Exits back to main menu if "q" key is pressed
                        break

                counter += 1



    elif choice1 == 4:
        exit()                                                               # If "4" is pressed, ends the program

    else:
        print("\nThere is no menu ",choice1, "\n")