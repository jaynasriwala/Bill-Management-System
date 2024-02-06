from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False, False)

def Reset():
    entry_dosa.delete(0, END)
    entry_coffee.delete(0, END)
    entry_cookies.delete(0, END)
    entry_tea.delete(0, END)
    entry_juice.delete(0, END)

def Total():
    try:
        a1 = int(dosa.get())
    except:
        a1 = 0

    try:
        a2 = int(coffee.get())
    except:
        a2 = 0

    try:
        a3 = int(cookies.get())
    except:
        a3 = 0

    try:
        a4 = int(tea.get())
    except:
        a4 = 0

    try:
        a5 = int(juice.get())
    except:
        a5 = 0

    c1 = 60 * a1
    c2 = 50 * a2
    c3 = 35 * a3
    c4 = 7 * a4
    c5 = 30 * a5

    lbl_total = Label(f2, font=("aria", 20, "bold"), text="-: Total :-", width=17, fg="lightyellow", bg="black")
    lbl_total.place(x=0, y=60)

    totalcost = c1 + c2 + c3 + c4 + c5
    string_bill = "Rs. ", str('%.2f' %totalcost)
    Total_bill.set(string_bill)

    entry_total = Entry(f2, font=("aria", 20, "bold"), textvariable=Total_bill, bd=6, width=15, bg="darkgray")
    entry_total.place(x=20, y=100)


Label(text="Bill Management", font=("Times new roman", 30), width=400, height=2, fg="darkgray", bg="black").pack()

# menu card

f = Frame(root, bg="darkgray", highlightbackground="black", highlightthickness=2, width=300, height=370)
f.place(x=10, y=110)

Label(f, text="-: Menu :-", font=("Gabriola", 30, "bold"), fg="black", bg="darkgray").place(x=80, y=0)

Label(f, font=("Lucida Calligraphy", 15), text="Coffee --------> Rs.50/plate", fg="black", bg="darkgray").place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15), text="Tea --------> Rs.7/plate", fg="black", bg="darkgray").place(x=10, y=110)
Label(f, font=("Lucida Calligraphy", 15), text="Dosa --------> Rs.60/plate", fg="black", bg="darkgray").place(x=10, y=150)
Label(f, font=("Lucida Calligraphy", 15), text="Juice --------> Rs.30/plate", fg="black", bg="darkgray").place(x=10, y=180)
Label(f, font=("Lucida Calligraphy", 15), text="Cookies --------> Rs.35/plate", fg="black", bg="darkgray").place(x=10, y=210)


# Bill

f2 = Frame(root, bg="darkgray", highlightbackground="black", highlightthickness=2, width=300, height=370)
f2.place(x=690, y=118)
Label(f2, text="-: Bill :-", font=("Gabriola", 30, "bold"), fg="black", bg="darkgray").place(x=80, y=0)

# entry work

f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()

dosa = StringVar()
coffee = StringVar()
tea = StringVar()
juice = StringVar()
cookies = StringVar()

lbl_dosa = Label(f1, font=("aria", 20, "bold"), text="Dosa", width=12, fg="blue4")
lbl_coffee = Label(f1, font=("aria", 20, "bold"), text="Coffee", width=12, fg="blue4")
lbl_tea = Label(f1, font=("aria", 20, "bold"), text="Tea", width=12, fg="blue4")
lbl_juice = Label(f1, font=("aria", 20, "bold"), text="Juice", width=12, fg="blue4")
lbl_cookies = Label(f1, font=("aria", 20, "bold"), text="Cookies", width=12, fg="blue4")

lbl_dosa.grid(row=1, column=0)
lbl_coffee.grid(row=2, column=0)
lbl_tea.grid(row=3, column=0)
lbl_juice.grid(row=4, column=0)
lbl_cookies.grid(row=5, column=0)


entry_dosa = Entry(f1, font=("aria", 20, "bold"), textvariable=dosa, bd=6, width=8, bg="lightpink")
entry_coffee = Entry(f1, font=("aria", 20, "bold"), textvariable=coffee, bd=6, width=8, bg="lightpink")
entry_tea = Entry(f1, font=("aria", 20, "bold"), textvariable=tea, bd=6, width=8, bg="lightpink")
entry_juice= Entry(f1, font=("aria", 20, "bold"), textvariable=juice, bd=6, width=8, bg="lightpink")
entry_cookies = Entry(f1, font=("aria", 20, "bold"), textvariable=cookies, bd=6, width=8, bg="lightpink")

entry_dosa.grid(row=1, column=1)
entry_coffee.grid(row=2, column=1)
entry_tea.grid(row=3, column=1)
entry_juice.grid(row=4, column=1)
entry_cookies.grid(row=5, column=1)

# buttons
btn_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)
btn_total = Button(f1, bd=5, fg="black", bg="lightgreen", font=("ariel", 16, "bold"), width=10, text="Total", command=Total)
btn_total.grid(row=8, column=1)

# Variable for displaying total bill
Total_bill = StringVar()

root.mainloop()
