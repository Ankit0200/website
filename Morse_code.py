### MORSE code converter
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.'
}

import tkinter
from tkinter import *

window =tkinter.Tk()
window.configure(border=4)
window.title('MORSE CODE CONVERTER')

def convert():
    my_morse=[]
    Morse_code.delete(1.0,END)
    Entered_Text = user_text.get('1.0', 'end-1c').upper()
    for char in Entered_Text:
        if char=="":
            my_morse.append("")
        else:
            for data in morse_code:
                if data==char:
                    my_morse.append(morse_code[data])

    Morse_code.insert(END, my_morse)



window.geometry('800x600+600+150')

# My_frame=tkinter.Frame(window,bd=4,relief=RIDGE,bg='lightyellow')
# My_frame.place(x=150,y=80,width=500,height=450)

user_txt_lbl=Label(window,font=(
    'Times New Roman',20,"bold"),fg='black',text='Enter your message')
user_txt_lbl.place(x=100,y=50)

user_text =Text(window,width=60, height=7,bd=2, relief=RIDGE,font=("Times New Roman",15))
user_text.place(x=100,y=100)


Morse_code_lbl=Label(window,font=(
    'Times New Roman',20,"bold"),fg='black',text='Morse Code')
Morse_code_lbl.place(x=100,y=280)

Morse_code =Text(window,width=60, height=7,bd=2, relief=RIDGE,font=("Times New Roman",15))
Morse_code.place(x=100,y=320)


Btn_convert=Button(window,text='Convert',font=('Times New Roman',15,'bold'),command=convert,bg='green',fg='black')
Btn_convert.place(x=600,y=270)





window.mainloop()
