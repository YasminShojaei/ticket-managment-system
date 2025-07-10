from view import *

def reset_form():
    id.set(id.get() + 1)
    name.set("")
    family.set("")
    birth_date.set("")
    user_name.set("")
    password.set("")

def save_btn_click():
    person =(id.get(), name.get() + "" + family.get(), birth_date.get(), user_name.get(), password.get(), is_locked.get(), role.get())
    table.insert("", END, values=person)
    msg.showinfo("Saved", "person saved")
    reset_form()

def clear_btn_click():
    for row in table.get_children():
        table.delete(row)

def edit_btn_click():
    print("Edit")

def cancel_btn_click():
    print("cancel")

def table_select(x):
    selected_user = table.item(table.focus())["values"]
    id.set(selected_user[0])
    name.set(selected_user[1])
    family.set(selected_user[1])
    birth_date.set(selected_user[2])
    user_name.set(selected_user[3])
    password.set(selected_user[4])
    is_locked.set(selected_user[5])
    role.set(selected_user[6])

window = Tk()
window.title("User View")
window.geometry("1000x450")


Label(window, text="id").place(x=10, y=20)
id = IntVar()
Entry(window, textvariable=id).place(x=100, y=20)

Label(window, text="Name").place(x=10, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=60)

Label(window, text="Family").place(x=10, y=100)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=100)

Label(window, text="Birth Date").place(x=10, y=140)
birth_date = StringVar()
Entry(window, textvariable=birth_date).place(x=100, y=140)

Label(window, text="User Name").place(x=10, y=180)
user_name = StringVar()
Entry(window, textvariable=user_name).place(x=100, y=180)

Label(window, text="Password").place(x=10, y=220)
password = StringVar()
Entry(window, textvariable=password).place(x=100, y=220)

Label(window, text="Is Locked").place(x=10, y=260)
is_locked = BooleanVar()

Radiobutton(window, text="True", variable=is_locked, value="True").place(x=95, y=260)
Radiobutton(window, text="False", variable=is_locked, value="False").place(x=150, y=260)


Label(window, text="Role").place(x=10, y=300)
role = StringVar()

Radiobutton(window, text="Customer", variable=role, value="Customer").place(x=95, y=300)
Radiobutton(window, text="Admin", variable=role, value="Admin").place(x=150, y=300)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6, 7], show="headings")

table.heading(1, text="ID")
table.heading(2, text="Name & Family")
table.heading(3, text="Birth Date")
table.heading(4, text="User Name")
table.heading(5, text="Password")
table.heading(6, text="Is Locksd")
table.heading(7, text="Role")

table.column(1, width=70)
table.column(2, width=110)
table.column(3, width=110)
table.column(4, width=110)
table.column(5, width=110)
table.column(6, width=70)
table.column(7, width=110)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=300, y=20 ,height=410)

Button(window, text="Save", command=save_btn_click).place(x=10,y= 350, width=65, height=35)
Button(window, text="Clear", command=clear_btn_click).place(x=85, y=350, width=65, height=35)
Button(window, text="Edit", command=edit_btn_click).place(x=160, y=350, width=65, height=35)
Button(window, text="Cancel", command=cancel_btn_click).place(x=10, y=390, width=215, height=40)


window.mainloop()
