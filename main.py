#Step 1 
from hangman import logo,stages

word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
random_word = random.choice(word_list)

z=[]
print(random_word)
len_gth = len(random_word)
for i in range(0,len_gth):
  z.append("_ ")
game_over = False
print(z)
count = 0
completed = 0
while not game_over:
  guess_in_word = False
  if count < 7:
    guess = input("Choose a letter: ").lower()
    for i in range (0,len_gth):
      if(guess == random_word[i]):
        guess_in_word = True
        z[i] = guess+" "
        completed = completed + 1
        print(stages[6-count])
        print("yayy! you have guessed a correct letter ", 6-count ," lives left")
        if "_ " not in z:
          print("yayy!, you guessed it right")
          game_over = True
          print("game_over")
    if (not guess_in_word) and  (not game_over):
      count = count + 1
      print(stages[6-count])
      print("you lost one life, you have", 6-count ," lives left")

  else:
    game_over = True
    print("You lost")
  print(z)
    







