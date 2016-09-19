# name : Ya Nan Tong
# student ID: 1432469

# Add the ¡°Hangman¡± graphic to your code. It might be a good idea to store the individual lines of the 
# graphics as strings in some list. Then you could just output as many as lines as you need from this list. 

# Error handling 1
def is_valid_cho_word():
    is_valid = True
    while is_valid == True:
        cho_word = input("Please enter an integer number (0<= number <10) to choose the word in the list: ")
        is_valid = False
        try:
            if (cho_word == ""):
                print("Empty input!")
                is_valid = True
                
            elif (int(cho_word)>=10):
                print("Index is out of range!")
                is_valid = True
       
        except ValueError:
            print("Input must be an interger!")
            is_valid = True
    return cho_word

# Error handling 2
def is_value_letter():
    is_valid = True
    while is_valid == True:
        guess = input("Please enter the letter you guess: ")
        is_valid = False
        if guess.isalpha()==False:
            print("You need to input a single alphabetic character!")
            is_valid = True
        elif (len(guess) > 1):
            print("You need to input a single alphabetuc character!")
            is_valid = True
    return guess

      
# store the build list and graph
words=['cow','horse','deer','elephant','lion','tiger','baboon','donkey','fox','giraffe'] 
graph= [" ------------- ", " |         |   ", " |          O  ", " |         / | ", " |          |  ", " |         / | ", " |             ", " |             "]

# welcome the user and let them choose a word
print("welcome to Hangman! Guess the mystery word with less than 6 mistakes!")
cho_word = is_valid_cho_word()

# find the legth of the word
length = len(words[int(cho_word)])
word = words[int(cho_word)]
print("The length of the word is:", length)

max_count = 6
count = 0
guesslist = ["_"] * length
test = ""

# user only can enter 6 mistake letters
while (count < max_count) and (test != word):
    print()
    guess = is_value_letter()
    #check if the guess is the letter in the word
    # guess is the letter in the word
    if guess in word:
        print("The letter is in the word.")
        for i in range(len(word)):
            if word[i] == guess:
                guesslist[i]=guess
                test="".join(guesslist)
        print("Letters matched so far:", test)
        
        
    # guess is not the letter in the word            
    else:
        print("The letter is not in the word.")
        test="".join(guesslist)
        print("letters matched so far:", test)
        if count == 0:
            print(graph[0])
        elif count == 1:
            print(graph[0])
            print(graph[1]) 
        elif count == 2:
            print(graph[0])
            print(graph[1])
            print(graph[2])
        elif count == 3:
            print(graph[0])
            print(graph[1])
            print(graph[2])
            print(graph[3])
        elif count == 4:
            print(graph[0])
            print(graph[1])
            print(graph[2])
            print(graph[3])
            print(graph[4])
        else:
            print(graph[0])
            print(graph[1])
            print(graph[2])
            print(graph[3])
            print(graph[4])
            print(graph[5])
            print(graph[6])
            print(graph[7])
    
        count = count +1   
        
# print the result
if (test != word) and (count >= max_count):
    print()
    print("Too many incorrect guesses. You lost!")
    print("The word was:", word)
else:
    print("You have found the mystery word. You win!")
print("Goodbye!")
 