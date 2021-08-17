import re
from tkinter import Tk, Button, Entry, DISABLED, Label, font, END
from functools import partial


def button_to_field(num):
    equation.insert(END, num)


def clear():
    result.delete("0", END) # clear result field
    equation.delete("0", END) # clear equation field


def calculate_result():
    result.delete("0", END) # clear result field
    data = equation.get()
    pattern_char = [r'\D+']
    index_arr = []
    char_arr = []
    num_arr = []
    num = ""

    # find all operations: + - * /
    for p in pattern_char:
        char_arr = re.findall(p, data)
    # insert all numbers to arr
    for i in range(len(data)):
        if data[i].isdigit():
            num += data[i]
        else:
            num_arr.append(num)
            num = ""
    num_arr.append(num)

    result_equation = int(num_arr[0])
    opcnt = 0

    # calculate result
    for j in range(1, len(num_arr)):
        if char_arr[opcnt] == "+":
            result_equation += int(num_arr[j])
            opcnt += 1
        elif char_arr[opcnt] == "-":
            result_equation -= int(num_arr[j])
            opcnt += 1
        elif char_arr[opcnt] == "*":
            result_equation *= int(num_arr[j])
            opcnt += 1
        elif char_arr[opcnt] == "/":
            try:
                result_equation /= int(num_arr[j])
                opcnt += 1
            except:
                print("illegal operation - Error")
            result_equation /= int(num_arr[j])
            opcnt += 1
    print("result = {0}".format(result_equation))
    result.insert(END, str(result_equation))


masterW = Tk()
masterW.title("Calculator")
masterW.geometry("270x300")
masterW.iconbitmap('Calc.ico')
masterW.resizable(False, False)

# buttons font
myFont = font.Font(weight="bold", size=12)

# equation field
equation = Entry(masterW, width="42", bd="3")
equation.place(x=5, y=10)

# result field
result = Entry(masterW, width="20", bd="3")
#state=DISABLED
result.place(x=50, y=35)

# result Label
resLabel = Label(masterW, text="Result:")
resLabel.place(x=4, y=35)

# ######### first buttons line ###########
btn1 = Button(masterW, text="1", width="5", height="2", command=partial(button_to_field, "1"))
btn1.place(x=5, y=65)

btn2 = Button(masterW, text="2", width="5", height="2", command=partial(button_to_field, "2"))
btn2.place(x=70, y=65)

btn3 = Button(masterW, text="3", width="5", height="2", command=partial(button_to_field, "3"))
btn3.place(x=135, y=65)

btnSum = Button(masterW, text="+", width="5", height="2", command=partial(button_to_field, "+"))
btnSum.place(x=200, y=65)

# ######### second buttons line ###########
btn4 = Button(masterW, text="4", width="5", height="2", command=partial(button_to_field, "4"))
btn4.place(x=5, y=122)

btn5 = Button(masterW, text="5", width="5", height="2", command=partial(button_to_field, "5"))
btn5.place(x=70, y=122)

btn6 = Button(masterW, text="6", width="5", height="2", command=partial(button_to_field, "6"))
btn6.place(x=135, y=122)

btnSub = Button(masterW, text="-", width="5", height="2", command=partial(button_to_field, "-"))
btnSub.place(x=200, y=122)

# ######### third buttons line ###########
btn7 = Button(masterW, text="7", width="5", height="2", command=partial(button_to_field, "7"))
btn7.place(x=5, y=179)

btn8 = Button(masterW, text="8", width="5", height="2", command=partial(button_to_field, "8"))
btn8.place(x=70, y=179)

btn9 = Button(masterW, text="9", width="5", height="2", command=partial(button_to_field, "9"))
btn9.place(x=135, y=179)

btnMult = Button(masterW, text="*", width="5", height="2", command=partial(button_to_field, "*"))
btnMult.place(x=200, y=179)

# ######### fourth buttons line ###########
btnClear = Button(masterW, text="clear", width="5", height="2", command=clear)
btnClear.place(x=5, y=236)

btn0 = Button(masterW, text="0", width="5", height="2", command=partial(button_to_field, "0"))
btn0.place(x=70, y=236)

btnEqual = Button(masterW, text="=", width="5", height="2", command=calculate_result)
btnEqual.place(x=135, y=236)

btnDivision = Button(masterW, text="/", width="5", height="2", command=partial(button_to_field, "/"))
btnDivision.place(x=200, y=236)

btn1['font'] = btn2['font'] = btn3['font'] = btn4['font'] = btn5['font'] = btn6['font'] = myFont
btn7['font'] = btn8['font'] = btn9['font'] = btn0['font'] = btnSum['font'] = btnSub['font'] = myFont
btnClear['font'] = btnMult['font'] = btnEqual['font'] = btnDivision['font'] = myFont

masterW.mainloop()
