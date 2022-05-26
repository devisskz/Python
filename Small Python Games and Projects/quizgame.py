
'''This is a multiple choice quiz game with 10 questions. 
	You're not allowed to make any mistakes, meaning for 
	one mistake you automatically lose. The first five
	questions are easy, and the other five are hard'''

import time


"""Starting screen"""

def welcome_screen():
	username = input("What is your name player? ")
	time.sleep(1)
	print("Hello ", username,"!")
	print("******************************************")
	print("WELCOME TO THE WORLD FAMOUS KNOWLEDGE QUIZ")
	print("******************************************")
	time.sleep(1)
	return username

"""Explains the rules of the game at the start"""

def rules():
	time.sleep(1)
	print("This guiz consists of ten questions, and one mistake is an automatic loss")
	time.sleep(2)
	print("You have to get through the ten questions without a mistake to get your prize")
	time.sleep(2)

"""To begin game press y"""

def quiz(username):
	begin_game = input("Are you ready to begin " + username + " (y)? ")
	if begin_game == "y" or begin_game == "yes":
		print()
		easy_question()

"""Easy question list"""

def easy_question():
	time.sleep(1)
	print("How many countries are there in the world, that are recognized by the UN?")
	question_a = input("A) 65 		B) 112 		C) 193		D) 235	")
	if question_a == "C" or question_a == "193" or question_a == "c":
		time.sleep(1)
		print()
		print("Great start!")
		print()
		print("Then we move on to the next question!")
		print()
		time.sleep(2)
		easy_question2()
	else:
		lostgame()

def easy_question2():
	time.sleep(1)
	print("What is the most populated city in the world?")
	question_b = input("A) New York city 	B) Tokyo	C) London 	D) Moscow ")
	print()
	if question_b == "B" or question_b == "Tokyo" or question_b == "tokyo" or question_b == "b":
		time.sleep(1)
		print("And the most populated city in the world is...")
		print()
		time.sleep(2)
		print("Tokyo! You are right!")
		print()
		print("Next question...")
		print()
		easy_question3()

	else:
		time.sleep(1)
		lostgame()

def easy_question3():
	time.sleep(1)
	print("What does the number Pi represent?")
	question_c = input("A) Circumference of a circle to its diameter	B) The ratio of triangle's sides	 C) Sum of the sides of a polygon 	")
	if question_c == "A" or question_c == "a" or question_c == "circumference":
		time.sleep(1)
		print("This is right!, Pi is the circumference of a circle to its diameter!")
		print()
		time.sleep(2)
		print("The circumference of a circle to its diameter!")
		print()
		print("Good job, next question...")
		print()
		easy_question4()
	else:
		time.sleep(1)
		lostgame()

def easy_question4():
	time.sleep(1)
	print("Which of these did the famous scientist Isaac Newton discover?")
	question_d = input("A) DNA Cloning 	 B) Law of gravitation 	C) Atomic Structure 	D) The Solar System 	")
	if question_d == "B" or question_d == "b" or question_d == "law of gravitation":
		time.sleep(1)
		print("Isaac Newton is famous for a lot of things, among which is...")
		print()
		time.sleep(2)
		print("The law of gravitation! This is the right answer!")
		print()
		print("Now, next question...")
		print()
		easy_question5()
	else:
		time.sleep(1)
		lostgame()

def easy_question5():
	time.sleep(1)
	print("Hong Kong was most recently a colony of which country?")
	question_e = input("A) China 	B) Spain 	C) Portugal 	D) England 	")
	if question_e == "D" or question_e == "d" or question_e == "England":
		time.sleep(1)
		print("I'm sorry but...")
		print()
		time.sleep(2)
		print("This is right! Hong Kong was an English colony before they gained their independence")
		print()
		print("You have finished the first half of the questions")
		print()
		print("These questions were easy level, now we move on to the hard...")
		time.sleep(1)
		hard_question1()
	else:
		time.sleep(1)
		lostgame()

def hard_question1():
	time.sleep(1)
	print("Which of the three most followed religions, Christianity, Islam, and Buddhism is the oldest?")
	question_f = input("A) Christianity 	B) Islam 	C) Buddhism  	")
	if question_f == "c" or question_f == "C" or question_f == "buddhism" or question_f == "Buddhism":
		time.sleep(1)
		print("Great start!")
		print()
		time.sleep(2)
		print("That is the right answer!")
		print()
		print("Now, more hard questions")
		print()
		hard_question2()
	else:
		time.sleep(1)
		lostgame()

def hard_question2():
	time.sleep(1)
	print("What country exports the most coffee beans woth of value per year?")
	question_z = input("A) Vietnam 	B) Colombia 	C) Germany	   D) Brazil	")
	if question_z == "d" or question_z == "D" or question_z == "brazil" or question_z == "Brazil":
		time.sleep(1)
		print("Amazing job!")
		print()
		time.sleep(2)
		print("Women in the USA got their right to vote in 1920!")
		print()
		print("Second hard question...")
		print()
		hard_question3()
	else:
		time.sleep(1)
		lostgame()

def hard_question3():
	time.sleep(1)
	print("Approximately when did women in the US get the right to vote?")
	question_g = input("A) 1820-1890 	B) 1900-1950 	C) 1960-2000 	")
	if question_g == "b" or question_g == "B" or question_g == "1900" or question_g == "1900-1950" or question_g == "1920":
		time.sleep(1)
		print("Amazing job!")
		print()
		time.sleep(2)
		print("Women in the USA got their right to vote in 1920!")
		print()
		print("Second hard question...")
		print()
		hard_question4()
	else:
		time.sleep(1)
		lostgame()

def hard_question4():
	time.sleep(1)
	print("The FIFA world cup (soccer) in 2018 was hosted by which country?")
	question_h = input("A) Russia 	B) England 	C) Qatar 	D) Korea 	")
	if question_h == "a" or question_h == "A" or question_h == "Russia" or question_h == "russia":
		time.sleep(1)
		print("Yes!")
		print()
		time.sleep(1)
		print("The 2018 FIFA world cup was hosted by Russia!")
		print()
		print("Almost there! Now to the last hard question..")
		print()
		hard_question5()
	else:
		time.sleep(1)
		lostgame()

def hard_question5():
	time.sleep(1)
	print("Where does the US get most of its oil from?")
	question_i = input("A) Iraq 	B) Saudi Arabia 	C) Canada 	D) Mexico 	")
	if question_i == "c" or question_i == "C" or question_i == "Canada" or question_i == "canada":
		time.sleep(1)
		print("Wow! You have completed all the questions!")
		print()
		time.sleep(1)
		wingame()
	else:
		time.sleep(1)
		lostgame()




"""If answered wrong, lose the game"""

def lostgame():
	print()
	print("Oh no, looks like your answer is wrong... Sorry but Better luck next time")
	
"""Start of game, order of functions"""

username = welcome_screen()
rules()
quiz(username)

"""ending of the game if won"""
def wingame():
	print("Very impressive, you are one of the only people in the world who have completed this hard quiz")
	time.sleep(1)
	print()
	print("******************************************************************")
	print("We would like to congratulate and thank you for playing this game!")
	print("******************************************************************")
	print()
	time.sleep(1)
	print("Good luck in all your future doings, human")
	endgame()