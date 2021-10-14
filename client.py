# This is the GUI of the client


import tkinter
from tkinter import *
from PIL import Image
from pathlib import Path

gui = Tk()
gui.geometry("700x700")
gui.title("Chatbox")

menuBtn = Menubutton(gui, text="Paramètre")

send_btn = Button(text="Send")
send_btn.place(x=450, y=670)

menuBtn.menu = Menu(menuBtn)
menuBtn["menu"] = menuBtn.menu

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()


def security_settings():
    setting_sec = Toplevel(gui)
    setting_sec.geometry("700x700")
    setting_sec.title("Security")
    hash_encrypt = tkinter.Frame(setting_sec)
    hash_encrypt.pack()
    Label(hash_encrypt, text="Encryption Parameters").pack()
    server_setting = tkinter.Frame(setting_sec)
    server_setting.grid(column=0,row=0)


def close():
    gui.destroy()
    gui.quit()


menuBtn.menu.add_checkbutton(label="Security settings", variable=v1, command=security_settings)
menuBtn.menu.add_checkbutton(label="Server settings", variable=v2)
menuBtn.menu.add_checkbutton(label="Close", variable=v3, command=close)

send_btn = Button(gui, text="Send")

msg_entry = Entry(font="arial")
msg_entry.pack(side="bottom")
menuBtn.pack()
gui.mainloop()
