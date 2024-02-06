# Got Ideas from https://github.com/ShaunHalverson/PythonHangman/blob/main/main.py

import random
    
class Hangman:
    def __init__(self, word):
        self.word = word
        print("Welcome to hangman")
        print("-"*20)
        # Tuple of Hangman Figures
        self.hangman = (
            """
            +----+  
            |    :
            |   
            |   
            |   
            | 
            ===
            """,
            """
            +----+  
            |    :
            |    O 
            |   
            |   
            | 
            ===
            """,
            """
            +----+  
            |    :
            |    O 
            |   /
            |   
            | 
            ===
            """,
            """
            +----+  
            |    :
            |    O 
            |   /|\ 
            |   
            |
            === 
            """,
            """
            +----+  
            |    :
            |    O 
            |   /|\ 
            |   /
            | 
            ===
            """,
            """
            +----+  
            |    :
            |    O 
            |   /|\ 
            |   / \ 
            | 
            ===
            """
        )

    def printWord(self, guessedLetters):
        allCorrect = True
        for char in self.word:
            if char in guessedLetters:
                print(char, end=" ")
            else:
                print("_", end=" ")
                allCorrect = False
        print()
        return allCorrect

    def printGuesses(self, guess_list):
        print(*guess_list, sep=" ")

    def play(self):
        amount_of_times_wrong = 0
        current_letters_guessed = []
        allGuessesCorrect = False

        while True:
            ### Prompt user for input
            letterGuessed = input("\nGuess a letter: ")
            ### Test for Input Format Errors
            if letterGuessed in current_letters_guessed:
                print("You guessed this letter earlier. Try again.")
                continue
            elif len(letterGuessed) > 1:
                print("Guess one letter at a time. Try again.")
                continue
            elif not letterGuessed.isalpha():
                print("Your guess needs to be a letter. Try again.")
                continue
            else:
                ### Accept Input
                current_letters_guessed.append(letterGuessed.lower())

            ### If Guess is Wrong Increment Error Count
            if letterGuessed not in self.word:
                amount_of_times_wrong += 1

            ### Give Feedback to User
            print("\nLetters guessed so far: ", end="")
            self.printGuesses(current_letters_guessed)
            print(self.hangman[amount_of_times_wrong])
            allGuessesCorrect = self.printWord(current_letters_guessed)

            ### Check if Game is Over
            if amount_of_times_wrong >= len(self.hangman) - 1:
                print("\nYou Lose! Better Luck Next Time.")
                return
            if allGuessesCorrect:
                print("\nCongratulations, You Win!")
                return

if __name__ == "__main__":
    wordDictionary = ["sunflower", "house", "diamond", "memes","yeet","hello", "howdy", "like", "subscribe"]
    ### Choose a random word
    randomWord = random.choice(wordDictionary)
    game = Hangman(randomWord)
    game.play()