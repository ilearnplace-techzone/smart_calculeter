from tkinter import*
from tkinter import messagebox
screen = Tk()
screen.title('My calculator')
screen.configure(bg='blue')

screen.iconbitmap('Calculator-icon.png')

screen.maxsize(width=490,height=500)
screen.minsize(width=343,height=470)

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def cliar():
    global operator
    operator=''
    tex.set(operator)

def equal ():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('notification','Try again something is wrong',parent=screen)

tex = StringVar()
operator = ''

entry1 = Entry(screen,bg='pink',font=('arial',20),bd='20',justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7)
              ,activebackground='green',activeforeground='white')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8)
              ,activebackground='green',activeforeground='white')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9)
              ,activebackground='green',activeforeground='white')
btn9.grid(row=1,column=2)

btnadd =Button(screen,text='+',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+')
               ,activebackground='green',activeforeground='white')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4)
              ,activebackground='green',activeforeground='white')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text='5',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5)
              ,activebackground='green',activeforeground='white')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6)
              ,activebackground='green',activeforeground='white')
btn6.grid(row=2,column=2)

btnsub =Button(screen,text='-',font=('arial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('-')
               ,activebackground='green',activeforeground='white')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1)
              ,activebackground='green',activeforeground='white')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text='2',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2)
              ,activebackground='green',activeforeground='white')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text='3',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3)
              ,activebackground='green',activeforeground='white')
btn3.grid(row=3,column=2)

btnmul =Button(screen,text='*',font=('arial',20,'italic bold'),bd=8,padx=17,pady=16,command=lambda:click('*')
               ,activebackground='green',activeforeground='white')
btnmul.grid(row=3,column=3)

btnequal = Button(screen,text='=',font=('arial',20,'italic bold'),bd=8,padx=15,pady=16,command=equal
                  ,activebackground='green',activeforeground='white')
btnequal.grid(row=4,column=0)

btnzero = Button(screen,text='0',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0)
                 ,activebackground='green',activeforeground='white')
btnzero.grid(row=4,column=1)

btnclear = Button(screen,text='c',font=('arial',20,'italic bold'),bd=8,padx=16,pady=16,command=cliar
                  ,activebackground='green',activeforeground='white')
btnclear.grid(row=4,column=2)

btndiv =Button(screen,text='/',font=('arial',20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('/')
               ,activebackground='green',activeforeground='white')
btndiv.grid(row=4,column=3)


screen.mainloop()