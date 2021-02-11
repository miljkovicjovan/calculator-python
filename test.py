import PySimpleGUI as sg

this = ""

layout = [
    [
        sg.Text(text = this, key = '-INPUT-', size=(28,1), background_color= "white", text_color="black", font=('Helvetica', 15)),
    ],
    [
        sg.Button("1", key = '1', size=(4,2)),sg.Button("2", key = '2', size=(4,2)),sg.Button("3", key = '3', size=(4,2)),sg.VerticalSeparator(),sg.Button("+", key = '+', size=(4,2), disabled = True),sg.Button("-", key = '-', size=(4,2), disabled = True),sg.Button("CE", key = 'CE', size=(4,2), disabled = True),
    ],
    [
        sg.Button("4", key = '4', size=(4,2)),sg.Button("5", key = '5', size=(4,2)),sg.Button("6", key = '6', size=(4,2)),sg.VerticalSeparator(),sg.Button("*", key = '*', size=(4,2), disabled = True),sg.Button("/", key = '/', size=(4,2), disabled = True),sg.Button("AC", key = 'AC', size=(4,2), disabled = True),
    ],
    [
        sg.Button("7", key = '7', size=(4,2)),sg.Button("8", key = '8', size=(4,2)),sg.Button("9", key = '9', size=(4,2)),sg.VerticalSeparator(),sg.Button("=", key = '=', size=(4,2), disabled = True),
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
    this = this + "*"
    text.update(this)

def calculate():
    text = window['-INPUT-']
    global this
    calculateOutput(this)

#checks when Comma symbol is allowed
def checkComma():
    global this
    thisList = list(this)
    index = len(this) - 1
    if "," in this:
        window[','].update(disabled = True)
    else:
        window[','].update(disabled = False)

    if bool(this) == False:
        window[','].update(disabled = True)    
    elif bool(this) == True and thisList[index] == "+":
        window[','].update(disabled = True)
    elif bool(this) == True and thisList[index] == "-":
        window[','].update(disabled = True)
    elif bool(this) == True and thisList[index] == "*":
        window[','].update(disabled = True)
    elif bool(this) == True and thisList[index] == "/":
        window[','].update(disabled = True)

#checks when Plus symbol is allowed
def checkPlusMinusTimes():
    global this
    thisList = list(this)
    index = len(this) - 1

    if bool(this) == False:
        window['+'].update(disabled = True) 
        window['*'].update(disabled = True)
        window['/'].update(disabled = True) 
        window['-'].update(disabled = True) 
    elif bool(this) == True and thisList[index] == "+":
        window['+'].update(disabled = True)
        window['-'].update(disabled = True)
        window['*'].update(disabled = True)
        window['/'].update(disabled = True)
    elif bool(this) == True and thisList[index] == "-":
        window['+'].update(disabled = True)
        window['-'].update(disabled = True)
        window['*'].update(disabled = True)
        window['/'].update(disabled = True)
    elif bool(this) == True and thisList[index] == ",":
        window['+'].update(disabled = True)
        window['-'].update(disabled = True)
        window['*'].update(disabled = True)
        window['/'].update(disabled = True)
    elif bool(this) == True and thisList[index] == "*":
        window['+'].update(disabled = True)
        window['-'].update(disabled = True)
        window['*'].update(disabled = True)
        window['/'].update(disabled = True)
    elif bool(this) == True and thisList[index] == "/":
        window['+'].update(disabled = True)
        window['-'].update(disabled = True)
        window['*'].update(disabled = True)
        window['/'].update(disabled = True)
    else:
        window['+'].update(disabled = False)
        window['-'].update(disabled = False)
        window['*'].update(disabled = False)
        window['/'].update(disabled = False)

def checkDelete():
    global this
    if bool(this) == True:
        window['CE'].update(disabled = False)
        window['AC'].update(disabled = False)
    else:
        window['CE'].update(disabled = True)
        window['AC'].update(disabled = True)

def checkCalculate():
    global this
    thisList = list(this)
    index = len(this) - 1
    if bool(this) == True and "+" in this and thisList[index] == "0":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "0":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "0":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "0":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "1":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "1":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "1":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "1":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "2":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "2":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "2":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "2":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "3":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "3":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "3":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "3":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "4":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "4":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "4":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "4":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "5":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "5":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "5":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "5":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "6":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "6":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "6":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "6":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "7":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "7":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "7":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "7":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "8":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "8":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "8":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "8":
        window['='].update(disabled = False)
    elif bool(this) == True and "+" in this and thisList[index] == "9":
        window['='].update(disabled = False)
    elif bool(this) == True and "-" in this and thisList[index] == "9":
        window['='].update(disabled = False)
    elif bool(this) == True and "*" in this and thisList[index] == "9":
        window['='].update(disabled = False)
    elif bool(this) == True and "/" in this and thisList[index] == "9":
        window['='].update(disabled = False)
    else:
        window['='].update(disabled = True)    

def checkLimit():
    global this
    if len(this) >= 27:
        sg.popup("Maximum length allowed is 27!!", title = "Too many characters!")

def checkText():
    checkComma()
    checkPlusMinusTimes()
    checkDelete()
    checkCalculate()
    checkLimit()

def calculateOutput(x):
    text = window['-INPUT-']
    this = eval(x)
    text.update(this)

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
    elif event == '*':
        times()
    elif event == '=':
        calculate()
    checkText()

window.close()