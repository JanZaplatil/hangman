
import random
from wordlist import words



word = random.choice(words)
while "-" in word or " " in word:
    word = random.choice(words) 



guessess = ""
usedWords = []
tries = 10 

while tries > 0:
    for letter in word:
        if letter in guessess:
            print(letter)
        else:
            print("X")
    guess = input ("Enter a letter: ")
    guessess += guess
    if guess not in word:
        tries -= 1
        print(" You have " + str(tries) + " tries left ! ")
    usedWords.append(guess)
    print(usedWords)


