import random
import tkinter as tk
from tkinter import messagebox

name= "sonu"
password= "sharma123"

def user_input():
    n = username_entry.get()
    p = password_entry.get()
    return n, p

def check_credentials():
    entered_username,entered_password =user_input()
    if entered_username == name and entered_password == password:
        messagebox.showinfo("login status","Login sucessful")
    else:
        messagebox.showinfo("Incorrect credentials","Incorrect username")


def generate_otp():
    o = random.randrange(100,500)
    return o 

def otp_login():
    entered_otp = otp_entry.get()
    if entered_otp == str(current_otp):
        username_label.config(text=f"user name: {name}")
        password_label.config(text=f"password: {password}")
    else:
        messagebox.showinfo("Incorrect otp", "Incorrect otp.please enter correct") 

def resend_otp():
    global current_otp
    current_otp = generate_otp()
def resend_otp1():
    global current_otp
    current_otp = generate_otp()
    messagebox.showinfo("otp window", f"An otp has been sent to your screen",)

def forget_credentials():
    global current_otp
    message="An otp has been send on your registered email id"
    messagebox.showinfo("forget username/passward",message)
    otp_label.config(text="Enter the otp recive on your email id:")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    username_entry.config(state=tk.DISABLED)
    password_entry.config(state=tk.DISABLED)
    login_button.config(state=tk.DISABLED)
    otp_login_button.config(state=tk.NORMAL)
    resend_otp_button.config(state=tk.NORMAL)



# Creat the main tkinter window

window = tk.Tk()
window.title("Login App")


# Creat labels, entry field and buttons
username_label = tk.Label(window, text="Enter user name:")
password_label = tk.Label(window, text="Enter user password:")
username_entry = tk.Entry(window)
password_entry = tk.Entry(window, show="*")


otp_label = tk.Label(window, text="")
otp_entry = tk.Entry(window, show="*")

login_button = tk.Button(window, text="Login", command=check_credentials)
otp_login_button = tk.Button(window, text="OTP Login", command=otp_login)
resend_otp_button = tk.Button(window, text="Resend OTP", command=resend_otp1)
forget_button = tk.Button(window, text="Forget username/Password", command=resend_otp1)

# Place widgets in the window 
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()
forget_button.pack()
otp_label.pack()
otp_entry.pack()
otp_login_button.pack()
resend_otp_button.pack()

# Start the tkinter main loop
window.mainloop()