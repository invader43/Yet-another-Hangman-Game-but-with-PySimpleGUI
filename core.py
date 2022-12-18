import random

word_list = ["aardvark", "baboon", "camel"]

word=random.choice(word_list)
length=len(word)
lives=6
known=[]
for i in range(length):
    known.append('_')
gamewon=False
while(not gamewon):
    display=' '
    for i in range(length):
        display+=known[i]
    print(display)
    print(lives)
    if not '_' in known:
        gamewon=True
        break
    print(' ')
    letter=input()
    letterfound=False
    for i in range(length):
        if word[i]==letter:
            known[i]=letter
            letterfound=True
    if not letterfound:
        lives-=1
    if lives==0:
        break


if gamewon:
    print("you win")
else:
    print("you lose")



