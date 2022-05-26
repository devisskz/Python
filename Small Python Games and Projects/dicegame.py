import random
import time

def welcome_screen():
	print("*****************************")
	print("Welcome to the game of notone")
	print("*****************************")

#main program

def play_round():
	'''play one round and return the score for that round'''
	die1 = random.choice(range(1,7))
	die2 = random.choice(range(1,7))
	first_roll = die1 + die2
	print("Your first roll is a ", first_roll)
	roll_again = input ("Do you want to roll again? (y/n)")
	total = first_roll
	while roll_again == "y" or roll_again == "yes":
		die1 = random.choice(range(1,7))
		die2 = random.choice(range(1,7))
		roll = die1 + die2
		print("You rolled a", roll)
		if roll == first_roll:
			return 0
		else:
			total = total + roll
			roll_again = input ("Do you want to roll again? (y/n)")
	return total

def display_scoreboard(p,c):
	print("Scoreboard")
	print("----------")
	print("Computer: ", c)
	print("Player:   ", p)

#main program

welcome_screen()
player_score = 0
computer_score = 0

time.sleep(2)
for i in range(10):
	print("Round #",i+1)
	time.sleep(1)
	score = play_round()
	player_score = player_score + score
	

	print("You scored " + str(score) + " points for that round")
	print("It is the computer's turn now")
	score = play_round()

	computer_score = computer_score + score

	time.sleep(1)
	print("The computer scored " + str(score) + " points for that round")
	print()
	display_scoreboard(player_score, computer_score)
	print()

if player_score > computer_score:
	print("You win")
elif player_score < computer_score:
	print("You lose")
else:
	print("It's a tie!")