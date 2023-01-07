import PySimpleGUI as sg
import random
state = 1 
lives = 6
word_list = ["aardvark", "baboon", "camel"]
known=[]
word=random.choice(word_list)
length=len(word)
for i in range(length):
    known.append('_ ')
display=' '
for i in range(length):
    display+=known[i]

gamewon=False
image = str(state) + '.png'

col1 = [[sg.Image(str(state) + '.png',key='image1')]]
col2 = [
    [sg.Text(display,key='display')],
    [sg.Input(key = 'text1'),sg.Button('Submit', font=('Times New Roman',12))]
    ]

layout = [
    [sg.Column(col1, element_justification='c' ),
    sg.Column(col2, element_justification='c')]
    ]
window = sg.Window("Calculator", layout)
gamewon=False
# Event loop
while True:
    event, values = window.read()






    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':# If submit button is clicked display chosen values
        #first check the text box for the text in it and take it as input 
        letter = values['text1']
        letterfound=False
        for i in range(length):
            if word[i]==letter:
                known[i]=letter
                letterfound=True
        if not letterfound:
            lives-=1
            state+=1
        display=' '
        for i in range(length):
            display+=known[i]+' '
        
        
        image = str(state) + '.png'
        window['image1'].update(str(state) + '.png')
        window['display'].update(display)
        window['text1'].update('')





        
window.close()
