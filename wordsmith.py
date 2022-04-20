import random
import time
# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()
#Make the beggining statment
game = input("Welcome to Wordsmith! In this game, come up with as many words as you can using the 7 letters you are given. Press Enter to begin!")
#Print the ready set go with the sleep command
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Go!")
#Make the loop which adds 7 random letters to a list and there are no multiples
randletters = []
while True:
  letters = random.randint(97, 122)
  if chr(letters) not in randletters:
    randletters.append(chr(letters))
  if len(randletters) == 7:
    break
print("Your random letters are: ")
print(randletters)
score = int(0)
#Make the while true loop for entering a word and seeing if it is valid
start = time.time()
usedWords = set()
while True:
  p = 0
  l = 0
  finish = time.time()
  #make an if statement to see if it has been more than __ seconds
  if finish - start > int(90):
    print("\nYou ran out of time! Your final score was " + str(score) + "!")
    break
  word = input("\nEnter a word: ")
  #Make the many if statements for if the word is in validwords, if it used or if it uses letters other than the ones in the list
  if word in validWords:
    if word not in usedWords:
      for i in range(len(word)):
        if word[i] not in randletters:
          p = p + 1
          if p > 0:
            print("You can only use the 7 letters you were given! ")
      for m in range(len(word)):
        if word[m] in randletters:
          l = l + 1 
          if l == len(word):
            score = score + int(len(word))
            print("Valid Word! Your Score: " + str(score))
            usedWords.add(word)
    elif word in usedWords:
      print("You already entered this word! Your score: " + str(score))
  elif word not in validWords:
    print("Invalid Word! Your score: " + str(score))
  finish = time.time()
  #make an if statement to see if it has been more than __ seconds
  if finish - start > int(10):
    print("\nYou ran out of time! Your final score was " + str(score) + "!")
    break
