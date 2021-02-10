import PySimpleGUI as sg

this = ""

layout = [
    [
        sg.Text(text = this, key = '-INPUT-', size=(28,1), background_color= "white", text_color="black", font=('Helvetica', 15)),
    ],
    [
        sg.Button("1", key = '1', size=(4,2)),sg.Button("2", key = '2', size=(4,2)),sg.Button("3", key = '3', size=(4,2)),sg.VerticalSeparator(),sg.Button("+", key = '+', size=(4,2)),sg.Button("-", key = '-', size=(4,2)),sg.Button("CE", key = 'CE', size=(4,2)),
    ],
    [
        sg.Button("4", key = '4', size=(4,2)),sg.Button("5", key = '5', size=(4,2)),sg.Button("6", key = '6', size=(4,2)),sg.VerticalSeparator(),sg.Button("x", key = 'x', size=(4,2)),sg.Button("/", key = '/', size=(4,2)),sg.Button("AC", key = 'AC', size=(4,2)),
    ],
    [
        sg.Button("7", key = '7', size=(4,2)),sg.Button("8", key = '8', size=(4,2)),sg.Button("9", key = '9', size=(4,2)),sg.VerticalSeparator(),sg.Button("(", key = '(', size=(4,2)),sg.Button(")", key = ')', size=(4,2)),sg.Button("=", key = '=', size=(4,2)),
    ],
    [
        sg.Button(",", key = ',', size=(4,2), disabled = True),sg.Button("0", key = '0', size=(4,2))
    ],
]

window = sg.Window('CALCULATOR', layout)

def one():
    text = window['-INPUT-']
    global this 
    this = this + "1"
    text.update(this)

def two():
    text = window['-INPUT-']
    global this 
    this = this + "2"
    text.update(this)

def three():
    text = window['-INPUT-']
    global this 
    this = this + "3"
    text.update(this)

def four():
    text = window['-INPUT-']
    global this 
    this = this + "4"
    text.update(this)

def five():
    text = window['-INPUT-']
    global this 
    this = this + "5"
    text.update(this)

def six():
    text = window['-INPUT-']
    global this 
    this = this + "6"
    text.update(this)

def seven():
    text = window['-INPUT-']
    global this 
    this = this + "7"
    text.update(this)

def eight():
    text = window['-INPUT-']
    global this 
    this = this + "8"
    text.update(this)

def nine():
    text = window['-INPUT-']
    global this 
    this = this + "9"
    text.update(this)

def zero():
    text = window['-INPUT-']
    global this 
    this = this + "0"
    text.update(this)

def comma():
    text = window['-INPUT-']
    global this 
    this = this + ","
    text.update(this)

def delete():
    text = window['-INPUT-']
    global this
    thisList = list(this)
    thisList.pop()
    this = ''.join(map(str, thisList))
    if len(this) == 0:
        this == ""
    text.update(this)

def deleteAll():
    text = window['-INPUT-']
    global this 
    this = ""
    text.update(this)

def plus():
    text = window['-INPUT-']
    global this 
    this = this + "+"
    text.update(this)

def minus():
    text = window['-INPUT-']
    global this 
    this = this + "-"
    text.update(this)

def divide():
    text = window['-INPUT-']
    global this 
    this = this + "/"
    text.update(this)

def times():
    text = window['-INPUT-']
    global this 
    this = this + "x"
    text.update(this)

def openP():
    text = window['-INPUT-']
    global this 
    this = this + "("
    text.update(this)

def closeP():
    text = window['-INPUT-']
    global this 
    this = this + ")"
    text.update(this)

def calculate():
    text = window['-INPUT-']
    global this 
    this = this + "="
    text.update(this)

#checks when Comma is allowed
def checkComma():
    global this
    thisList = list(this)
    lastIndex = len(this) - 1
    print(thisList)
    

def checkText():
    checkComma()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    elif event == '1':
        one()
    elif event == '2':
        two()
    elif event == '3':
        three()
    elif event == '4':
        four()
    elif event == '5':
        five()
    elif event == '6':
        six()
    elif event == '7':
        seven()
    elif event == '8':
        eight()
    elif event == '9':
        nine()
    elif event == '0':
        zero()
    elif event == ',':
        comma()
    elif event == 'CE':
        delete()
    elif event == 'AC':
        deleteAll()
    elif event == '+':
        plus()
    elif event == '-':
        minus()
    elif event == '/':
        divide()
    elif event == 'x':
        times()
    elif event == '(':
        openP()
    elif event == ')':
        closeP()
    elif event == '=':
        calculate()
    checkText()

window.close()