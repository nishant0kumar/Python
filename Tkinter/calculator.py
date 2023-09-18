from tkinter import *

window = Tk()

#window.geometry('420x420')

    

display = Entry(window, width=20,borderwidth= 10,font='bold')

button1 = Button(window,padx=30, pady=20, text="1" )
button2 = Button(window,padx=30, pady=20, text="2" )
button3 = Button(window,padx=30, pady=20, text="3" )
button4 = Button(window,padx=30, pady=20, text="4" )
button5 = Button(window,padx=30, pady=20, text="5" )
button6 = Button(window,padx=30, pady=20, text="6" )
button7 = Button(window,padx=30, pady=20, text="7" )
button8 = Button(window,padx=30, pady=20, text="8" )
button9 = Button(window,padx=30, pady=20, text="9" )

button0 = Button(window,padx=110, pady=20, text="0" )

buttonad = Button(window, padx=40, pady=50, text="+")
buttonclear = Button(window, padx=30, pady=20, text="clear")
buttonenter = Button(window, padx=30, pady=50, text="enter")


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button0.grid(row=4,columnspan=3)

buttonad.grid(row=1,rowspan=2, column=3)
buttonenter.grid(row=3, rowspan=2, column=3)
buttonclear.grid(row=0, column=3)


display.grid(row=0, columnspan=3)

window.mainloop()