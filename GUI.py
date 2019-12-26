import tkinter
import time
import datetime
import requests
from functools import partial
from tkinter import *


main=tkinter.Tk()
main.title("Utility App")

running = False

#Declaring all pages here
homePage=tkinter.Frame(main, height=900, width=900)
def goHome():
  homePage.tkraise()
  running=False
  
timerPage=tkinter.Frame(main)

def goTimer():
  timerPage.tkraise()
  running=False
  
worldClockPage=tkinter.Frame(main)

def goWC():
  worldClockPage.tkraise()
  running=False
  
stopWatchPage=tkinter.Frame(main)

def goSW():
  stopWatchPage.tkraise()
  running= True

homePage.tkraise()

#Everything for the home page goes here
homePage.grid_propagate(False)
homePage.grid(row=0, column=0, sticky="nsew")
homeTitle = tkinter.Label(homePage, text="Welcome to your personal utilities",fg="black", font="Verdana 25 bold")
homeTitle.place(relx=.5 , rely=.05, anchor='center')
moreInfo = tkinter.Label(homePage, text="Please click any of the buttons below to start", fg="black", font="Verdana 10 bold")
moreInfo.place(relx=.5 , rely=.1, anchor='center')
timerBu=tkinter.Button(homePage, text="Go to Timer", command=goTimer, width = 15, height =3,bg="grey",fg="white")
timerBu.place(relx=.5,rely=.4, anchor='center')
worldclockBu=tkinter.Button(homePage, text="Go to World Clock", command=goWC, width = 15, height =3,bg="grey",fg="white")
worldclockBu.place(relx=.5,rely=.2, anchor='center')
stopwatchBu=tkinter.Button(homePage, text="Go to Stopwatch", command=goSW, width = 15, height =3,bg="grey",fg="white")
stopwatchBu.place(relx=.5,rely=.3, anchor='center')

#Everything for the timer page goes here
timerPage.grid(row=0, column=0, sticky="nsew")
label=tkinter.Label(timerPage)
homepageBu=tkinter.Button(timerPage, text="Go to Home page",bg="grey",fg="white", command=goHome, width = 15, height =3)
homepageBu.place(relx=.2,rely=.8, anchor='center')
stopwatchBu=tkinter.Button(timerPage, text="Go to Stopwatch",bg="grey",fg="white", command=goSW, width = 15, height =3)
stopwatchBu.place(relx=.5,rely=.8, anchor='center')
worldclockBu=tkinter.Button(timerPage, text="Go to World Clock",bg="grey",fg="white", command=goWC, width = 15, height =3)
worldclockBu.place(relx=.8,rely=.8, anchor='center')
labelfont = ('times', 30, 'bold')

class Countdown(tkinter.Frame):
    '''A Frame with label to show the time left, an entry to input the seconds to count
    down from, and a start button to start counting down.'''
    def __init__(timerPage, master):
        super().__init__(master)
        timerPage.create_widgets()
        timerPage.show_widgets()
        timerPage.seconds_left = 0
        timerPage._timer_on = False

    def show_widgets(timerPage):

        timerPage.title.pack()
        timerPage.label.pack()
        timerPage.label1.pack()
        timerPage.entry.pack()
        timerPage.start.pack()

    def create_widgets(timerPage):

        timerPage.title=tkinter.Label(timerPage,text="Timer",font='times 40 bold')
        timerPage.label = tkinter.Label(timerPage, text="00:00:00",width=20, height=8)
        timerPage.label.config(font=labelfont)
        timerPage.label1 = tkinter.Label(timerPage, text = "Type in the amount of seconds to countdown here",font='times 10 bold')
        timerPage.entry = tkinter.Entry(timerPage, justify='center')
        timerPage.entry.focus_set()
        timerPage.start = tkinter.Button(timerPage, text="Start", command=timerPage.start_button, height=2, border=3, width=10,font="times 20 bold")

    def countdown(timerPage):
        '''Update label based on the time left.'''
        timerPage.label['text'] = timerPage.convert_seconds_left_to_time()

        if timerPage.seconds_left:
            timerPage.seconds_left -= 1
            timerPage._timer_on = timerPage.after(1000, timerPage.countdown)
        else:
            timerPage._timer_on = False

    def start_button(timerPage):
        '''Start counting down.'''
        timerPage.seconds_left = int(timerPage.entry.get())   # 1. to fetch the seconds
        timerPage.stop_timer()                           # 2. to prevent having multiple
        timerPage.countdown()                            #    timers at once

    def stop_timer(timerPage):
        '''Stops after schedule from executing.'''
        if timerPage._timer_on:
            timerPage.after_cancel(timerPage._timer_on)
            timerPage._timer_on = False

    def convert_seconds_left_to_time(timerPage):

        return datetime.timedelta(seconds=timerPage.seconds_left)


if __name__ == '__main__':

    countdown = Countdown(timerPage)
    countdown.pack()

 

#Everything for the World Clock Page goes here
worldClockPage.grid(row=0, column=0, sticky="nsew")
srs = tkinter.Label(worldClockPage, text="World Clock", fg="black", font="Verdana 30 bold")
srs.place(relx=.5,rely=.05, anchor='center')
wrw = tkinter.Label(worldClockPage, text="Type in a country that you would like to search up", fg="black", font="Verdana 15")
wrw.place(relx=.5,rely=.15, anchor='center')
homepageBu=tkinter.Button(worldClockPage, text="Go to Home page",bg="grey",fg="white", command=goHome, width = 15, height =3)
homepageBu.place(relx=.2,rely=.8, anchor='center')
stopwatchBu=tkinter.Button(worldClockPage, text="Go to Stopwatch",bg="grey",fg="white", command=goSW, width = 15, height =3)
stopwatchBu.place(relx=.8,rely=.8, anchor='center')
timerBu=tkinter.Button(worldClockPage, text="Go to Timer",bg="grey",fg="white", command=goTimer, width = 15, height =3)
timerBu.place(relx=.5,rely=.8, anchor='center')

def searchCountry(userInput):
    # REST API by RESTCountries.eu
    url = "https://restcountries.eu/rest/v2/name/" + userInput
    response = requests.get(url).json()

    if (type(response) is dict):
        createSearchWindow(True)
    else:
        createSearchWindow(False, response)

def createSearchWindow(isError, data = None):
    searchWindow = Toplevel(worldClockPage)
    if (isError):
        errorMsg = Label(searchWindow, text="Error in input. Try Again.").grid(row=0)
    else:
        if (len(data) > 1):
            for i in range(len(data)):
                country = data[i]
                button = Button(searchWindow, text=country["name"], command=lambda x=country: displayDetails(x)).grid(row=i)
        else:
            displayDetails(data[0])

def displayDetails(country):
    # set variables- name, timezone names, local time in tz's
    countryName = country["name"]
    timezones = country["timezones"]
    localTimes = []
    for timezone in timezones:
        localTimes.append(convertTimezoneToLocalTime(timezone))

    displayWindow = Toplevel(worldClockPage)
    countryNameLabel = Label(displayWindow, text=countryName).grid(row=0)
    for i in range(len(timezones)):
        timezoneLabel = Label(displayWindow, text=timezones[i] + ": " + localTimes[i]).grid(row=i+1)

def convertTimezoneToLocalTime(timezone):
    if (len(timezone) == 3):
        timezone = 0
    else:
        timezone = timezone[3:6]
    offset = int(timezone) * 3600
    sinceEpoch = time.time()
    localTime = time.gmtime(sinceEpoch + offset)
    return time.strftime('%a, %d %b %Y %H:%M:%S GMT', localTime)


# variables
userInput = StringVar()

# window contents
countryFieldLabel = Label(worldClockPage, text = "Search a country: ",font="Verdana 10 bold")
countryFieldLabel.place(relx=.2,rely=.4)
countryField = Entry(worldClockPage, textvariable=userInput)
countryField.place(relx=.5,rely=.4)
countrySearchButton = Button(worldClockPage, text="Search", command= lambda: searchCountry(userInput.get()), width = 15, height =3)
countrySearchButton.place(relx=.8,rely=.4)
    



#Everything for the stopwatch page goes here
stopWatchPage.grid(row=0, column=0, sticky="nsew")
worldclockBu=tkinter.Button(stopWatchPage, text="Go to World Clock",bg="grey",fg="white", command=goWC, width = 15, height =3)
worldclockBu.place(relx=.8,rely=.8, anchor='center')
timerBu=tkinter.Button(stopWatchPage, text="Go to Timer",bg="grey",fg="white", command=goTimer, width = 15, height =3)
timerBu.place(relx=.5,rely=.8, anchor='center')
homepageBu=tkinter.Button(stopWatchPage, text="Go to Home page",bg="grey",fg="white", command=goHome, width = 15, height =3)
homepageBu.place(relx=.2,rely=.8, anchor='center')
counter = -1
mCounter=0
hCounter=0
running = False

def ResetSeconds(labelS):
  global counter
  counter = 1

def ResetMinutes(labelM):
  global mCounter
  mCounter=1

def ResetHours(labelH):
  global hCounter
  hCounter=0

def GetMins():
  labelM.configure(text=mCounter)

def GetHours():
  labelH.configure(text=hCounter)

def currentLap():
  global lapTime
  lapTime = str(hCounter) + "   : " + str(mCounter) + "    : " + str(counter-1)
  timeTable.insert(0,lapTime)


def clearTable():
  timeTable.delete(0,tkinter.END)

def counter_label(labelS):  
    def count(): 
        if running: 
            global counter
            global mCounter
            
  
            # To manage the intial delay. 
            if counter==-1:             
                display="Starting..."
            else: 
                display=str(counter) 
  
            labelS['text']=display   # Or label.config(text=display) 
  
            #labelS.after(arg1, arg2) delays by first argument given in milliseconds and then calls the function given as second argument. 
            # Generally like here we need to call the function in which it is present repeatedly. Delays by 1000ms=1 seconds and call count again. 
            labelS.after(1000, count)  
            counter += 1
            #This checks if the seconds is equal to 60 then it resets seconds
            if counter == 61:
              mCounter+=1
              ResetSeconds(labelS)
              GetMins()
              #This checks if the minutes is equal to 60 then it resets minutes
              if mCounter==60:
                hCounter+=1
                ResetMinutes(labelM)
                GetHours()
    # Triggering the start of the counter. 
    count()
    
  
# start function of the stopwatch 
def Start(labelS): 
    global running 
    running=True
    counter_label(labelS) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    lap['state']='normal'
    labelM['text']=' '
    labelH['text']=' '

    
  
# Stop function of the stopwatch 
def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    lap['state']='disabled'
    running = False
  
  

# Reset function of the stopwatch 
def Reset(labelS, labelM, labelH): 
    global counter 
    counter=-1
    mCounter=0
    clearTable()
  
    # If rest is pressed after pressing stop. 
    if running==False:       
        reset['state']='disabled'
        lap['state']='disabled'
        labelM['text']='Welcome!'
        labelS['text']=' '
        labelH['text']=' '
  
    # If reset is pressed while the stopwatch is running. 
    else:                
        labelS['text']='Starting...'
        labelM['text']=' '
        labelH['text']=' '
  
  
# Fixing the window size.
mt = tkinter.Label(stopWatchPage, text="Stopwatch", fg="black", font="Verdana 30 bold")
mt.place(relx=.5,rely=.02, anchor='center')
sls = tkinter.Label(stopWatchPage, text="Seconds", fg="black", font="Verdana 30 bold") 
sls.place(relx=.8 , rely=.1, anchor='center')
labelS = tkinter.Label(stopWatchPage, fg="black", font="Verdana 30 bold") 
labelS.place(relx=.8 , rely=.15, anchor='center')
mlm = tkinter.Label(stopWatchPage, text="Minutes", fg="black", font="Verdana 30 bold") 
mlm.place(relx=.5 , rely=.1, anchor='center')
labelM = tkinter.Label(stopWatchPage, text="Welcome!", fg="black", font="Verdana 30 bold")
labelM.place(relx=.5 , rely=.15, anchor='center')
hlh = tkinter.Label(stopWatchPage, text="Hours", fg="black", font="Verdana 30 bold") 
hlh.place(relx=.2 , rely=.1, anchor='center')
labelH = tkinter.Label(stopWatchPage, fg="black", font="Verdana 30 bold")
labelH.place(relx=.2 , rely=.15, anchor='center')
start = tkinter.Button(stopWatchPage, text='Start', width=15, command=lambda:Start(labelS)) 
stop = tkinter.Button(stopWatchPage, text='Stop',  width=15, state='disabled', command=Stop) 
reset = tkinter.Button(stopWatchPage, text='Reset', width=15, state='disabled', command=lambda:Reset(labelS, labelM, labelH))
lap = tkinter.Button(stopWatchPage, text='Lap',  width=15, state='disabled', command=currentLap)
lap.place(relx=.5 , rely=.28, anchor='center')
start.place(relx=.2 , rely=.25, anchor='center')
stop.place(relx=.5 , rely=.25, anchor='center')
reset.place(relx=.8 , rely=.25, anchor='center')

#timeTable
timeTable = tkinter.Listbox(stopWatchPage,width=50,height=18)
timeTable.place(relx=.5 , rely=.55, anchor='center')

main.mainloop()
