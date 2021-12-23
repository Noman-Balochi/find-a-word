from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

mainframeColor = '#379b9e'



def header(root,img_path):
    headingColor = '#3d7adb'

    global Get_Img

    headerframe = Frame(root, height=100, width=800,bg=headingColor)
    headerframe.place(x=0,y=0)
    
    OpenImgPath = Image.open(img_path)
    img_resize_path = OpenImgPath.resize((60, 60))
    Get_Img = ImageTk.PhotoImage(img_resize_path)

    Label(headerframe, image=Get_Img, width=50,height=50,pady=10).place(x=250,y=30)
    Label(headerframe,text="Find Word",bg=headingColor,fg="white",font=("Times", "35", "bold ")).place(x=350,y=35)

def Input(mainframe):
    global player
    player =StringVar()
    
    NameLbl = Label(mainframe,text="Enter Your Name",font=("Times", "16", "bold "), bg=mainframeColor, fg="white")
    NameLbl.place(x=250,y=10)

    UserName = Entry(mainframe,textvariable=player,width=14,font=("Times", "14", "bold "))
    UserName.place(x=430,y=10)

    Label(mainframe,text="Select Level",font=("Times","24","bold"),fg="yellow",bg=mainframeColor).place(x=300,y=50)



def btnlevel(mainframe,levelVar,txt_x_axis,txt_y_axis,btn_x_axis,btn_y_axis):
      
    # levelName = levelVar
    global Imgforbtn
    if(levelVar == "beginner"):
        imgPath = "G:\\python tutorials\\find word\\projectWord\\level-1.png"
    elif(levelVar=="medium"):
        imgPath = "G:\\python tutorials\\find word\\projectWord\\level-2.png"
    elif(levelVar=="advance"):
        imgPath = "G:\\python tutorials\\find word\\projectWord\\level-3.png"

    def Begin():
        clear_frame()
        gameScreen(mainframe,player.get(),"__ __ __ __ __ __ __","Bigner","Animal",10,"A, B, C","Congratulation! You Win")
        

    def clear_frame():
        for widgets in mainframe.winfo_children():
            widgets.destroy()

    def on_enter(e):
        level['width'] = 180
        level['height'] = 180
        level['background'] = "red"
        level["border"] = "4"

    def on_leave(e):
        level['width'] = 160
        level['height'] = 160
        level['background'] = mainframeColor

           
    Label(mainframe,text=levelVar.upper(),font=("Times","20","bold"),fg="white",bg=mainframeColor).place(x=txt_x_axis,y=txt_y_axis)

    Img = Image.open(imgPath)
    Img_resize = Img.resize((170, 170))
    Imgforbtn = ImageTk.PhotoImage(Img_resize)
    global a,m,b
    if(levelVar == "beginner"):
        b = Imgforbtn
        level= Button(mainframe,image=b, borderwidth=0,width=160,height=160,border=4,  bg=mainframeColor, cursor="hand2",command=Begin)
        
    elif(levelVar=="medium"):
        m = Imgforbtn
        level= Button(mainframe,image=m, borderwidth=0,width=160,height=160,border=4,  bg=mainframeColor, cursor="hand2")

    elif(levelVar=="advance"):
        a = Imgforbtn
        level= Button(mainframe,image=a, borderwidth=0,width=160,height=160,border=4,  bg=mainframeColor, cursor="hand2")


    level.place(x=btn_x_axis,y=btn_y_axis)

    level.bind("<Enter>",on_enter)
    level.bind("<Leave>",on_leave)


def gameScreen(frame,UserName,gess_word,levelName,gess_list_type,remaining_live,guess_char,msg):
    font_list = list(font.families())
    centerFrameFont = str(font_list[281])
    center_color = "#eba434"
    lrcolor = "#3fcbe0"
    guess_type_Name = "Guess the "+ gess_list_type

    def back():
        for widgets in frame.winfo_children():
            widgets.destroy()
        stratTab(frame)

    ########  left side framee ###########################
    frame_left_side = Frame(frame,highlightbackground=center_color,bg=lrcolor, highlightthickness=4,width=200, height=358, bd= 0)
    frame_left_side.place(x=0,y=0)

    ########## Back Button ##########
    Button(frame,text="Back", borderwidth=0,width=25,height=2,border=1,  bg="black",fg="white", cursor="hand2",command=back).place(x=8,y=300)

    ######## Show player Name ###############
    Label(frame_left_side,text="Player:",font=("Times","12","bold"),fg="white",bg=lrcolor).place(x=0,y=10) # player label 
    player_Name = Label(frame_left_side,text=UserName,font=(str(font_list[181]),"16","bold"),fg="#800000",bg=lrcolor) # player Name
    player_Name.place(x=5,y=30)

    Label(frame_left_side,text="Level :",font=("Times","12","bold"),fg="white",bg=lrcolor).place(x=0,y=60) # Level Label
    level_lbl = Label(frame_left_side,text=levelName,font=("Times","16","bold"),fg="#800000",bg=lrcolor) # Level Name (bigner, Midium & Advance )
    level_lbl.place(x=60,y=60)

    ########  Center frame ###########################
    frame_center = Frame(frame,highlightbackground=center_color,bg=center_color, highlightthickness=4,width=400, height=358, bd= 0)
    frame_center.place(x=200,y=0)

    ############ Lable #############
    Label(frame_center,text="Press any alphabet key to",font=(centerFrameFont,"20","bold"),fg="#42ff5b",bg=center_color).place(x=50,y=5)
    ########### Word List type ##############
    guesslbl =Label(frame_center,text=guess_type_Name ,font=(str(font_list[213]),"20","bold"),fg="#5dba7f",bg=center_color)
    guesslbl.place(x=70,y=40)

    

    Guess =Label(frame_center,text=gess_word ,font=(str(font_list[213]),"14","bold"),fg="#ffed4f",bg=center_color)
    Guess.place(x=100,y=120)

    remarks = Label(frame_center,text=msg ,font=(str(font_list[13]),"14","bold"),fg="white",bg=center_color) # Message Label for match wind loos 
    remarks.place(x=100,y=203)

    ########  Right side framee ###########################
    frame_right_side = Frame(frame,highlightbackground=center_color,bg=lrcolor, highlightthickness=4,width=200, height=358, bd= 0)
    frame_right_side.place(x=600,y=0)
    #################  Remaining ########################
    remaining_live = Label(frame_right_side,text=remaining_live ,font=(str(font_list[120]),"20","bold"),fg="#00ff44",bg=lrcolor) # Remaining Live Number
    remaining_live.place(x=70,y=10)
    Label(frame_right_side,text="Remaining Live" ,font=(str(font_list[120]),"18","bold"),fg="#ffed4f",bg=lrcolor).place(x=0,y=40) # Remaining Live Label

    Label(frame_right_side,text="Guess Charecters" ,font=(str(font_list[120]),"15","bold"),fg="#ffed4f",bg=lrcolor).place(x=0,y=90)

    guessed_list = Label(frame_right_side,text=guess_char ,font=(str(font_list[120]),"18","normal"),fg="#00ff41",bg=lrcolor) # Remaining Live Number
    guessed_list.place(x=0,y=120)

def stratTab(mainframe):
    Input(mainframe)
    # ==================== Button level 1 ========================

    btnlevel(mainframe,"beginner",90,100,80,140)
    # ==================== Button level 2 ========================

    btnlevel(mainframe,"medium",320,100,300,140)

    # ==================== Button level 3 ========================
    btnlevel(mainframe,"advance",530,100,510,140)