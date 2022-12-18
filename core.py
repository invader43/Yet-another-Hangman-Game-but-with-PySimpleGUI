import numpy as np

#Step 1 

word_list = np.array(["aardvark", "baboon", "camel"])

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word=np.random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
length=len(word)
known=[]
for i in range(length):
    known.append('_')
gameover=False
while(not gameover):
    display=' '
    for i in range(length):
        display+=known[i]
    print(display)
    if not '_' in known:
        gameover=True
        break
    print(' ')
    letter=input()
    for i in range(length):
        if word[i]==letter:
            known[i]=letter





#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.