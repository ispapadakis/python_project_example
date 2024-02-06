# Got Ideas from https://github.com/ShaunHalverson/PythonHangman/blob/main/main.py

import random
    
class Hangman:
    def __init__(self, word):
        self.word = word
        print("Welcome to hangman")
        print("-"*20)

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
            ### Test for Input Format for Errors
            if letterGuessed in current_letters_guessed:
                print("You guessed this letter earlier. Try again.")
                continue
            if len(letterGuessed) > 1:
                print("Guess one letter at a time. Try again.")
                continue
            if not letterGuessed.isalpha():
                print("Your guess needs to be a letter. Try again.")
                continue
            ### Accept Input
            current_letters_guessed.append(letterGuessed.lower())

            ### If Guess is Wrong Increment Error Count
            if letterGuessed not in self.word:
                amount_of_times_wrong += 1

            ### Give Feedback to User
            print("\nLetters guessed so far: ", end="")
            self.printGuesses(current_letters_guessed)
            self.print_hangman(amount_of_times_wrong)
            allGuessesCorrect = self.printWord(current_letters_guessed)

            ### Check if Game is Over
            if amount_of_times_wrong >= 6:
                print("\nYou Lose! Better Luck Next Time.")
                return
            if allGuessesCorrect:
                print("\nCongratulations, You Win!")
                return
        
    def print_hangman(self, wrong):
        if(wrong == 0):
            print("\n+---+")
            print("    |")
            print("    |")
            print("    |")
            print("   ===")
        elif(wrong == 1): 
            print("\n+---+")
            print("O   |")
            print("    |")
            print("    |")
            print("   ===")
        elif(wrong == 2):
            print("\n+---+")
            print("O   |")
            print("|   |")
            print("    |")
            print("   ===")
        elif(wrong == 3):
            print("\n+---+")
            print(" O  |")
            print("/|  |")
            print("    |")
            print("   ===")
        elif(wrong == 4):
            print("\n+---+")
            print(" O  |")
            print("/|\ |")
            print("    |")
            print("   ===")
        elif(wrong == 5):
            print("\n+---+")
            print(" O  |")
            print("/|\ |")
            print("/   |")
            print("   ===")
        elif(wrong == 6):
            print("\n+---+")
            print(" O   |")
            print("/|\  |")
            print("/ \  |")
            print("    ===")

if __name__ == "__main__":
    wordDictionary = ["sunflower", "house", "diamond", "memes","yeet","hello", "howdy", "like", "subscribe"]
    ### Choose a random word
    randomWord = random.choice(wordDictionary)
    game = Hangman(randomWord)
    game.play()