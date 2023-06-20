from tkinter import ttk
import tkinter as tk      
from tkinter import messagebox 
import pickle
import os

def open_projects_file():
    try:
        with open(r"C:\Users\Abhay\Desktop\TimeSheet++_Data\data.pickle", 'rb') as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error Loading Object", ex)

try:
    projectList = open_projects_file()
except:
    projectList = ['Create New Project', 'Project1', 'Project2', 'Project3', 'Project4']

class Application(tk.Frame):              
    def __init__(mainFrame, master=None):
        tk.Frame.__init__(mainFrame, master)
        mainFrame.grid(padx=70,pady=70)

def mainFrameButtonFunction():
    if projects.get() == 'Create New Project':
        def newProjectWindowButtonFunction():
            if newProjectTextBox.get() != '' and newProjectTextBox.get() not in projects['values']:
                projects['values'] += (newProjectTextBox.get(),)
                projects.set('')
                newProjectWindow.destroy()

        newProjectWindow = tk.Toplevel(width=300, height = 275)
        newProjectWindow.title(projects.get())
        newProjectWindow.resizable(False, False)

        newProjectTextBox = ttk.Entry(newProjectWindow)
        newProjectButton = ttk.Button(newProjectWindow, command=newProjectWindowButtonFunction, text='Create')
        newProjectLabel = ttk.Label(newProjectWindow, text='Name The Project')
        newProjectTextBox.place(relx=.5, rely=.45, anchor='center')
        newProjectButton.place(relx=.5, rely = .55, anchor='center')
        newProjectLabel.place(relx=.5, rely = .35, anchor='center')

        newProjectWindow.mainloop()
        
    elif projects.get() != "":
        currProject = projects.get()

        def deleteProjectButtonFunction():
            newProjectList = []
            for project in projects['values']:
                if project != currProject:
                    newProjectList.append(project)
            projects['values'] = newProjectList
            projects.delete(0,'end')
            projects.set('')
            projectWindow.destroy()

        projectWindow = tk.Toplevel(width=300, height=300)
        projectWindow.title(projects.get())
        projectWindow.resizable(False, False)

        deleteProjectButton = ttk.Button(projectWindow, command=deleteProjectButtonFunction, text='Delete')
        deleteProjectButton.place(relx=.5, rely = .5, anchor='center')

        projectWindow.mainloop()


app = Application()

label = ttk.Label(app, text='Select a Project')
projects = ttk.Combobox(app, state="readonly", values= projectList, textvariable = 'Select a Project')
button = ttk.Button(app, command = mainFrameButtonFunction, text='Open')
label.grid(row=0, column=0, pady=10)
projects.grid(row=1, column=0)
button.grid(row=2, column=0, pady=10)     

def closeApp():
    answer = messagebox.askyesnocancel("Quit", "Do you want to save and quit?")
    if answer:
        save_projects(projects['values'])
        app.master.destroy()
    elif answer == False:
        app.master.destroy()

def save_projects(obj):
    try:
        os.mkdir(r'C:\Users\Abhay\Desktop\TimeSheet++_Data')
    except OSError as er:
            print(er)
    try:
        with open(r"C:\Users\Abhay\Desktop\TimeSheet++_Data\data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error Saving Object!", ex)
    
app.master.title('TimeSheet++')    
app.master.resizable(False, False)
app.master.protocol("WM_DELETE_WINDOW", closeApp)
app.mainloop()  