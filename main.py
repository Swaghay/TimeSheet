import tkinter as tk       

class Application(tk.Frame):              
    def __init__(frame, master=None):
        tk.Frame.__init__(frame, master)   
        frame.grid(ipadx=300, ipady=200)                       
        frame.createWidgets()
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    def createWidgets(quit):
        quit.quitButton = tk.Button(quit, text='Quit',
            command=quit.quit)            
        quit.quitButton.grid(row=0, column=0)            

app = Application()                       
app.master.title('TimeSheet++')    
app.mainloop()  