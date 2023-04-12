from tkinter import *
import backend

selected_row = []


def selected(event):
    global selected_row
    index = list.curselection()
    selected_row = list.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_row[1])
    e2.delete(0, END)
    e2.insert(END, selected_row[2])
    e3.delete(0, END)
    e3.insert(END, selected_row[3])
    e4.delete(0, END)
    e4.insert(END, selected_row[4])
    e5.delete(0, END)
    e5.insert(END, selected_row[5])
    e6.delete(0, END)
    e6.insert(END, selected_row[6])


def delete_cmd():
    backend.delete(selected_row[0])
    view_cmd()


def view_cmd():
    list.delete(0, END)
    for row in backend.view():
        list.insert(END, row)


def search_cmd():
    list.delete(0, END)
    for row in backend.search(date_text.get(), earnings_text.get(), exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get()):
        list.insert(END, row)


def add_cmd():
    backend.insert(date_text.get(), earnings_text.get(), exercise_text.get(
    ), study_text.get(), diet_text.get(), expense_text.get())
    list.delete(0, END)
    list.insert(END, (date_text.get(), earnings_text.get(), exercise_text.get(
    ), study_text.get(), diet_text.get(), expense_text.get()))


def edit_cmd():
    global selected_row
    backend.edit(selected_row[0], date_text.get(), earnings_text.get(),
                 exercise_text.get(), study_text.get(), diet_text.get(), expense_text.get())
    list.delete(0, END)
    for row in backend.view():
        list.insert(END, row)


win = Tk()

win.wm_title("Daily Routine")

l1 = Label(win, text="Date", bg="white", fg="dark orange",
           font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l1.grid(row=0, column=0, sticky=N+S+E+W)

l2 = Label(win, text="Earnings", bg="white", fg="dark orange",
           font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l2.grid(row=0, column=2, sticky=N+S+E+W)

l3 = Label(win, text="Exercise", bg="white", fg="dark orange",
           font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l3.grid(row=1, column=0, sticky=N+S+E+W)

l4 = Label(win, text="Study", bg="white", fg="dark orange",
           font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l4.grid(row=1, column=2, sticky=N+S+E+W)

l5 = Label(win, text="Diet", bg="white", fg="dark orange",
           font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l5.grid(row=2, column=0, sticky=N+S+E+W)

l6 = Label(win, text="Expense", bg="white", fg="dark orange",
           font="Lato 12", borderwidth=2, relief="groove", padx="4", pady="4")
l6.grid(row=2, column=2, sticky=N+S+E+W)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0, column=1)

earnings_text = StringVar()
e2 = Entry(win, textvariable=earnings_text)
e2.grid(row=0, column=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable=exercise_text)
e3.grid(row=1, column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=1, column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable=diet_text)
e5.grid(row=2, column=1)

expense_text = StringVar()
e6 = Entry(win, textvariable=expense_text)
e6.grid(row=2, column=3)

list = Listbox(win, height=15, width=40)
list.grid(row=3, column=0, rowspan=10, columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=9)

list.bind('<<ListboxSelect>>', selected)

b1 = Button(win, text='ADD', width=12, pady=5, command=add_cmd, bg="white", fg="blue",
            font="Lato 12", borderwidth=2, relief="groove")
b1.grid(row=3, column=3)

b2 = Button(win, text='EDIT', width=12, pady=5, command=edit_cmd, bg="white", fg="blue",
            font="Lato 12", borderwidth=2, relief="groove")
b2.grid(row=4, column=3)

b3 = Button(win, text='SEARCH', width=12, pady=5, command=search_cmd, bg="white", fg="blue",
            font="Lato 12", borderwidth=2, relief="groove")
b3.grid(row=5, column=3)

b4 = Button(win, text='DELETE', width=12, pady=5, command=delete_cmd, bg="white", fg="blue",
            font="Lato 12", borderwidth=2, relief="groove")
b4.grid(row=6, column=3)

b5 = Button(win, text='VIEW', width=12, pady=5, command=view_cmd, bg="white", fg="blue",
            font="Lato 12", borderwidth=2, relief="groove")
b5.grid(row=7, column=3)

b6 = Button(win, text='CLOSE', width=12, pady=5, command=win.destroy, bg="white", fg="blue",
            font="Lato 12", borderwidth=2, relief="groove")
b6.grid(row=8, column=3)

win.mainloop()
