from tkinter import ttk
import tkinter as tk       

class Application(tk.Frame):              
    def __init__(frame, master=None):
        tk.Frame.__init__(frame, master)   
        frame.grid(ipadx=300, ipady=200)                       
        label = ttk.Label(text='Select a Project')
        programs = ttk.Combobox(state="readonly", values=['Project1', 'Project2', 'Project3', 'Project4'], textvariable = 'Select a Project')
        label.grid()
        programs.grid()
        
        

app = Application()                       
app.master.title('TimeSheet++')    
app.mainloop()  