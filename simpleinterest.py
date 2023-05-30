from tkinter import *
window = Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='#FFB4A2')

def calculate_simpleInterest():
    rate=int(rate_entry.get())
    principal=int(principal_entry.get())
    time=int(time_entry.get())
    simpleInterest=(principal*rate*time)/100
    simpleInterest=round(simpleInterest, 1)
    name=username.get()
    result_label.destroy()
    output_message = Label(result_frame, text=name+", your simpleInterest value is "+str(simpleInterest), bg="#FFB4A2", font=("Calibri",12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()
    
app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "#463618", bg = "#FFB4A2", font=("Calibri", 20),bd=5)
app_label.place(x=20, y=20)

name_label=Label(window, text="Your Name", fg = "#463618", bg = "#FFB4A2", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=175, y=92)

principal_label=Label(window, text="Enter principal value", fg = "#463618", bg = "#FFB4A2", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=125)

principal_entry=Entry(window, text="", bd=2, width=22)
principal_entry.place(x=175, y=127)

rate_label=Label(window, text="Enter rate(%)", fg = "#463618", bg = "#FFB4A2", font=("Calibri", 12),bd=1)
rate_label.place(x=20, y=160)

rate_entry=Entry(window, text="", bd=2, width=22)
rate_entry.place(x=175, y=162)

time_label=Label(window, text="Enter Duration (years)", fg = "#463618", bg = "#FFB4A2", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=200)

time_entry=Entry(window, text="", bd=2, width=22)
time_entry.place(x=175, y=205)

calculate_button=Button(window, text="CALCULATE", fg = "#463618", bg = "#B583AD",bd=5, command=calculate_simpleInterest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg = "#FFB4A2", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "#FFB4A2", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()
