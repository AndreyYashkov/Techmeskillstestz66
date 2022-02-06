import tkinter as tk
from tkinter import messagebox
win = tk.Tk()
#win.geometry(f'330x380')
win.title('Крестики-Нолики')


def check_win(x_or_o):
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,7],[0,4,8],[6,4,2]]
    for i in win:
        a = set(i)
        b = set(x_or_o)
        if len(a.intersection(b)) == 3:
            messagebox.showinfo("Победа! ", "Игра окончена")

a = 'anything'
list_ofx= []
list_ofo= []
def press(x):
    global a
    if a == 'X':
        a = ('O')
        buttons[x].config(text=a, bg="white",state="disabled")
        list_ofx.append(buttons.index(buttons[x]))
        check_win(list_ofx)

        c = set(list_ofx)
        check_win(c)

        return a
    else:
        a = ('X')
        buttons[x].config(text=a, bg="red", state="disabled")
        list_ofo.append(buttons.index(buttons[x]))
        b = set(list_ofo)
        check_win(b)

        sorted(list_ofo)
        return a




label = tk.Label(width= 10, height = 5, font=('Times New Roman',1,'bold'))

buttons = [tk.Button(width =10,height = 5, font=('Times New Roman',15,'bold'), bg="lightblue", command = lambda x=i: press(x)) for i in range(9)]


label.grid(row=0,column=0,columnspan=3)

row = 1
col = 0
for i in range (9):
    buttons[i].grid(row=row,column = col)
    col +=1
    if col ==3:
        row +=1
        col = 0




win.mainloop()