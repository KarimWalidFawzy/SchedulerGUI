import cmd
import time
from tkinter import *
def SRTF():
    pass
def Drawprocess(window,process):
    canvas=Canvas(window)
    label=Label(window,text=process.name)
    label.place(x=(process.burst_time+process.arrival_time)/2,y=250)
def FCFS():
    secondwindow=Tk()
    secondwindow.title("FCFS")
    secondwindow.geometry('500x500')
    z=entry.get()
    process=[]
    secondLabel=Label(secondwindow,text=f'Average turnaround time={z}')
    thrdlabl=Label(secondwindow,text=f'Average waiting time={z}')
    frthlabl=Label(secondwindow,text=f'Remaining Burst time={z}')
    secondLabel.place(x=0,y=470)
    thrdlabl.place(x=160,y=470)
    frthlabl.place(x=300,y=470)
    canvas=Canvas(secondwindow)
    canvas.create_rectangle(2,2,z,z)
    canvas.pack()
def SJFnp():
    thrdwindow=Tk()
    thrdwindow.title("SJF non-preemptive")
def RR():
    frthwindow = Tk()
    frthwindow.title("RR")
def prtyschdlng():
    ffthwndw=Tk()
    ffthwndw.title('Priority Scheduling')
def SJFp():
    pass
window=Tk()
label=Label(window,text="Please select the type of scheduler you wish to use:")
label.place(x=0,y=0)
window.geometry("420x420")
window.title("Scheduler")
but=Button(window,
           text="FCFS (First come first served)",
           command=FCFS)
but.place(x=0,y=20)
but2=Button(window,text="SJF (Shortest job first) non-preemptive",command=SJFnp)
but2.place(x=0,y=50)
but3=Button(window,text="Round Robin (RR)",command=RR)
but3.place(x=0,y=80)
prool=BooleanVar()
butprrty=Button(window,text="Use priority non-preemptive scheduling",command=prtyschdlng)
butprrty.place(x=0,y=110)
prcheck=Button(window,text='Use SJF preemptive scheduling',command=SJFp)
prcheck.place(x=0,y=140)
but5=Button(window,text='Use Priority preemptive scheduling',command=SRTF)
but5.place(x=0,y=170)
but4=Button(window,text="Add new process")#command=Process
but4.place(x=0,y=200)
label2=Label(window,text="Enter burst time of process:")
label2.place(x=0,y=230)
entry=Entry(window)
entry.place(x=0,y=250)
window.mainloop()
#place window on computer screen

