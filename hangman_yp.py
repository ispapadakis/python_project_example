# Got Ideas from https://github.com/ShaunHalverson/PythonHangman/blob/main/main.py


import random
wordDictionary = ["sunflower", "house", "diamond", "memes","yeet","hello", "howdy", "like", "subscribe"]
### Choose a random word
randomWord = random.choice(wordDictionary)


def print_hangman(wrong):
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

def printGuesses(guess_list):
  print(*guess_list, sep=" ")
    
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

  def play(self):
    amount_of_times_wrong = 0
    current_letters_guessed = []
    allGuessesCorrect = False

    while(amount_of_times_wrong < 6 and not allGuessesCorrect):
      ### Prompt user for input
      letterGuessed = input("\nGuess a letter: ")
      current_letters_guessed.append(letterGuessed)
      print("\nLetters guessed so far: ")
      printGuesses(current_letters_guessed)
      if letterGuessed in self.word:
        ### User is Right
        ### Update the drawing and Print Word
        print_hangman(amount_of_times_wrong)
        allGuessesCorrect = self.printWord(current_letters_guessed)
      else:
        ### User is Wrong
        amount_of_times_wrong+=1
        ### Update the drawing and Print Word
        print_hangman(amount_of_times_wrong)
        allGuessesCorrect = self.printWord(current_letters_guessed)

    if allGuessesCorrect:
      print("\nCongratulations, You Win!")
    else:
        print("\nYou Lose! Better Luck Next Time.")

game = Hangman(randomWord)
game.play()