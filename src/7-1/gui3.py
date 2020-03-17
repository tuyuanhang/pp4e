import sys
from tkinter import *

def quit():
    print('hello, i must be going...')
    sys.exit()

widget = Button(None, text='Hello event world', command=quit)
widget.pack()
widget.mainloop()