#Name: Parker and Batyr
#Date: May 13, 2019
#Hawaiian Words 
#
#

import time

def introduction():
	time.sleep(2)
	print("Topic: Hawaiian Word")
	print("What is Hawaiian word?")
	print("Hawaiian language is a simple language that consists of 12 characters, 5 vowels and 7 consonants.")
	print( "In phonetic, the consonants and vowels split into different pronouncing sound")
	print("While the consonants like 'p, k, h, l, m, n' pronounced like English versions, the consonant 'w' sounds differently based on the letter infront or behind it")
	print("Vowels and Vowel groups are separated in the way they pronounced as well")
	time.sleep(2)

	print("For instance:")
	print("...Vowels:"
		"a = ah"
		" e = eh"
		"i = ee"
		"o = oh"
		"u = oo")
	print("...Vowel groups:"
		"ai = eye" 
		"ae = eye"
		"ao = ow"
		"au = ow"
		"ei = ay"
		"eu = eh-oh"
		"iu = ew"
		"oi = oy"
		"ou = ow"
		"ui = ooey")
	time.sleep(2)
	print("For this assignment, a string iteration, manipulation, loops and function will be used to convey an input of a word to manipulate a corresponding Hawaiian pronounciation")



#Creating a dictionary structure for all the Hawaiian pronounciation 
#Reference for dictionary means of usage: https://realpython.com/python-dicts/

List_pronounciation = dict([
	("a", "ah"),
	("e", "eh"),
	("i", "ee"),
	("o", "oh"),
	("u", "oo"),
	("ai", "eye"),
	("ae", "eye"),
	("au", "ow"),
	("ei", "ay"),
	("eu", "eh-oh"),
	("iu", "ew"),
	("oi", "oy"),
	("ou", "ow"),
	("ui", "ooey"),
	("p", "p"),
	("k", "k"),
	("h", "h"),
	("l", "l"),
	("m", "m"),
	("n", "n")
	])

#Creating a while loop to evaluate the right condition of a normal vowel to execute a correct Hawaiian pronouncation with what it is defined on the top

def words():
	characters=['a', 'e', 'i', 'o', 'u', 'p', 'k', 'h', 'l', 'm', 'n', 'w']

	"""if characters==('a') or ('e') or ('i') or ('o') or ('u') or ('p') or ('k') or ('h') or ('l') or ('m') or ('n') or ('w'):
		"""
	while True:
		word=input('Please enter an alphabet vowel or combine 2 vowels if desire:')

		if(realword(characters, word)):
			result=Hawaiianword(word)
			#Runs realword and Hawaiianword functions for validity and result
			print(word,'is pronounced', result)
		else:
			print(word,'is not a Hawaiian word')
			return False

		choice=input('Would you like to enter another vowel? (y):')
		if choice=='y' or 'Y':
			words()
		else:
			print("Thank you for using Hawaiian words")
			break

			#Gives choice to repeat the program if needed

		#main function, for recognizing if word inputted is Hawaiian, if yes runs through next functions:

def realword(characters, word):
	for ch in word:
		if characters=='':
			print(ch, 'is not a Hawaiian character')
			return False
	return True

		#Checks for the character to in word to be a valid Hawaiian charater

def Hawaiianword(word):
	result = ''
	x=0

	while x<len(word)-1:
		ch=word[x]

		if ch=='a':
			ch2=word[x+1]
			if ch2=='e' or ch2=='i':
				result=result+"eye-"
				x=x+1
			elif ch2=='o' or ch2=='u':
				result=result+'ow-'
				x=x+1
			else:
				result=result+'ah-'
				x=x+1
		elif ch=='e':
			ch2=word[x+1]

			if ch2=='u':
				result+'eh-oo-'
				x=x+1
			elif ch2=='i':
				result=result+'ay-'
				x=x+1
			else:
				result=result+'eh-'
				x=x+1
		elif ch=='i':
			ch2==word[x+1]
			if ch2=='u':
				result=result+'ew-'
				x=x+1
			else:
				result=result+'ee-'
				x=x+1
		elif ch=='o':
			ch2=word[x+1]

			if ch2=='u':
				result=result+'ow-'
				x=x+1
			elif ch2=='i':
				result=result+'oy-'
				x=x+1
			else:
				result=result+'oh-'
				x=x+1
		elif ch=='u':
			ch2=word[x+1]

			if ch2=='i':
				result=result+'ooey-'
				x=x+1
			else:
				result=result+'oo-'
				x=x+1
		elif ch=='p':
			result=result+'p-'
		elif ch=='k':
			result=result+'k-'
		elif ch=='h':
			result=result+'h-'
		elif ch=='l':
			result=result+'l-'
		elif ch=='m':
			result=result+'m-'
		elif ch=='n':
			result=result+'n-'

	return result

			#For every vowel, recognizes and gives it as a pronounciation and for the following character aswell


introduction()
words()

#running functions




