from tkinter import *
import sqlite3 

#==========Setting Up the Main Frame============
# constructor the frame
root = Tk()

# Title of the Frame
root.title("Python: Simple Login Application")

# Size of the window
width = 400
height = 400 

# Screen width and height
screen_width =root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2) 
y = (screen_height/2) - (height/2) 
root.geometry("%dx%d+%d+%d" % (width, height, x,y))
root.resizable(0,0)

# Set background color
root.config(background="orange") 

#============ Designing The Layout=============
#======VAriables=======
USERNAME = StringVar()
PASSWORD = StringVar()

#======Frames===========
Top = Frame(root, bd=2,relief=RIDGE) 
Top.pack(side=Top, fill=X) 

Form = Frame(root, height=200)
Form.pack(side=Top, pady=20)

#===========Labels==============
lbl_title = Label(Top, text="Python: Simple Login Application", font=('arial',15))
lbl_title.pack(fill=X) 

lbl_username = Label(Form, text="Username:", font=('arial', 14),bd=15)
lbl_username.grid(row=0, sticky='e') 

lbl_password = Label(Form, text="Password:", font=("arial", 14), bd=15) 
lbl_password.grid(row=1, sticky="e") 

lbl_text = Label(Form) 
lbl_text.grid(row=2, columnspan=2) 

# Display window
root.mainloop() 