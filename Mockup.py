from tkinter import *
class View:
    root = Tk()
    root.geometry("1920x1080")
    root.config(bg="gray")

    frame_topleft = Frame(root)
    frame_topleft.config(bg="white")
    frame_topleft.grid(row=0, sticky=W)

    frame_topright = Frame(root)
    frame_topright.config(bg="white")
    frame_topright.grid(row=0, column=1, sticky=W)

    frame_underleft = Frame(root)
    frame_underleft.config(bg="green", padx=10, pady=10)
    frame_underleft.grid(row=1, column=0)

    frame_underright = Frame(root)
    frame_underright.config(bg="orange", padx=10, pady=10)
    frame_underright.grid(row=1, column=1)

    frame_bottom = Frame(root)
    frame_bottom.grid(row=2, rowspan=2)

    title = Label(frame_topleft, text="Team Rocket - Command Center", bg="blue", fg="white")
    title.config(anchor=NW, height=6, width=50, pady=20, padx=20)
    title.grid(row=0, column=0)

    date_time = Label(frame_topright, text="Date and time")
    date_time.config(anchor=W, height=6, width=50, pady=20, padx=20)
    date_time.grid(row=0, column=1)

    #button_launch = Button(frame_midtobottomright, text="LAUNCH", fg="blue")
    #button_launch.grid(sticky=N)
    #button_abort = Button(frame_midtobottomright,text="ABORT", fg="red")
    #button_abort.grid(sticky=S)

    #console_out = Label(frame_midtobottomright, text="Heeeeeelllloooooo")
    #console_out.config(width=250, height=500)
    #console_out.grid(row=2)

    #console_in = Entry(frame_midtobottomright)
    #console_in.config(width=75)
    #console_in.grid(row=3)



    #Use keyboard event to capture what is typed in console

    #Graphs
    current_altitude = Label(frame_underright, text="00.00")
    current_altitude.grid(row=0, column=0)

    canvas_altitude = Canvas(frame_underright)
    canvas_altitude.config(bg="black", width=850, height=275)
    canvas_altitude.grid(row=0, column=1)

    current_velocity = Label(frame_underright, text="00.00")
    current_velocity.grid(row=1, column=0)
    current_velocity.config(width=15)

    canvas_velocity = Canvas(frame_underright)
    canvas_velocity.config(bg="white", width=850, height=275)
    canvas_velocity.grid(row=1, column=1)

    current_acceleration = Label(frame_underright, text="00.00")
    current_acceleration.grid(row=2, column=0)

    canvas_acceleration = Canvas(frame_underright)
    canvas_acceleration.config(bg="blue", width=850, height=275)
    canvas_acceleration.grid(row=2, column=1)

    canvas_test = Canvas(frame_underleft)
    canvas_test.config(bg="white", width=800, height=835)
    canvas_test.grid(row=0)

    root.mainloop()


