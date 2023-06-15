from tkinter import ttk
import tkinter as tk       

programList = ['Create New Project', 'Project1', 'Project2', 'Project3', 'Project4']

class Application(tk.Frame):              
    def __init__(mainFrame, master=None):
        tk.Frame.__init__(mainFrame, master)
        mainFrame.grid(padx=70,pady=70)

def mainFrameButtonFunction():
    if programs.get() == 'Create New Project':
        def newProjectWindowButtonFunction():
            if newProjectTextBox.get() != '' and newProjectTextBox.get() not in programs['values']:
                programs['values'] += (newProjectTextBox.get(),)
                newProjectWindow.destroy()

        newProjectWindow = tk.Toplevel(width=300, height = 300)
        newProjectWindow.title(programs.get())
        newProjectWindow.resizable(False, False)

        newProjectTextBox = ttk.Entry(newProjectWindow)
        newProjectButton = ttk.Button(newProjectWindow, command=newProjectWindowButtonFunction, text='Create')
        newProjectLabel = ttk.Label(newProjectWindow, text='Name The Project')
        newProjectTextBox.place(relx=.3, rely=.4)
        newProjectButton.place(relx=.38, rely = .5)
        newProjectLabel.place(relx=.346, rely = .3)

        newProjectWindow.mainloop()
    elif programs.get() != "":
        currProgram = programs.get()

        def deleteProgramButtonFunction():
            newProgramList = []
            for program in programs['values']:
                if program != currProgram:
                    newProgramList.append(program)
            programs['values'] = newProgramList
            programs.delete(0,'end')
            programWindow.destroy()

        programWindow = tk.Toplevel(width=300, height=300)
        programWindow.title(programs.get())
        programWindow.resizable(False, False)

        deleteProgramButton = ttk.Button(programWindow, command=deleteProgramButtonFunction, text='Delete')
        deleteProgramButton.place(relx=.38, rely = .5)

        programWindow.mainloop()


app = Application()

label = ttk.Label(app, text='Select a Project')
programs = ttk.Combobox(app, state="readonly", values= programList, textvariable = 'Select a Project')
button = ttk.Button(app, command = mainFrameButtonFunction, text='Open')
label.grid(row=0, column=0, pady=10)
programs.grid(row=1, column=0)
button.grid(row=2, column=0, pady=10)     

app.master.title('TimeSheet++')    
app.master.resizable(False, False)
app.mainloop()  