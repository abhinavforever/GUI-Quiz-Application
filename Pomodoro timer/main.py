import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps=0
timer=None

from tkinter import *
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0
    canvas.itemconfig(timer_text,text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps in [2,4,6,8]:
        check_marks.config(text=check_marks['text']+"✔")

    if reps == 1 or reps==3 or reps==5 or reps==7:
        title_label['fg'] = GREEN
        title_label['text']="Work"
        count_down(work_sec)
    elif reps==8:
        title_label['text'] = "Break"
        title_label['fg']=RED
        count_down(long_break_sec)
    elif reps in [2,4,6]:
        title_label['text'] = "Break"
        title_label['fg'] = PINK
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60) #or use count//60 i.e. floor division
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,140,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


title_label=Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
title_label.grid(row=0, column=1)

start_button=Button(text="Start", font=(FONT_NAME, 10, "bold"),highlightthickness=0,command=start_timer)
start_button.grid(row=2, column=0)

window.bind('')
reset_button=Button(text="Reset", font=(FONT_NAME, 10, "bold"),highlightthickness=0,command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks=Label(text="", fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW, highlightthickness=0)
check_marks.grid(row=3, column=1)

window.mainloop()