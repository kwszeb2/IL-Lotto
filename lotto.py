# Illinois Lotto
# User either inputs their lucky numbers or its auto random generated

# import random number generator
from random import randint

# constant number for powerball, megamillion, and lucky day
a = 5

# constant number for lotto extra
b = 6

# constant number for pick 3 and 4
c = 3
d = 4

# auto generated powerball
def autoPowerPick(powerList):
	
	while len(powerList) < a:
		# check to see if there are duplicate numbers
		r = randint(1,69)
		if r not in powerList:
			powerList.append(r)

	return powerList.sort()

# manula generated powerball
def manualPowerPick(powerList):

	print("Choose your "+ str(a) + " lucky numbers! ")

	while len(powerList) < a:
		powerPick = int(input()) # user writes his lucky numbers 
		if powerPick  > 69: # if users picks number that exceeds prompts again for another number
			print("numbers go only to 69.. try again!!")
			powerPick = int(input())
			if powerPick < 70:
				powerList.append(powerPick) # adds it to the list
			else:
				print("invalid") 
		else:
			if powerPick not in powerList: # if users numbers is in the list and is <70
				powerList.append(powerPick)
			else:
				print("number already exists.. try again!!")
				powerPick = int(input())
				if powerPick < 70:
					powerList.append(powerPick)
				else:
					print("numbers go only to 69.. try again!!2")

	return powerList.sort()

# auto generated mega million
def autoMegaPick(megaList):
	
	while len(megaList) < a:
		# check to see if there are duplicate numbers
		r = randint(1,70)
		if r not in megaList:
			megaList.append(r)

	return megaList.sort()

# manual generated mega million
def manualMegaPick(megaList):

	print("Choose your "+ str(a) + " lucky numbers! ")

	while len(megaList) < a:
		megaPick = int(input()) # users writes his lucky numbers
		if megaPick  > 70: # if users picks number that exceeds prompts again for another number
			print("numbers go only to 70.. try again!!")
			megaPick = int(input())
			if megaPick < 71:
				megaList.append(megaPick) # adds it to the list
			else:
				print("invalid") 
		else:
			if megaPick not in megaList: # if users numbers is in the list and is <70
				megaList.append(megaPick)
			else:
				print("number already exists.. try again!!")
				megaPick = int(input())
				if megaPick < 71:
					megaList.append(megaPick)
				else:
					print("numbers go only to 70.. try again!!2")

	return megaList.sort()

# auto generated lotto extra 
def autoLottoXPick(lottoXList):
	
	while len(lottoXList) < b:
		# check to see if there are duplicate numbers
		r = randint(1,52)
		if r not in lottoXList:
			lottoXList.append(r)

	return lottoXList.sort()

# manual generated lotto extra
def manualLottoXPick(lottoXList):

	print("Choose your " + str(b) + " lucky numbers!")

	while len(lottoXList) < b:
		lottoXPick = int(input()) # users writes his lucky numbers
		if lottoXPick  > 52: # if users picks number that exceeds prompts again for another number
			print("numbers go only to 52.. try again!!")
			lottoXPick = int(input())
			if lottoXPick < 53:
				lottoXList.append(lottoXPick) # adds it to the list
			else:
				print("invalid") 
		else:
			if lottoXPick not in megaList: # if users numbers is in the list and is <70
				lottoXList.append(lottoXPick)
			else:
				print("number already exists.. try again!!")
				lottoXPick = int(input())
				if lottoXPick < 53:
					lottoXList.append(lottoXPick)
				else:
					print("numbers go only to 52.. try again!!2")

	return lottoXList.sort()

# auto generated pick 3
def autoPickTList(threeFireList):

	while len(threeFireList) < c:
		r = randint(0,9)
		threeFireList.append(r)

	return threeFireList

# manual generated pick 3
def manualPickTList(threeFireList):

	print("Choose your " + str(c) + " lucky numbers!")

	while len(threeFireList) < c:
		pickT = input() # users writes his lucky numbers
		threeFireList.append(pickT)

	return threeFireList

# auto generated pick 4
def autoPickFList(fourFireList):

	while len(fourFireList) < d:
		r = randint(0,9)
		fourFireList.append(r)

	return fourFireList

# manual generated pick 4
def manualPickFList(fourFireList):

	print("Choose your "+ str(d) + " lucky numbers!!")

	while len(fourFireList) < d:
		pickF = input() # users writes his lucky numbers
		fourFireList.append(pickF)

	return fourFireList

print("Welcome to Illinois Lotto!!\n")

print("Select which Lotto you want to play: (One or more lottos can be picked)\n"
	+ "\tPowerBall (P) \n" + " \tMega Million (M) \n" +
	" \tLotto Extra Shot (LE) \n" + " \tPick 3 Fireball (P3) \n" + " \tPick 4 Fireball (P4)\n")

# games played for each lotto
games = input("How many draws to play lotto? ")

powerList = [] # powerball empty list
megaList = [] # megamillion empty list
lottoXList = [] # lotto extra empty list
threeFireList = [] # pick 3 fireball empty list
fourFireList = [] # pick 4 fireball empty list

counter = 0

while counter < int(games):
	
	# player selets the games they want to play
	playSelect = input("What is your pick? ")

	# auto or manually generated lucky numbers
	playPick = input("\n(1) auto generated  or (2) user picks lucky numbers: ")

	if playSelect == "P":
		if playPick == "1":
			autoPowerPick(powerList)
		else:
			manualPowerPick(powerList)
		powerList.append(randint(1,26))
		print("Powerball numbers are: ", powerList)
		powerList.clear()
	elif playSelect == "M":
		if playPick == "1":
			autoMegaPick(megaList)
		else:
			manualMegaPick(megaList)
		megaList.append(randint(1,25))
		print("Mega Million numbers are: ",megaList)
		megaList.clear()
	elif playSelect == "LE":
		if playPick == "1":
			autoLottoXPick(lottoXList)
		else:
			manualLottoXPick(lottoXList)
		lottoXList.append(randint(1,25))
		print("Lotto Extra Shot numbers are: ",lottoXList)
		lottoXList.clear()
	elif playSelect == "P3":
		if playPick == "1":
			autoPickTList(threeFireList)
		else:
			manualPickTList(threeFireList)
		threeFireList.append(randint(0,9))
		print("Pick 3 Fireball numbers are: ",threeFireList)
		threeFireList.clear()
	elif playSelect =="P4":
		if playPick == "1":
			autoPickFList(fourFireList)
		else:
			manualPickFList(fourFireList)
		fourFireList.append(randint(0,9))
		print("Pick 4 Fireball numbers are: ",fourFireList)
		fourFireList.clear()
	else:
		print("Wrong selection...Try again!!")


	counter += 1

	print("Thank you for playing Illinois Lotto!!")