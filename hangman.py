# main.py
import random
print("Welcome to hangman! You have 15 guesses to figure out the correct word. Good luck!")
#ask player to guess letter and tell how many guesses they have
word = set()
f = open("words.txt")
wordss = f.readlines()
wordss = [x.strip() for x in wordss]
f.close()
num = random.randint(1, len(wordss) -1)
word1 = wordss[num]
#Add word to the set and make the dashes
for i in range(len(word1)):
  word.add(word1[i])
words = ""
for l in range(len(word1)):
  words += ("_")
print(words)
#Set up the guesses variable and start the while true loop
guesses = 15

while True:
  letter = input("Guess a letter! You have " + str(guesses) + " guesses remaining: ")
  guesses = guesses - 1
  if str(letter) in word:
    word.remove(letter)
  
  word3 = ""
  #Add the letters from the set to a string
  words = ""
  print(words)
  for letters in word:
    word3 += letters
  #Check if the words in the set are the words in the word and if they arent, put that letter in the dashes
  for n in range(len(word1)):
    for z in range(len(word3)):
      if str(word1[n]) == str(word3[z]):
        words += "_"
    if str(word1[n]) not in str(word3):
        words += str(word1[n])
  print(words)
  if words == word1:
    print("Congratulations, you win!")
    break
  if guesses == 0:
    print("The word was " + word1)
    print("Sorry you've run out of chances, try again next time")
    break
  
