from os import path
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
from configparser import ConfigParser


configur = ConfigParser()
configur.read('config.ini')

def config():
    editor_font = configur.get("editor","font")
    editor_font_size = configur.get("editor","font_size")
    title = configur.get("main","title")
    them = configur.get("main","them")
    resizable = configur.get("main","resizable")
    try:
        if resizable == "false":
            window.resizable(False,False)
        if resizable == "true":
            window.resizable(True,True)
        if them == "dark":
            window.title(title + "(ALPHA)   " + them + "(beta)")
            output.configure(bg='black', fg='#1dd604')
            textEditor.configure(bg='#362f2e', fg='#d2ded1', insertbackground='white',font=editor_font + " " + editor_font_size)
        if them == "light":
            window.title(title + "(ALPHA)   them:" + them + "(ALPHA)")
            output.configure(bg='white',fg='#1dd604')
            textEditor.configure(bg='white', insertbackground='black',font=editor_font + " " + editor_font_size)
    except:
        print("Error Config!")
        messagebox.showerror("Error!","Error in Config.ini!")
    
    textEditor.configure(font=editor_font + " " + editor_font_size)

    

window = Tk()

gpath = ''

def runMyCode():
    global gpath
    if gpath == '':
        messagebox.showerror("Please save the file first","Please save the file first")
        return
    command = "python" + " "+'"%s"' % gpath
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputResult, error = process.communicate()
    output.delete('1.0','end')
    output.insert('1.0',outputResult)
    output.insert('1.0',error)
     

def openMyFile():
        path = askopenfilename(filetypes=[('Python Files','*.py')])
        with open(path, 'r') as file:
            code = file.read()
            textEditor.delete('1.0', END)
            textEditor.insert('1.0', code)
            global gpath
            gpath = path

def saveMyFileAs():
    global gpath
    if gpath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = gpath
    with open(path, 'w') as file:
            code = textEditor.get('1.0', END)
            file.write(code)

textEditor = Text()
textEditor.pack()

output = Text(height=7)
output.bind("<Key>", lambda a: "break")

output.pack()
 
menuBar = Menu(window)

fileBar = Menu(menuBar, tearoff=0)

fileBar.add_command(label='Open', command = openMyFile)
fileBar.add_command(label='Save', command = saveMyFileAs)
fileBar.add_command(label='SaveAs', command = saveMyFileAs)
fileBar.add_command(label='Exit', command = exit)
menuBar.add_cascade(label='File', menu = fileBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='run', command = runMyCode)
menuBar.add_cascade(label='Tools', menu = runBar)

window.config(menu=menuBar)


config()
window.mainloop()
