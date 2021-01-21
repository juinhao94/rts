from tkinter import *
from tello import Tello

### Drone Initialization
tello = Tello()

### Setup Tkinter window
root = Tk()  # Initiate controller dashboard GUI
root.title('Tello Drone Controller') # Window Title
root.geometry('800x400') # Window Size (width x height)



### ------------------------------- ###
### User defined methods
### ------------------------------- ###

### Start to sweep within preplan route
def start_sweep():
    print("Status >>> Initiating parameter sweep")
    print("Status >>> Parameter sweep is running...")
    tello.run_sweep()

    
### Change auto/manual mode
def override_sweep():
    print("Status >>> Parameter sweep has been overridden")
    tello.terminate_sweep()


### Exit controller
def quit_dashboard():
    print("See ya!")
    tello.close_socket()
    root.destroy()


### Drone start taking off from land
def takeoff():
    print("Action >>> Drone is taking off...")
    tello.takeoff()
    print("Status >>> Drone is ready for flight.")

    
### Drone move back to Checkpoint
def reset_position():
    print("Action >>> Move back to Checkpoint 0")
    tello.reset_position()

    
### Drone preparing for land    
def ready_to_land():
    print("Action >>> Returning to charging base...")
    tello.ready_to_land()
    
    
### Drone landing    
def land():
    print("Action >>> Drone is landing...")
    tello.land()
    print("Status >>> Drone landed safely")

    
### Drone move forward
def forward():
    print("Action >>> Move forward 10 units")
    tello.forward()


### Drone move backward
def back():
    print("Action >>> Move backward 10 units")
    tello.back()


### Drone rotate to left
def turn_left():
    print("Action >>> Rotate left for 90", chr(176), sep='')
    tello.rotate_left()


### Drone rotate to right    
def turn_right():
    print("Action >>> Rotate right for 90", chr(176), sep='')
    tello.rotate_right()


    
### ------------------------------- ###
### Dashboard buttons creation
### ------------------------------- ###

# Prepare for landing button
photoReady = PhotoImage(file="ready.png")
btnReady = Button(root, image=photoReady, text="Ready for landing", command=ready_to_land, height=50, width=120, compound=TOP)
#readyToLandButton = Button(top, height=2, width=15, text="Prepare to land", command=ready_to_land)

# Land button
photoLand = PhotoImage(file="drone_down.png")
btnLand = Button(root, image=photoLand, text="Land", command=land, height=50, width=120, compound=TOP)

# Sweep button
photoSweep = PhotoImage(file="route.png")
btnSweep = Button(root, image=photoSweep, text="Run Sweep", command=start_sweep, height=50, width=120, compound=TOP)

# Take Off button
photoTakeOff = PhotoImage(file="drone_up.png")
btnTakeOff = Button(root, image=photoTakeOff, text="Take Off", command=takeoff, height=50, width=120, compound=TOP)

# Back To Origin button
photoResetPosition = PhotoImage(file="reset.png")
btnResetPosition = Button(root, image=photoResetPosition, text="Back to Origin", command=reset_position, height=50, width=120, compound=TOP)

# Move FORWARD button
photoForward = PhotoImage(file="up.png")
btnForward = Button(root, image=photoForward, command=forward, height=50, width=50, compound=TOP)

# Rotate LEFT button
photoLeft = PhotoImage(file="left.png")
btnLeft = Button(root, image=photoLeft, command=turn_left, height=50, width=50, compound=LEFT)

# Mode overriden button
photoOverride = PhotoImage(file="override.png")
btnOverride = Button(root, image = photoOverride, command=override_sweep, height=50, width=50, compound=LEFT)

# Rotate RIGHT button
photoRight = PhotoImage(file="right.png")
btnRight = Button(root, image=photoRight, command=turn_right, height=50, width=50, compound=RIGHT)

# Move BACKWARD button
photoBack = PhotoImage(file="down.png")
btnBack = Button(root, image=photoBack, command=back, height=50, width=50, compound=BOTTOM)

# Exit Program button
photoQuit = PhotoImage(file="quit.png")
btnQuit = Button(root, image=photoQuit, text="Quit Controller", command=quit_dashboard, height=50, width=120, compound=TOP)


### ------------------------------- ###
### Action button placement
### ------------------------------- ###

root.grid_columnconfigure(1, minsize=30)  # Column 1 spacing
root.grid_rowconfigure(5, minsize=30)  # Row 5 spacing


# -- Row 2 buttons --
btnForward.grid(row=2, column=3)
btnTakeOff.grid(row=2, column=7)

# -- Row 3 buttons --
btnLeft.grid(row=3, column=2)
btnOverride.grid(row=3, column=3)
btnRight.grid(row=3, column=4)
btnReady.grid(row=3, column=6)
btnSweep.grid(row=3, column=7)
btnResetPosition.grid(row=3, column=8)

# -- Row 4 buttons --
btnBack.grid(row=4, column=3)
btnLand.grid(row=4, column=7)

# -- Row 6 buttons --
btnQuit.grid(row=6, column=5)


# Event looping in this controller window
root.mainloop()