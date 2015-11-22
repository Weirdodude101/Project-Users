from components import Localizer
from components import yaml
import os
import os.path
import sys
if sys.platform == "win32":
	os.system("title Project Users")
	os.system("cls")
else:
	sys.stdout.write("\x1b]2;Project User\x07")
	os.system("clear")

def startUp():
	print ("Welcome to Project Users")
	print ("------------------------")
	print ("1: Create a person")
	print ("2: Find a person")
	print ("3: Login with admin account")
	option = raw_input("Enter here: ")
	if option == "1":
		clearConsole()
		addPersonMenu()
	elif option == "2":
		clearConsole()
		findPersonMenu()
	elif option == "3":
		clearConsole()
		adminLogin()
	else:
		clearConsole()
		print "You must choose 1, 2 or 3!"
		print "--------------------------"
		startUp()

def adminLogin():
	print ("Please login with a admin account")
	print ("---------------------------------")
	username = raw_input("Username: ")
	password = raw_input("Password: ")
	path = os.path.exists(Localizer.peopleDatabase + "{0}.yaml".format(username))
	if not path:
		clearConsole()
		print "Invalid account"
		print "------------------------"
		startUp()
	else:
		personInfo = loadYaml(Localizer.peopleDatabase + "{0}.yaml".format(username))
		if username == personInfo['Username'] and password == personInfo['Password'] and personInfo['Admin'] == True:
			clearConsole()
			adminConsole()
		else:
			clearConsole()
			print "Invalid account, heading back to start"
			print "--------------------------------------"
			startUp()

def adminConsole():
	print ("Welcome to the admin console")
	print ("----------------------------")
	print ("1: Manage Users")
	print ("2: Run custom code")
	print ("3: Go back to start")
	option = raw_input("Enter: ")
	if option == "1":
		clearConsole()
		manageUsers()
	elif option == "2":
		clearConsole()
		code = raw_input("Enter some code(May cause you to crash): ")
		exec(code)
		print ("--------------------------------------")
		print ("Code executed, heading back to console")
		print ("--------------------------------------")
		adminConsole()
	elif option == "3":
		clearConsole()
		startUp()
	else:
		clearConsole()
		print "Invalid option"
		print "--------------"
		adminConsole()

def manageUsers():
	print ("Manage users")
	print ("-----------------")
	print ("1: Edit a account")
	print ("2: Remove a account")
	print ("3: Admin a account")
	print ("4: Go back")
	print ("5: Go to start")
	option = raw_input("Enter here: ")
	if option == "1":
		clearConsole()
		editAccount()
	elif option == "2":
		clearConsole()
		removeAccount()
	elif option == "3":
		clearConsole()
		adminAccount()
	elif option == "4":
		clearConsole()
		adminConsole()
	elif option == "5":
		clearConsole()
		startUp()
	else:
		clearConsole()
		print "Invalid option, heading back to the console"
		print "------------------------------------------"
		adminConsole()

def editAccount():
	account = raw_input("Enter a account you would like to edit: ")
	path = os.path.isfile(Localizer.peopleDatabase + "{0}.yaml".format(account))
	if not path:
		print "Invalid username, heading back to console"
		print "-------------------------------------"
		adminConsole()
	else:
		personInfo = loadYaml(Localizer.peopleDatabase + "{0}.yaml".format(account))
		print ("Edit user info for: {0}".format(personInfo['Username']))
		print ("#########################")
		print ("Username: {0}".format(personInfo['Username']))
		print ("Password: {0}".format(personInfo['Password']))
		print ("First name: {0}".format(personInfo['FirstName']))
		print ("Last name: {0}".format(personInfo['LastName']))
		print ("Age: {0}".format(personInfo['Age']))
		print ("Gender: {0}".format(personInfo['Gender']))
		print ("Hobby: {0}".format(personInfo['Hobby']))
		print ("#########################")
		print ("1: Change username")
		print ("2: Change password")
		print ("3: Change first name")
		print ("4: Change last name")
		print ("5: Change age")
		print ("6: Change gender")
		print ("7: Change hobby")
		option = raw_input("Enter here: ")
		if option == "1":
			newUser = raw_input("Enter a new username for {0}: ".format(personInfo['Username']))
			optionDict = dict(
				Username = newUser,
				Password = personInfo['Password'],
				FirstName = personInfo['FirstName'],
				LastName = personInfo['LastName'],
				Age = personInfo['Age'],
				Gender = personInfo['Gender'],
				Hobby = personInfo['Hobby'],
				Admin = personInfo['Admin']
				)
			dumpYaml(Localizer.peopleDatabase + "{0}.yaml".format(personInfo['Username']),optionDict)
			os.rename(Localizer.peopleDatabase + "{0}.yaml".format(personInfo['Username']),Localizer.peopleDatabase + "{0}.yaml".format(newUser))
			clearConsole()
			print "Successfully edited account, heading back to console"
			print "---------------------------"
			adminConsole()
		elif option == "2":
			newPass = raw_input("Enter a new password for {0}: ".format(personInfo['Username']))
			editInfo(
				personInfo['Username'],
				newPass,
				personInfo['FirstName'],
				personInfo['LastName'],
				personInfo['Age'],
				personInfo['Gender'],
				personInfo['Hobby'],
				personInfo['Admin']
			)
			clearConsole()
			print "Successfully edited account, heading back to console"
			print "---------------------------"
			adminConsole()
		elif option == "3":
			newFname = raw_input("Enter a new first name for {0}: ".format(personInfo['Username']))
			editInfo(
				personInfo['Username'],
				personInfo['Password'],
				newFname,
				personInfo['LastName'],
				personInfo['Age'],
				personInfo['Gender'],
				personInfo['Hobby'],
				personInfo['Admin']
			)
			clearConsole()
			print "Successfully edited account, heading back to console"
			print "---------------------------"
			adminConsole()
		elif option == "4":
			newLname = raw_input("Enter a new last name for {0}: ".format(personInfo['Username']))
			editInfo(
				personInfo['Username'],
				personInfo['Password'],
				personInfo['FirstName'],
				newLname,
				personInfo['Age'],
				personInfo['Gender'],
				personInfo['Hobby'],
				personInfo['Admin']
			)
			clearConsole()
			print "Successfully edited account, heading back to console"
			print "---------------------------"
			adminConsole()
		elif option == "5":
			newAge = raw_input("Enter a new age for {0}: ".format(personInfo['Username']))
			editInfo(
				personInfo['Username'],
				personInfo['Password'],
				personInfo['FirstName'],
				personInfo['LastName'],
				newAge,
				personInfo['Gender'],
				personInfo['Hobby'],
				personInfo['Admin']
			)
			clearConsole()
			print "Successfully edited account, heading back to console"
			print "---------------------------"
			adminConsole()
		elif option == "6":
			newGender = raw_input("Enter a new gender for {0}: ".format(personInfo['Username']))
			editInfo(
				personInfo['Username'],
				personInfo['Password'],
				personInfo['FirstName'],
				personInfo['LastName'],
				personInfo['Age'],
				newGender,
				personInfo['Hobby'],
				personInfo['Admin']
			)
			clearConsole()
			print "Successfully edited account, heading back to console"
			print "---------------------------"
			adminConsole()
		elif option == "7":
			newHobby = raw_input("Enter a new hobby for {0}: ".format(personInfo['Username']))
			editInfo(
				personInfo['Username'],
				personInfo['Password'],
				personInfo['FirstName'],
				personInfo['LastName'],
				personInfo['Age'],
				personInfo['Gender'],
				newHobby,
				personInfo['Admin']
			)
			clearConsole()
			print "Successfully edited account, heading back to console"
			print "---------------------------"
			adminConsole()
		else:
			clearConsole()
			print "Invalid option, heading back to console"
			print "---------------------------------------"
			adminConsole()

def editInfo(username,password,firstname,lastname,age,gender,hobby,admin):
	optionDict = dict(
		Username = username,
		Password = password,
		FirstName = firstname,
		LastName = lastname,
		Age = age,
		Gender = gender,
		Hobby = hobby,
		Admin = admin
	)
	dumpYaml(Localizer.peopleDatabase + "{0}.yaml".format(username),optionDict)


def removeAccount():
	user = raw_input("Enter the name of the account you would like to remove: ")
	path = os.path.isfile(Localizer.peopleDatabase + "{0}.yaml".format(user))
	if not path:
		clearConsole()
		print "Invalid account, heading back to console"
		print "----------------------------------------"
		adminConsole()
	else:
		os.remove(Localizer.peopleDatabase + "{0}.yaml".format(user))
		clearConsole()
		print "Successfully removed account, heading back to console"
		print "----------------------------"
		adminConsole()

def adminAccount():
	setAdmin = raw_input("Enter the account you would like to turn admin: ")
	path = os.path.isfile(Localizer.peopleDatabase + "{0}.yaml".format(setAdmin))
	if not path:
		clearConsole()
		print "Invalid account, heading back to console"
		print "----------------------------------------"
		adminConsole()
	else:
		personInfo = loadYaml(Localizer.peopleDatabase + "{0}.yaml".format(setAdmin))
		editInfo(
			personInfo['Username'],
			personInfo['Password'],
			personInfo['FirstName'],
			personInfo['LastName'],
			personInfo['Age'],
			personInfo['Gender'],
			personInfo['Hobby'],
			True
		)
		clearConsole()
		print "Successfully admined account, heading back to console"
		print "----------------------------"
		adminConsole()


def addPersonMenu():
	print ("Enter a few credentials for your person")
	print ("---------------------------------------")
	username = raw_input("Enter username: ")
	path = os.path.isfile(Localizer.peopleDatabase + "{0}.yaml".format(username))
	if path:
		print "Username already taken, please choose another"
		print "---------------------------------------------"
		addPersonMenu()
	password = raw_input("Enter password: ")
	fname = raw_input("Enter first name: ")
	lname = raw_input("Enter last name: ")
	age = raw_input("Enter age: ")
	gender = raw_input("Enter gender: ")
	hobby = raw_input("Enter hobby: ")
	createYaml(Localizer.peopleDatabase + "{0}.yaml".format(username), username, password, fname, lname, age, gender, hobby)
	clearConsole()
	print ("Created a person with these credentials: ")
	print ("#########################")
	print ("Username: {0}".format(username))
	print ("Password: {0}".format(password))
	print ("First name: {0}".format(fname))
	print ("Last name: {0}".format(lname))
	print ("Age: {0}".format(age))
	print ("Gender: {0}".format(gender))
	print ("Hobby: {0}".format(hobby))
	print ("#########################")
	print ("1: Go back to start")
	print ("2: Find people")
	print ("3: Create another person")
	option = raw_input("Enter here: ")
	print ("#########################")
	if option == "1":
		clearConsole()
		startUp()
	elif option == "2":
		clearConsole()
		findPersonMenu()
	elif option == "3":
		clearConsole()
		addPersonMenu()
	else:
		clearConsole()
		print "Invalid option, heading back to start"
		print "-------------------------------------"
		startUp()

def findPersonMenu():
	userSearch = raw_input("Enter a username to search: ")
	clearConsole()
	path = os.path.isfile(Localizer.peopleDatabase + "{0}.yaml".format(userSearch))
	if not path:
		print "Invalid username, heading back to start"
		print "-------------------------------------"
		startUp()
	else:
		personInfo = loadYaml(Localizer.peopleDatabase + "{0}.yaml".format(userSearch))
		print ("User info for: {0}".format(personInfo['Username']))
		print ("#########################")
		print ("Username: {0}".format(personInfo['Username']))
		print ("Username: {0}".format(personInfo['Password']))
		print ("First name: {0}".format(personInfo['FirstName']))
		print ("Last name: {0}".format(personInfo['LastName']))
		print ("Age: {0}".format(personInfo['Age']))
		print ("Gender: {0}".format(personInfo['Gender']))
		print ("Hobby: {0}".format(personInfo['Hobby']))
		print ("#########################")
		print ("1: Go back to start")
		print ("2: Find more people")
		print ("3: Create a person")
		option = raw_input("Enter here: ")
		print ("#########################")
		if option == "1":
			clearConsole()
			startUp()
		elif option == "2":
			clearConsole()
			findPersonMenu()
		elif option == "3":
			clearConsole()
			addPersonMenu()
		else:
			clearConsole()
			print "Invalid option, heading back to start"
			print "-------------------------------------"
			startUp()
	
def dumpYaml(filepath,option):
	with open(filepath, 'w') as outfile:
		newAttb = outfile.write(yaml.dump(option,default_flow_style=False) )
	return newAttb

def loadYaml(filepath):
	with open(filepath, "r") as file_descriptor:
		personInfo = yaml.load(file_descriptor)
	return personInfo

def createYaml(filepath,username,password,fname,lname,age,gender,hobby):
	personDict = dict(
		Username = username,
		Password = password,
		FirstName = fname,
		LastName = lname,
		Age = age,
		Gender = gender,
		Hobby = hobby,
		Admin = False
		)
	with open(filepath, 'w') as outfile:
		newAcc = outfile.write(yaml.dump(personDict,default_flow_style=False) )
	return newAcc

def clearConsole():
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

startUp()
