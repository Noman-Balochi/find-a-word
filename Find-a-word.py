from os import write
from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
import random


# premierleague
root = Tk()
root.title("Find a Word")
root.geometry("800x500")
root.resizable(False,False)

headingColor = '#3d7adb'
mainframeColor = '#379b9e'
list_Name_lbl = ""
## lable UserName,

bigner_word_list = {"Fruits":["melon","lemon","mango","peach","papay","berry"]}
medium_word_list = {"Animal":["giraffe","bittern","opossum","elephant","squirrel","kangaroo","monkey","turtle"]}
advance_word_list = {"Color" : ["goldenrod","lawngreen","lightblue","lightgreen"]}

################# Level Button Method #########################
def levels(levelName,level_word_list,live):
    if (len(UserName.get()) == 0):
        messagebox.showwarning("Feild Required","Please Enter Name first")
    elif (len(UserName.get()) < 3):
        messagebox.showwarning("Feild Required","Name Required at least 3 letters")
    else:
        global player_lbl_Name , level_lbl, guess_lbl_list_Name, guess_Word_lbl, remaining_live_lbl, guess_word, original_word, lives,guess_word 
        global wrong_list, all_guess_list

        wrong_list = []
        all_guess_list = []
        guess_word = []
        MainScreen()
        lives = live
        player_lbl_Name.config(text=UserName.get())
        level_lbl.config(text=levelName)
        remaining_live_lbl.config(text=lives)

        listName = random.choice(list(level_word_list.keys()))
        wordlist = random.choice(list(level_word_list.values()))

        original_word = random.choice(wordlist)
        guess_lbl_list_Name.config(text="Guess The "+listName)

        for i in range(len(original_word)):
            guess_word.append("__")
    
        guess_word = [i for i in guess_word]
        guess_Word_lbl.config(text=guess_word)

        print(original_word+str(len(original_word)))

def Beginnerlevel():
    levels("Beginner",bigner_word_list,15)

def MediumLevel():
    levels("Medium",medium_word_list,20)


def AdvanceLevel():
    levels("Advance",advance_word_list,15)
    
        
    

def EnterKey():
    global player_lbl_Name , level_lbl, guess_lbl_list_Name, guess_Word_lbl, remaining_live_lbl, guess_word, original_word, remarks_lbl, enter_guess_charecter, lives
    global wrong_list, all_guess_list,btn_Entered_Char

    char = enter_guess_charecter.get()
    remarks_lbl.config(text="",fg="green")
    if(lives > 1):
        lives = lives - 1
        if(lives < 4):
            remaining_live_lbl.config(text=lives,fg="red")
        else:
            remaining_live_lbl.config(text=lives)
        

        if not char.isalpha():
            remarks_lbl.config(text='Guess only a letter',fg="red")
        #check if guessed letter length is one or not
        elif(len(char)>1):
            remarks_lbl.config(text='Guess only one letter...',fg="red")
        #check that letter chosen by user is already guessed or not
        elif(char in all_guess_list):
            remarks_lbl.config(text='You have Already guessed this letter',fg="red")
        #check if guessed_letter is matches with original_word
        elif char in original_word:
            print("char in oringal")
            for i in range(len(original_word)):
                if original_word[i] == char:
                    guess_word[i]=original_word[i]

            remarks_lbl.config(text="Wow! it match!",fg="green")
        else:
            # """if guessed_letter is not in original_word 
            # prompt user for wrong chosen letter"""
            remarks_lbl.config(text="You Guessed wrong letter",fg="red")
            wrong_list.append(char)
            

        all_guess_list.append(char)
        # print(all_guess_list)
        # print(wrong_list)
        guess_word = [i for i in guess_word]
        guess_word_string = "".join(guess_word)

        guess_Word_lbl.config(text=guess_word)
        print(original_word,guess_word_string)
        
        if original_word == guess_word_string:
            # print("You win")
            remarks_lbl.config(text='YAY !!, You have Got the letter ...',fg="green")
            btn_Entered_Char.config(state="disabled")
            enter_guess_charecter.config(state="disabled")
        
       
    else:
        messagebox.showwarning("Game Over","You Feild!")
        remaining_live_lbl.config(text="0",fg="red")
        btn_Entered_Char.config(state="disabled")
        enter_guess_charecter.config(state="disabled")

    enter_guess_charecter.delete(0, 'end')
    
#==================== Level Button Methods Show Screen ==========================

def Input():
    global UserName

    NameLbl = Label(mainframe,text="Enter Your Name",font=("Times", "16", "bold "), bg=mainframeColor, fg="white")
    NameLbl.place(x=250,y=10)

    UserName = Entry(mainframe,width=14,font=("Times", "14", "bold "))
    UserName.place(x=430,y=10)

    Label(mainframe,text="Select Level",font=("Times","24","bold"),fg="yellow",bg=mainframeColor).place(x=300,y=50)

def btnlevel(levelVar,txt_x_axis,txt_y_axis,btn_x_axis,btn_y_axis):
    
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

    global Imgforbtn
    if(levelVar == "beginner"):
        # imgPath = "G:\\python tutorials\\find word\\projectWord\\level-1.png"
        imgPath = ".\\projectWord\\level-1.png"
    elif(levelVar=="medium"):
        # imgPath = "G:\\python tutorials\\find word\\projectWord\\level-2.png"
        imgPath = ".\\projectWord\\level-2.png"
    elif(levelVar=="advance"):
        # imgPath = "G:\\python tutorials\\find word\\projectWord\\level-3.png"
        imgPath = ".\\projectWord\\level-3.png"
        
    Img = Image.open(imgPath)
    Img_resize = Img.resize((170, 170))
    Imgforbtn = ImageTk.PhotoImage(Img_resize)
    global a,m,b
    if(levelVar == "beginner"):
        b = Imgforbtn
        level= Button(mainframe,image=b, borderwidth=0,width=160,height=160,border=4,  bg=mainframeColor, cursor="hand2",command=Beginnerlevel)
    elif(levelVar=="medium"):
        m = Imgforbtn
        level= Button(mainframe,image=m, borderwidth=0,width=160,height=160,border=4,  bg=mainframeColor, cursor="hand2",command=MediumLevel)
    elif(levelVar=="advance"):
        a = Imgforbtn
        level= Button(mainframe,image=a, borderwidth=0,width=160,height=160,border=4,  bg=mainframeColor, cursor="hand2",command=AdvanceLevel)

    level.place(x=btn_x_axis,y=btn_y_axis)

    level.bind("<Enter>",on_enter)
    level.bind("<Leave>",on_leave)

def stratTab():
    Input()
    # ==================== Button level 1 ========================

    btnlevel("beginner",90,100,80,140)
    # ==================== Button level 2 ========================

    btnlevel("medium",320,100,300,140)

    # ==================== Button level 3 ========================
    btnlevel("advance",530,100,510,140)
    
######## Clear Button Frame Widgets ================
def clear_frame():
    for widgets in mainframe.winfo_children():
        widgets.destroy()

#========== Clear MainScreen frame ========
def back():
    for widgets in mainframe.winfo_children():
        widgets.destroy()
    stratTab()

# ############ this is where we Guess the Word ==================
def MainScreen():
    global list_Name_lbl
    global player_lbl_Name
    global level_lbl
    global guess_lbl_list_Name
    global enter_guess_charecter
    global guess_Word_lbl
    global remarks_lbl
    global remaining_live_lbl
    global btn_Entered_Char
    

    font_list = list(font.families())
    centerFrameFont = str(font_list[281])
    center_color = "#eba434"
    lrcolor = "#3fcbe0"

    ########  left side framee ###########################
    frame_left_side = Frame(mainframe,highlightbackground=center_color,bg=lrcolor, highlightthickness=4,width=200, height=358, bd= 0)
    frame_left_side.place(x=0,y=0)

    ########## Back Button ##########
    Button(mainframe,text="Back", borderwidth=0,width=25,height=2,border=1,  bg="black",fg="white", cursor="hand2",command=back).place(x=8,y=300)

    ######## Show player Name ###############
    Label(frame_left_side,text="Player:",font=("Times","12","bold"),fg="white",bg=lrcolor).place(x=0,y=10) # player label 
    player_lbl_Name = Label(frame_left_side,font=(str(font_list[181]),"16","bold"),fg="#800000",bg=lrcolor) # player Name
    player_lbl_Name.place(x=5,y=30)

    ########### show the level type (bigner,medium,advance)
    Label(frame_left_side,text="Level :",font=("Times","12","bold"),fg="white",bg=lrcolor).place(x=0,y=60) # Level Label
    level_lbl = Label(frame_left_side,font=("Times","16","bold"),fg="#800000",bg=lrcolor) # Level Name (bigner, Midium & Advance )
    level_lbl.place(x=60,y=60)

    ########  Center frame ###########################
    frame_center = Frame(mainframe,highlightbackground=center_color,bg=center_color, highlightthickness=4,width=400, height=358, bd= 0)
    frame_center.place(x=200,y=0)

    ############ Lable #############
    ########### Name of  List type ##############
    guess_lbl_list_Name =Label(frame_center,font=(str(font_list[213]),"20","bold"),fg="#5dba7f",bg=center_color)
    guess_lbl_list_Name.place(x=70,y=10)

    Label(frame_center,text="Enter any alphabet letter",font=(centerFrameFont,"20","bold"),fg="#42ff5b",bg=center_color).place(x=50,y=70)
    ########### Enter Charecter in Entry / textbox to guess the word
    enter_guess_charecter = Entry(mainframe,width=10,font=("Times", "20", "bold "))
    enter_guess_charecter.place(x=260,y=120)
    ############ Button To Guess Charecter ###############
    btn_Entered_Char = Button(mainframe,text="Enter",font=("Times", "12", "bold "),width=10,command=EnterKey) #
    btn_Entered_Char.place(x=420,y=123)
    
    ################ the word to Guess (__ __ __ __ __ ) ##########
    guess_Word_lbl =Label(frame_center,font=(str(font_list[213]),"20"),fg="#ffed4f",bg=center_color) # guess word __ __ __ __ __ 
    guess_Word_lbl.place(x=50,y=200)

    ############# Remarks (msg) ############3
    remarks_lbl = Label(frame_center,font=(str(font_list[13]),"14","bold"),fg="white",bg=center_color) # Message Label for match wind loos 
    remarks_lbl.place(x=100,y=290)

    ########  Right side framee ###########################
    frame_right_side = Frame(mainframe,highlightbackground=center_color,bg=lrcolor, highlightthickness=4,width=200, height=358, bd= 0)
    frame_right_side.place(x=600,y=0)

    #################  Remaining live ########################
    remaining_live_lbl = Label(frame_right_side, font=(str(font_list[120]),"20","bold"),fg="#00ff44",bg=lrcolor) # Remaining Live Number
    remaining_live_lbl.place(x=70,y=10)
    Label(frame_right_side,text="Remaining Live" ,font=(str(font_list[120]),"18","bold"),fg="#ffed4f",bg=lrcolor).place(x=0,y=40) # Remaining Live Label
    ############# All Guessed List ######################
    Label(frame_right_side,text="Guessed Charecters" ,font=(str(font_list[120]),"12","bold"),fg="#ffed4f",bg=lrcolor).place(x=0,y=90)
    all_guessed_list_lbl = Label(frame_right_side,text="" ,font=(str(font_list[120]),"18","normal"),fg="#00ff41",bg=lrcolor) # Remaining Live Number
    all_guessed_list_lbl.place(x=0,y=120)


############### main frame ##################### 
mainframe = Frame(root, height=360, width=800, bg=mainframeColor )
mainframe.place(x=0,y=102)

# global Get_Img
# img_path = "G:\\python tutorials\\find word\\projectWord\\button-1.png"
img_path = ".\\projectWord\\button-1.png"

headerframe = Frame(root, height=100, width=800,bg=headingColor)
headerframe.place(x=0,y=0)

OpenImgPath = Image.open(img_path)
img_resize_path = OpenImgPath.resize((60, 60))
Get_Img = ImageTk.PhotoImage(img_resize_path)

Label(headerframe, image=Get_Img, width=50,height=50,pady=10).place(x=250,y=30)
Label(headerframe,text="Find Word",bg=headingColor,fg="white",font=("Times", "35", "bold ")).place(x=350,y=35)

############## start screen ###############

stratTab()

# ############ Footer Frame #############
footerframe = Frame(root, height=40, width=800, bg='#25344d')
footerframe.place(x=0,y=460)

Label(footerframe , text="Copyright | Noman 2021",bg='#25344d',fg="white", font=("Times","14","bold")).place(x=300,y=0)

root.mainloop()