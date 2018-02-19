from tkinter import *

window =Tk()

#def mpg_calculate():
    #miles = miles_text.get()
    #gallons = gallons_text.get()
    #mpg = miles / gallons
    #b3.insert(mpg)




window.wm_title("MPG Converter")

b1 = Button(window,text="Miles Driven")
b1.grid(row=0,column=0)

miles_text = StringVar()
e1=Entry(window,textvariable="miles")
e1.grid(row=0,column=1)

b2 = Button(window,text="Gallons/Fuel")
b2.grid(row=1,column=0)

gallons_text = StringVar()
e2 = Entry(window,textvariable="gallons_text")
e2.grid(row=1,column=1)

b3 = Button(window,text="Calcualte MPG",command= lambda: action(somenumber))
b3.grid(row=2,column=0)

mpg_text = StringVar()
e2 = Entry(window,textvariable="mpg_text")
e2.grid(row=2,column=1)

window.mainloop()
