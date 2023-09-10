from tkinter import *
window = Tk()
window.configure(bg="lightpink")
window.geometry("400x600")
window.title("Interest Rate Calculator")

head_label = Label(window , text="INTEREST RATE CALCULATOR" , font=("arial" , 18 , "bold")  , bg="lightpink" , fg="black")
head_label.place(x=20 , y=40)

p_label = Label(window , text="Principal Ammount (rs): " , font=("arial" , 16 , "bold")  , bg="lightpink" , fg="black")
p_label.place(x=10 , y=100)

principal = Entry(window  , text="" ,  bd=2 , width=15)
principal.place(x = 260 , y=100)


R_label = Label(window , text="Interest Rate (%): " , font=("arial" , 16 , "bold")  , bg="lightpink" , fg="black")
R_label.place(x=10 , y=160)

rate = Entry(window  , text="" ,  bd=2 , width=15)
rate.place(x = 200 , y=160)


t_label = Label(window , text="Time Interval (years): " , font=("arial" , 16 , "bold")  , bg="lightpink" , fg="black")
t_label.place(x=10 , y=220)
time = Entry(window  , text="" ,  bd=2 , width=15)
time.place(x = 250 , y=220)

def cal_rate():
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())
    interest = (p*r*t)/100
    interest = round(interest , 2)

    result_label.destroy()
    output = Label(result_frame , text="Your interest ammount is "+ str(interest) , width=30 , fg="black" , bg="lightpink" , font=("arial" , 14 , 'bold'))
    output.place(x=5 , y=5)
    output.pack()

cal_button = Button(window , text="calculate" , fg="black" , bg="lightblue" , bd=4 , command= cal_rate , width=20)
cal_button.place(x=100 , y=260)

result_frame = LabelFrame(window , text="result" , bg="lightpink" , font=('arial' ,16 , 'bold') )
result_frame.pack(padx = 20 , pady=20)
result_frame.place(x=20 , y=300)

result_label = Label(result_frame , text=" " , font=("arial" , 14 , "bold") , fg="black" , bg="lightpink" ,width=20)
result_label.place(x=20 , y=20)
result_label.pack()



window.mainloop()