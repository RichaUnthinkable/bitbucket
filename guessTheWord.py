import random

def edit_movie_name(movieName):
	oMovieName = movieName
	movieNameLen = len(movieName)
	#print("movieNameLen : " , movieNameLen)
	k = int(movieNameLen/3)
	indices = random.sample(list(range(0,movieNameLen)), k)
	#print("indices : " ,indices )
	movieNameList = list(oMovieName)
	
	for i in indices:
		movieNameList[i] = '_' 
	movieName = "".join(movieNameList)
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
		start = input("Do You wanna Play Movie Guess Game? Press Y ")
		start = start.lower()
		if  start != 'y' :
			break;
		selectedMovie = get_movie();
		movieName = selectedMovie[0]
		indices = selectedMovie[1]
		oMovieName = selectedMovie[2]
		print(movieName)	
		
		guessedMovieName = list(movieName)
		indices.sort()
		for i in indices:
			guesses = 3
			while guesses :
				guessedChar = input("Enter your guess : ")
				guessedMovieName[i] = guessedChar
				if oMovieName.startswith("".join(guessedMovieName[0:i+1])) == False :
					guesses = guesses-1 
					if guesses > 0 :
						print("Wrong Guess, You left with only {} Guesses ".format(guesses))
						continue
					else:
						print("You Loose ")
				
				else:
					print("Right Guess. Go Ahead")
					break
			else:
				break
		else :
			print("You win : Movie Name is {}".format("".join(guessedMovieName).upper()))


play()


