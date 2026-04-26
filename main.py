from pyscript import display, document
import numpy as np

import logging
logging.getLogger("matplotlib").setLevel(logging.ERROR) # Suppress matplotlib warnings

import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# CLASSMATE LIST (GARCIA)
class addingClassmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject
        
    # is this what introduce() method means?
    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}! My favorite subject is {self.subject}."

previousClassmate = [
    addingClassmate("Jalainie Abdullah", "Topaz", "P.E."),
    addingClassmate("Harmony Yao", "Topaz", "Music"),
    addingClassmate("Ivy Zosa", "Topaz", "TLE"),
    addingClassmate("Skyler Escobar", "Topaz", "TLE"),
    addingClassmate("Phoebe Catimbang", "Topaz", "TLE"),
    ]

# global list
classmates = []


def addClassmate(e):
    output = document.getElementById("output")
    output.innerHTML = ""
    
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value
    
    if name and section and subject:
        # ur adding classmate data here, using append, so it can show in the list
        classmate = addingClassmate(name, section, subject)
        classmates.append(classmate)
        
        display(f"{name} has been added to the list.", target="output")
    else:
        display("Please fill in all the fields.", target="output")


def showList(e):
    output = document.getElementById("output")
    output.innerHTML = ""
    
    if previousClassmate:
        for i in previousClassmate:
            display(i.introduce(), target="output")
            
    # gets the list from the global variable
    if classmates:
        for i in classmates:
            # for every classmate in the list, it'll call the introduce thingy at the start (this is the message)
            display(i.introduce(), target="output")
            
# ATTENDANCE TRACKER (ABDULLAH)
month = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Aug", "Sep", "Oct", "Nov", "Dec"])
absences = np.full(10, np.nan)   # start with 10 empty values or spaces

def add(e):
    selected_month = document.getElementById("month").value
    absence_value = document.getElementById("absences").value
    
    if selected_month == "" or absence_value == "":
        document.getElementById("output").innerHTML = "Please select a month and enter absences."
        return
    
    absence_number = int(absence_value)
    
    index = np.where(month == selected_month)[0][0] # finding the specific month (it compares the month from the global value and the selected month which is in the index)
    absences[index] = absence_number # it goes to that position in the absence global value, replaces the nan with the local absence_number value
    
    document.getElementById("output").innerText = f"Absences recorded for {selected_month}."
    document.getElementById("absences").value = ""
    
def graph(e):
    document.getElementById("graph_output").innerText = ""
    if np.all(np.isnan(absences)):
        document.getElementById("output").innerText = "Please add an value to the absences."
        return
    
    # making the graph
    plt.bar(month, absences, color='skyblue')
    plt.title("Section Attendance Tracker")
    plt.xlabel("Monthly Attendance (Absences)")
    plt.ylabel("Number of Absences")
    plt.grid()

    display(plt, target="graph_output")
    document.getElementById("output").innerText = ""