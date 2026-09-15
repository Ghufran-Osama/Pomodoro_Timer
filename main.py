from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
fg = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
check_mark = "\u2713"
reps = 0
tt = None
# ---------------------------- TIMER MECHANISM ------------------------------- #
def reset_time():
    global marks
    global reps
    global tt
    if tt != None:
        window.after_cancel(tt)
    canvas.itemconfig(t_down, text="00:00")
    marks = ""
    Timer_lb.config(text="work", bg=YELLOW, fg=fg)
    reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # making it count down in mins and secs instead of whole numbers
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # making it start with 00 on the other side instead of 0
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # making the timer actually count down
    if count >= 0:
        global tt
        canvas.itemconfig(t_down, text=f"{count_min}:{count_sec}")
        tt = window.after(1000, count_down, count - 1)
    else:
        start_counting()
        marks =""
        work_sec = math.floor(reps/2)
        for _ in range(work_sec):
            marks += check_mark
        check_lb.config(text=marks)


# the function we will put as a command in the button
def start_counting():
    global reps
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer_lb.config(text="Break", bg=YELLOW, fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer_lb.config(text="Break", bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        Timer_lb.config(text="work", bg=YELLOW, fg=fg)


# ----------UI-------------------------------------
window = Tk()
window.title("Ghufran`s POMODORO timer :)")
window.configure(bg=YELLOW,padx = 100 , pady = 50)

#making teh canvas and adding teh tomato pic
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112,image=pic )
t_down =canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

#making teh timer label
Timer_lb = Label(text="TIMER",font=(FONT_NAME,50,"bold"),bg=YELLOW,fg = fg)
Timer_lb.grid(row=0,column=1)

#making the check mark
check_lb = Label(font=(FONT_NAME,20,"bold"),bg=YELLOW,fg=fg)
check_lb.grid(row=5,column=1)

#make the start and stop button
button_start = Button(text="start",highlightthickness=0,command = start_counting)
button_start.grid(row=4,column=0)
button_reset = Button(text="reset",highlightthickness=0,command = reset_time)
button_reset.grid(row=4,column=2)

window.mainloop()
