from tkinter import *

root = Tk()
MainFrame = Frame(root)
MainFrame.pack(fill= X)
secondframe = Frame(root)
secondframe.pack()


label1 = Label(MainFrame, text= "Mainframe", width= "20", height= "4")
label1.pack(fill= X)


button1 = Button(secondframe, text= "Test", width= "20", height= "4")

root.mainloop()