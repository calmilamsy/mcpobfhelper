# Author:      calmilamsy
#
# Created:     23/09/2018
# Copyright:   (c) calmilamsy 2018
# Licence:     GNU-GPL V3 I guess. Idgaf, just dont turn it into a virus or something.

try:
    from tkinter import *
except:
    from Tkinter import *
clientErr=False
serverErr=False

class classes:
    class client:
        obfclass=[]
        deobfclass=[]
    class server:
        obfclass=[]
        deobfclass=[]

def makeLabel(master, h, w, y, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.grid(columnspan=2, row=y, column=0)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label

def makeButton(master, h, w, a, y, lr, *args, **kwargs):
    if lr==True: lr=0
    else: lr=1
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.grid(columnspan=1, row=y, column=lr)
    button = Button(f, *args, **kwargs)
    button.pack(fill=BOTH, expand=1)
    return button

def makeInput(master, h, w, y, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.grid(columnspan=2, row=y, column=0)
    entry = Entry(f, *args, **kwargs)
    entry.pack(fill=BOTH, expand=1)
    return entry

def empty(master, h, w, y, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.grid(columnspan=2, row=y, column=0)
    return f

def getObfTable():
    global clientErr
    global serverErr
    deobfclass=[]
    try:
        file=open("temp/client_rg.srg", "r")
        for line in file.readlines():
            if line[:2] == "CL":
                typ, obfclass, deobfclasspath = line.split(" ")
                classes.client.deobfclass.append(deobfclasspath.split("/")[len(deobfclasspath.split("/"))-1][:-1])
                classes.client.obfclass.append(obfclass)
    except Exception as error:
        status.config(text="Error: Missing or corrupt client file.", foreground="red")
        clientErr=True
    try:
        file=open("temp/server_rg.srg", "r")
        for line in file.readlines():
            if line[:2] == "CL":
                typ, obfclass, deobfclasspath = line.split(" ")
                classes.client.deobfclass.append(deobfclasspath.split("/")[len(deobfclasspath.split("/"))-1][:-1])
                classes.server.obfclass.append(obfclass)
    except Exception as error:
        status.config(text="Error: Missing or corrupt server file.", foreground="red")
        serverErr=True
    if (clientErr == True) and (serverErr == True):
        status.config(text="Error: Missing or corrupt server and client file.", foreground="red")

win=Tk()
win.geometry("320x300")
## win.resizable(False, False)
win.title("MCP Obfuscation Helper V1")
makeLabel(win, 100, 320, 0, text="Instructions:\n1. Place this program in your MCP folder.\n2. Run the program.\n3. Enter the class (CaSe-sEnSiTiVe).\n4. Press 'Obfuscate' or Deobfuscate.", font=("Courier", 9), justify="left")
makeInput(win, 20, 280, 1)
empty(win, 20, 320, 2)
result=makeLabel(win, 20, 320, 3)
empty(win, 20, 320, 4)
makeButton(win, 40, 100, "left", 5, True, text="Client Deob")
makeButton(win, 40, 100, "left", 5, True, text="Client Reob")
makeButton(win, 40, 100, "right", 6, False, text="Server Deob")
makeButton(win, 40, 100, "right", 6, False, text="Server Reob")
empty(win, 20, 320, 7)
f = Frame(win, height=20, width=320)
f.pack_propagate(0)
f.grid(row=8)
status = Label(f, text="", background="lightgrey")
status.pack(fill=BOTH, expand=1)
getObfTable()
win.mainloop()