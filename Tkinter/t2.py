""" from tkinter import *

window = Tk()

window.geometry("420x420")
window.title("INsaan")

window.config(background="black")

photo = PhotoImage()

label = Label(
    window, text="Hello world", 
    font=('Arial',40, 'bold'), 
    fg='white', 
    bg='black',
    relief=RAISED,
    padx=20,
    pady=20
    )
label.pack()

window.mainloop() """

from tkinter import *
window =  Tk()

window.geometry('540x540')

window.title("Login form")

""" window.config(background='black')

def click():
    username = entry.get()
    pas = entry_password.get()
    print(username)
    print(pas)

login = Label(
    window,
    text="login = ",
    font=("monospace", 10 , 'bold'),

    fg='white',
    bg='black',
)

password = Label(
    window,
    text="Password = ",
    font=('monospace',10,'bold'),
    fg='white',
    bg='black'
)

but = Button(window, text="submit", command=click)

entry = Entry(window,
              font=('monospace',10, 'bold'),
              fg='black')

entry_password = Entry(window,
                       font=('monospace',10,'bold'),
                       fg='black',
                       show="*")

login.grid(row=0, column=0)
entry.grid(row=0, column=1)

password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)

but.grid(row=2, columnspan=2)



#checkbox
x = IntVar()

def display():
    if(x.get() == 1):
        print("hii")
    else:
        print("bye")

check_butt = Checkbutton(window,
                         text="I am smart",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display)

check_butt.grid(row=3)


 """

#radio button 

food = ['pizza','ham' ,'rpti']

for index in range(len(food)):
    radiobutton = Radiobutton(window, text=food[index])
    radiobutton.pack()

window.mainloop()