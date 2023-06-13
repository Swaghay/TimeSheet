from tkinter import ttk
import tkinter as tk       

class Application(tk.Frame):              
    def __init__(mainFrame, master=None):
        tk.Frame.__init__(mainFrame, master)   
        mainFrame.grid(ipadx=300, ipady=200)                       
        label = ttk.Label(mainFrame, text='Select a Project')
        programs = ttk.Combobox(mainFrame, state="readonly", values=['Project1', 'Project2', 'Project3', 'Project4'], textvariable = 'Select a Project')
        label.grid(row=0, column=0)
        programs.grid(row=1, column=0)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_rowconfigure(1, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        

app = Application()                       
app.master.title('TimeSheet++')    
app.mainloop()  