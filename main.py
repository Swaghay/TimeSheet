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

        newProjectWindow = tk.Toplevel(width=300, height = 275)
        newProjectWindow.title(programs.get())
        newProjectWindow.resizable(False, False)

        newProjectTextBox = ttk.Entry(newProjectWindow)
        newProjectButton = ttk.Button(newProjectWindow, command=newProjectWindowButtonFunction, text='Create')
        newProjectLabel = ttk.Label(newProjectWindow, text='Name The Project')
        newProjectTextBox.place(relx=.5, rely=.45, anchor='center')
        newProjectButton.place(relx=.5, rely = .55, anchor='center')
        newProjectLabel.place(relx=.5, rely = .35, anchor='center')

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
            programs.set('')
            programWindow.destroy()

        programWindow = tk.Toplevel(width=300, height=300)
        programWindow.title(programs.get())
        programWindow.resizable(False, False)

        deleteProgramButton = ttk.Button(programWindow, command=deleteProgramButtonFunction, text='Delete')
        deleteProgramButton.place(relx=.5, rely = .5, anchor='center')

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