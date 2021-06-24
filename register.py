from tkinter import *
import os 

def delete2():
  screen3.destroy()
def delete3():
  screen4.destroy()
def delete4():
  screen5.destroy()
def delete5():
  screen7.destroy()

def saved():
  global screen7
  screen7= Toplevel(screen)
  screen7.title("Saved")
  screen7.geometry("100x100")
  Label(screen7, text="Saved").pack()
  Button(screen7, text= "OK", command=delete5).pack()
 
  

def save():
  filename = raw_filename.get()
  notes= raw_notes.get()

  data=open(filename, "w")
  data.write(notes)
  data.close()

  saved()



def create_notes():
  global raw_filename
  raw_filename = StringVar()
  global raw_notes
  raw_notes= StringVar()

  screen6= Toplevel(screen)
  screen6.title("Info")
  screen6.geometry("300x250")
  Label(screen6, text="Please enter a filename for the note below: ").pack()
  Entry(screen6,textvariable=raw_filename).pack()
  Label(screen6, text="Please enter the notes for the file below: ").pack()
  Entry(screen6,textvariable=raw_notes).pack()
  Button(screen6,text="Save", command=save).pack()

def view_notes1():
  filename1=raw_filename1.get()
  data= open(filename1, "r")
  data1 = data.read()
  screen8= Toplevel(screen)
  screen8.title("Info")
  screen8.geometry("250x400")
  Label(screen8, text=data1).pack()
 
  

def view_notes():
  screen7= Toplevel(screen)
  screen7.title("Info")
  screen7.geometry("250x400")
  all_files= os.listdir()
  Label(screen7, text="Please choose one of the filenames below").pack()
  Label(screen7, text=all_files).pack()
  global raw_filename1
  raw_filename1 = StringVar()
  Entry(screen7, textvariable=raw_filename1).pack()
  Button(screen7,command=view_notes1, text="OK").pack()

def delete_note1():
  filename3=raw_filename2.get()
  os.remove(filename3)
  screen10= Toplevel(screen)
  screen10.title("Info")
  screen10.geometry("250x400")
  Label(screen10, text=filename3+" removed successfully").pack()

def delete_note():
  screen9= Toplevel(screen)
  screen9.title("Info")
  screen9.geometry("250x400")
  all_files= os.listdir()
  Label(screen9, text="Please choose one of the filenames below").pack()
  Label(screen9, text=all_files).pack()
  global raw_filename2
  raw_filename2 = StringVar()
  Entry(screen9, textvariable=raw_filename2).pack()
  Button(screen9,command=delete_note1, text="OK").pack()



def session():
  global screen3
  screen3= Toplevel(screen)
  screen3.title("Dashboard")
  screen3.geometry("400x400")
  Label(screen3, text="Welcome to dashboard").pack()
  Button(screen3, text= "Create Note ", command=create_notes).pack()
  Button(screen3, text= "View Note", command= view_notes).pack()
  Button(screen3, text= "Delete Note", command= delete_note).pack()





def login_success():
  session()
  

def password_not_recognized():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text="Password Error").pack()
  Button(screen4, text= "OK", command= delete3).pack()


def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text="No User Found ").pack()
  Button(screen5, text= "OK", command= delete4).pack()


def register_user():

  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def login_verify():
    user_name= username_verify.get()
    pass_word= password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files= os.listdir()
    if user_name in list_of_files:
      file1= open(user_name, "r")
      verify = file1.read().splitlines()
      if pass_word in verify:
        login_success()
      else:
        password_not_recognized()
    else:
      user_not_found()

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()
    
    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    
    Label(screen2, text = "Username * ").pack()
    username_entry1= Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text = " ").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1= Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text = " ").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()




def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Notes 1.0")
  Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
  
