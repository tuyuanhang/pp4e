from tkinter import *

def greeting():
    print('hello stdout world...')

win = Frame()
win.pack()
Label(win, text='Hello Container world').pack(side=TOP)
Button(win, text='Hello',command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()