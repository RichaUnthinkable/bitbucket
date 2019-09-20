import random

def edit_movie_name(movieName):
	oMovieName = movieName
	movieNameLen = len(movieName)
	k = int(movieNameLen/3) # Getting Number of characters to be removed
	indices = random.sample(list(range(0,movieNameLen)), k) # Generating k random indices
	movieNameList = list(oMovieName)
	
	for i in indices:
		movieName = movieName[0:i] + '_' + movieName[i+1:] 
	result = [movieName , indices, oMovieName]
	return result


def choose_movie():
	words = ['titanic','avatar','Gladiator','alien','vertigo','gandhi','rocky','jaws','Casablanca','inception','psycho','momento']
	movie = random.choice(words)
	return movie.lower()

def get_movie():
	movieName = choose_movie()
	return edit_movie_name(movieName)

def play() :
	
	while 1 == 1 :
		start = input("\n\n\t\t\tDo You wanna Play Movie Guess Game? Press Y ")
		print('\n\n\n')
		start = start.lower()
		if  start != 'y' :
			break;
		selectedMovie = get_movie();
		movieName = selectedMovie[0]
		indices = selectedMovie[1]
		oMovieName = selectedMovie[2]
		print("\t\t\tYour Movie Name is : " ,movieName.upper())	
		
		guessedMovieName = movieName
		
		indices.sort()
		guesses = 3
		for i in indices:
			while guesses :
				guessedChar = input("Enter your guess : ")
				
				print("\nYou Guessed : {} ".format(guessedMovieName[0:i] + guessedChar+'\u0332' +  guessedMovieName[i+1:]).upper())
				guessedMovieName = guessedMovieName[0:i] + guessedChar +  guessedMovieName[i+1:]
				
				if oMovieName.startswith(guessedMovieName[0:i+1]) == False :
					guesses = guesses-1 
					if guesses > 0 :
						print("\nWrong Guess, You left with only {} Guesses ".format(guesses))
						print("\n \t\t\tYour Movie Name is : {} .".format(movieName.upper()))	
						continue
					else:
						print("\n\n\n \t\t\tYou Loose ")
				else:	
					movieName = guessedMovieName
					print("\nRight Guess. Go Ahead")
					print("\n \t\t\tYour Movie Name is : {} .".format(guessedMovieName).upper())
					break
			else:
				break
		else :
			print("\n\n\n \t\t\tYou win : Movie Name is {}".format(guessedMovieName.upper()))


play()


