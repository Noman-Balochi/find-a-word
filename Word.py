
from tkinter import *
# from tkinter.ttk import *
from PIL import ImageTk, Image
from lipword import *

# premierleague
root = Tk()
root.title("Find a Word")
root.geometry("800x500")
root.resizable(False,False)

# main frame #379b9e 
mainframe = Frame(root, height=360, width=800, bg=mainframeColor )
mainframe.place(x=0,y=102)

##################### this is header ###################### 
mainframeColor = '#379b9e'

img_path = "G:\\python tutorials\\find word\\projectWord\\button-1.png"
header(root,img_path)

#################### main Frame ##########################

stratTab(mainframe)

############### footer frame ##################
footerframe = Frame(root, height=40, width=800, bg='#25344d')
footerframe.place(x=0,y=460)

Label(footerframe , text="Copyright | Noman 2021",bg='#25344d',fg="white", font=("Times","14","bold")).place(x=300,y=0)

root.mainloop()