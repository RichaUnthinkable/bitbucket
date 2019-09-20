'''-------------------Movie guess Game 
	Developer : Richa Gupta
	Created On : Sep 19, 2019
	Modified On : Sep 20, 2019
'''
import random

def edit_movie_name(movieName):
	'''
		This function edit movieName 
		by replacing randomly selected indices 
		with _. 
	'''
	
	EditMovieName = movieName # creating a copy of movieName to edit  
	movieNameLen = len(movieName) #Length of movie string

	k = int(movieNameLen/3) # Getting Number of characters to be removed
	indices = random.sample(list(range(0,movieNameLen)), k) # Generating k random indices
	
	'''Replace characters at generated indices with _'''
	for i in indices:
		EditMovieName = EditMovieName[0:i] + '_' + EditMovieName[i+1:]
	 
	result = [EditMovieName,indices,movieName] 
	return result

def choose_movie():
	'''
		This function select a movie from available movies or movie list
	'''
	movies = ['titanic','avatar','Gladiator','alien','vertigo','gandhi','rocky','jaws','Casablanca','inception','psycho','momento']
	movie = random.choice(movies) #To select a movie from available movie
	return movie.lower() 


def get_movie():
	'''
		This function select a movie from movie dataStore and 
		return an edited movie name with original movie name and modified indexes
	'''
	movieName = choose_movie()
	return edit_movie_name(movieName)

def play() :
	''' 
		Conducts the whole game 
	''' 
		
	'''
		Variables : 

		editedMovieName : Movie Name with blanks. Keeps track of correctly guessed character till the time
		blanks : list of blank indexes in movieName 
		movieName : Original/ Full Movie Name
		guessedMovieName : guessedMovieName keeps the track of movie guessed by user till the time
		guesses : To keep track of wrong inputs/guess
		
	'''
	while 1 == 1 : #Run the game until user quits
		start = input("\n\n\t\t\tDo You wanna Play Movie Guess Game? Press Y ") #get input from user to start/continue the game
		print('\n\n\n')
		start = start.lower()
		if  start != 'y' :  # Stop Game in case user choose not to contine
			break
		selectedMovie = get_movie() # Get a movie from movie dataStores
		editedMovieName = selectedMovie[0]
		blanks = selectedMovie[1]
		blanks.sort()
		movieName = selectedMovie[2] 
		print("\t\t\tYour Movie Name is : ", editedMovieName.upper())	
		
		guessedMovieName = editedMovieName
		guesses = 3 

		for i in blanks :
			while guesses > 0 :
				guessedChar = input("Enter your guess : ") #guessed character entered by user
				
				print("\nYou Guessed : {} ".format(guessedMovieName[0:i] 
								+ guessedChar+'\u0332' 
								+  guessedMovieName[i+1:]).upper()) #Guessed Character will be underlined
				
				guessedMovieName = guessedMovieName[0:i]+guessedChar+guessedMovieName[i+1:] # Create Guessed Movie Name String
				
				if guessedChar == '' or movieName.startswith(guessedMovieName[0:i+1]) == False : # Wrong Guess
					guesses = guesses-1
					if guesses > 0 : #In case or wrong guess check number of remaining attempts
						print("\nWrong Guess, You left with only {} Guesses ".format(guesses))
						print("\n \t\t\tYour Movie Name is : {} .".format(editedMovieName.upper()))	
						continue
					else:
						print("\n\n\n \t\t\t------Sorry! You Loose-------- ")
				else:	#if guessed character is correct
					editedMovieName = guessedMovieName
					print("\nRight Guess. Go Ahead")
					print("\n \t\t\tYour Movie Name is : {} .".format(guessedMovieName).upper())
					break
			else:
				break
		else :	
			if guessedMovieName == movieName :
				print("\n\n\n \t\t\t--------Hurray!!! You win : Movie Name is {}-------".format(guessedMovieName.upper()))


play()


