import sys
from tkinter import *
from tkinter.messagebox import showinfo

class GuiMaker(Frame):
    menuBar = []
    toolBar = []
    helpButton = True

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.start()
        self.makeMenuBar()
        self.makeToolBar()
        self.makeWidgets()

    def makeMenuBar(self):
        """
        在顶部创建菜单栏,expand=no, fill=x,调整时保持宽带一致
        """
        menubar = Frame(self, relief=RAISED, bd=2)
        menubar.pack(side=TOP, fill=X)

        for (name, key, items) in self.menuBar:
            mbutton = Menubutton(menubar, text=name, underline=key)
            mbutton.pack(side=LEFT)
            publldown = Menu(mbutton)
            self.addMenuItems(pulldown, items)
            mbutton.config(menu=publldown)

        if self.helpButton:
            Button(menubar, text='Help',
                            cursor = 'gumby',
                            relief = FLAT,
                            command = self.help).pack(side=RIGHT)

    def addMenuItems(self, menu, items):
        for item in items:
            if item == 'separator':
                menu.add_separator({})
            elif type(item) == list:
                for num in item:
                    menu.entryconfig(num, state=DISABLED)
            elif type(item[2]) != list:
                menu.add_command(label = item[0],
                                underline = item[1],
                                command = item[2])
            else:
                pullover = Menu(menu)
                self.addMenuItems(pullover, item[2])
                menu.add_cascade(label = item[0],
                                 underline = item[1],
                                 menu = pullover)

    def makeToolBar(self):
        name = Label(self,
                     width=40, height=10,
                     relief=SUNKEN, bg='white',
                     text = self.__class__.__name__,
                     cursor = 'crosshair')
        name.pack(expand=YES, fill=BOTH, side=TOP)

    def help(self):
        showinfo('Help', 'Sorry, no help for' + self.__class__.__name__)

    def start(self):
        pass

#TK 8.0 
GuiMakerFrameMenu = GuiMaker  #用于嵌入式组件菜单

class GuiMakerWindowMenu(GuiMaker):
    def makeMenuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        for (name, key, items) in self.menuBar:
            pulldown = Menu(menubar)
            self.addMenuItems(pulldown, items)
            menubar.add_cascade(label=name, underline=key, menu=pulldown)

        if self.helpButton:
            if sys.platform[:3] == 'win':
                menubar.add_command(label='Help', command=self.help)
        else:
            pulldown = Menu(menubar)
            pulldown.add_command(label='About', command=self.help)
            menubar.add_cascade(label='Help', menu=pulldown)

if __name__ == '__main__':
    from guimixin import GuiMixin

    menuBar = [
        ('File', 0, 
            [('Open', 0, lambda:0),
             ('Quit', 0, sys.exit)]),
        ('Edit', 0,
            [('Cut', 0, lambda:0),
            ('Paste', 0, lambda:0)])]

    toolBar = [('Quit', sys.exit, {'side':LEFT})]

    class TestAppFrameMenu(GuiMixin, GuiMakerFrameMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar

    class TestAppWindowMenu(GuiMixin, GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar

    class TestAppWindowMenuBasic(GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar

root = Tk()
TestAppFrameMenu(Toplevel())
TestAppWindowMenu(Toplevel())
TestAppWindowMenuBasic(root)
root.mainloop()