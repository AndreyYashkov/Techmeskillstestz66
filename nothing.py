import tkinter as tk
win = tk.Tk()
win.geometry(f'330x380')
win.title('Уважаемый калькулятор')

def addnum(digit):
    znachenie = okno.get()+str(digit)
    okno.delete(0,tk.END)
    okno.insert(0,znachenie)

def operaciya(operaciya):
    value = okno.get()
    if value[-1] in "-+/*":
        value = value[:-1]
    okno.delete(0,tk.END)
    okno.insert(0,value+operaciya)

def schitaem():
    value=okno.get()
    okno.delete(0,tk.END)
    okno.insert(0,eval(value))

def chistim():
    okno.delete(0, tk.END)
    okno.insert(0," ")



okno = tk.Entry(win,justify = tk.RIGHT,font=('arial narrow',18,'bold'))
okno.grid(row=0,column=0,columnspan = 5,stick="we",padx=5,pady=5)

tk.Button(text='1',font=('Times New Roman',15,'bold'),command=lambda:addnum(1)).grid(row=1,column=0,padx=9,pady=9,stick="wesn")
tk.Button(text='2',font=('Times New Roman',15,'bold'),command=lambda:addnum(2)).grid(row=1,column=1,padx=9,pady=9,stick="wesn")
tk.Button(text='3',font=('Times New Roman',15,'bold'),command=lambda:addnum(3)).grid(row=1,column=2,padx=9,pady=9,stick="wesn")
tk.Button(text='4',font=('Times New Roman',15,'bold'),command=lambda:addnum(4)).grid(row=2,column=0,padx=9,pady=9,stick="wesn")
tk.Button(text='5',font=('Times New Roman',15,'bold'),command=lambda:addnum(5)).grid(row=2,column=1,padx=9,pady=9,stick="wesn")
tk.Button(text='6',font=('Times New Roman',15,'bold'),command=lambda:addnum(6)).grid(row=2,column=2,padx=9,pady=9,stick="wesn")
tk.Button(text='7',font=('Times New Roman',15,'bold'),command=lambda:addnum(7)).grid(row=3,column=0,padx=9,pady=9,stick="wesn")
tk.Button(text='8',font=('Times New Roman',15,'bold'),command=lambda:addnum(8)).grid(row=3,column=1,padx=9,pady=9,stick="wesn")
tk.Button(text='9',font=('Times New Roman',15,'bold'),command=lambda:addnum(9)).grid(row=3,column=2,padx=9,pady=9,stick="wesn")
tk.Button(text='0',font=('Times New Roman',15,'bold'),command=lambda:addnum(0)).grid(row=4,column=0,stick="wesn",padx=9,pady=9)

tk.Button(text='+',font=('Times New Roman',15,'bold'),command=lambda:operaciya('+')).grid(row=1,column=4,stick="wesn",padx=9,pady=9)
tk.Button(text='-',font=('Times New Roman',15,'bold'),command=lambda:operaciya('-')).grid(row=2,column=4,stick="wesn",padx=9,pady=9)
tk.Button(text='*',font=('Times New Roman',15,'bold'),command=lambda:operaciya('*')).grid(row=3,column=4,stick="wesn",padx=9,pady=9)
tk.Button(text='/',font=('Times New Roman',15,'bold'),command=lambda:operaciya('/')).grid(row=4,column=4,stick="wesn",padx=9,pady=9)

tk.Button(text='C',font=('Times New Roman',15,'bold'),command=lambda:chistim()).grid(row=4,column=2,stick="wesn",padx=9,pady=9)
tk.Button(text='=',font=('Times New Roman',15,'bold'),command=lambda:schitaem()).grid(row=4,column=1,stick="wesn",padx=9,pady=9)

win.grid_columnconfigure(0,minsize=80)
win.grid_columnconfigure(1,minsize=80)
win.grid_columnconfigure(2,minsize=80)
win.grid_columnconfigure(4,minsize=80)
win.grid_rowconfigure(1,minsize=80)
win.grid_rowconfigure(2,minsize=80)
win.grid_rowconfigure(3,minsize=80)
win.grid_rowconfigure(4,minsize=80)

win.mainloop()
