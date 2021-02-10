import PySimpleGUI as sg

this = ""

layout = [
    [
        sg.Text(text = this, key = '-INPUT-', size=(28,1), background_color= "white", text_color="black", font=('Helvetica', 15)),
    ],
    [
        sg.Button("1", key = '1', size=(4,2)),sg.Button("2", key = '2', size=(4,2)),sg.Button("3", key = '3', size=(4,2)),sg.VerticalSeparator(),sg.Button("+", key = '+', size=(4,2)),sg.Button("-", key = '-', size=(4,2)),sg.Button("CE", key = 'CE', size=(4,2), disabled = True),
    ],
    [
        sg.Button("4", key = '4', size=(4,2)),sg.Button("5", key = '5', size=(4,2)),sg.Button("6", key = '6', size=(4,2)),sg.VerticalSeparator(),sg.Button("x", key = 'x', size=(4,2), disabled = True),sg.Button("/", key = '/', size=(4,2), disabled = True),sg.Button("AC", key = 'AC', size=(4,2), disabled = True),
    ],
    [
        sg.Button("7", key = '7', size=(4,2)),sg.Button("8", key = '8', size=(4,2)),sg.Button("9", key = '9', size=(4,2)),sg.VerticalSeparator(),sg.Button("(", key = '(', size=(4,2)),sg.Button(")", key = ')', size=(4,2)),sg.Button("=", key = '=', size=(4,2), disabled = True),
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

def checkText():
    global this
    thisList = list(this)
    lastIndex = len(this) - 1
    if this == "":
        window['CE'].update(disabled = True)
        window['AC'].update(disabled = True)
        window['x'].update(disabled = True)
        window['/'].update(disabled = True)
    if thisList[lastIndex] == "-" or "+" or "x" or "/":
        window['-'].update(disabled = True)
        window['+'].update(disabled = True)
        window['x'].update(disabled = True)
        window['/'].update(disabled = True)
        window[','].update(disabled = True)
    else:
        window['-'].update(disabled = False)
        window['+'].update(disabled = False)
        window['x'].update(disabled = False)
        window['/'].update(disabled = False)
        window[','].update(disabled = False)

    if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "-" or "+" or "(" or ")" in this:
        window['CE'].update(disabled = False)
        window['AC'].update(disabled = False)
        window['x'].update(disabled = False)
        window['/'].update(disabled = False)
        if "," in this:
            window[','].update(disabled = True)
        else:
            window[','].update(disabled = False)
    

while True:
    event, values = window.read()
    checkText()
    if event == sg.WIN_CLOSED :
        break
    elif event == '1':
        one()
        checkText()
    elif event == '2':
        two()
        checkText()
    elif event == '3':
        three()
        checkText()
    elif event == '4':
        four()
        checkText()
    elif event == '5':
        five()
        checkText()
    elif event == '6':
        six()
        checkText()
    elif event == '7':
        seven()
        checkText()
    elif event == '8':
        eight()
        checkText()
    elif event == '9':
        nine()
        checkText()
    elif event == '0':
        zero()
        checkText()
    elif event == ',':
        comma()
        checkText()
    elif event == 'CE':
        delete()
        checkText()
    elif event == 'AC':
        deleteAll()
        checkText()
    elif event == '+':
        plus()
        checkText()
    elif event == '-':
        minus()
        checkText()
    elif event == '/':
        divide()
        checkText()
    elif event == 'x':
        times()
        checkText()
    elif event == '(':
        openP()
        checkText()
    elif event == ')':
        closeP()
        checkText()
    elif event == '=':
        calculate()

window.close()