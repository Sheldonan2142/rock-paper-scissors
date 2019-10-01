# abigail sheldon
# Rock paper scissors
# Variables
# insert random comments
import random

pscore = 0
cscore = 0
ties = 0
computerChoice = ["r","p","s"]
# welcome message 
# print the message & prompt for player name
print("Welcome to Rock Paper Scissors")
pname=input("What is your name? ")



# final score
def printScore():
	# write message & player / computer score
	print("The score is: ")
	print(pname +": "+str(pscore))
	print("computer: "+str(cscore))
	print("ties: "+str(ties))

# game loop
# make a forever loop
while True:
	# print current score
	printScore()
	# prompt for a choice ( r(rock), p(paper), s(scissors), q(quit))
	pchoice=input("Enter r (rock), p (paper), s (scissors), or q (to quit): ")
	# deal w players entering q
	if pchoice=="q":
		break
	#get computer's choice
	cHoice=random.choice(computerChoice)


#compare for players entering r
if pchoice == "r":
	print(pname +" picked rock")
	#if computer is r, p, or s
	if cHoice=="r":
		print("computer picked rock")
		print("this is a tie")
		ties=ties+1
	elif cHoice=="p":
		print("computer picked paper")
		print("paper covers rock")
		cscore=cscore+1
	else:
		print("computer picked scissors")
		print("rock breaks scissors")
		pscore=pscore+1
#compare for players entering p
elif pchoice=="p":
	pass
	print(pname +" picked paper")
	if cHoice=="r":
		print("computer picked rock")
		print("paper covers rock")
		pscore=pscore+1
	elif cHoice=="p":
		print("computer picked paper")
		print("this is a tie")
		ties=ties+1
	else:
		print("computer picked scissors")
		print("scissors cuts paper")
		cscore=cscore+1
#compare for players entering s
elif pchoice=="s":
	pass
	print(pname +" picked scissors")
	if cHoice=="r":
		print("computer picked rock")
		print("rock breaks scissors")
		cscore=cscore+1
	elif cHoice=="p":
		print("computer picked paper")
		print("scissors cut paper")
		pscore=pscore+1
	else:
		print("computer picked scissors")
		print("this is a tie")
		ties=ties+1
# deal w player entering unknown
