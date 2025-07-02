from tkinter import *
import tkinter.ttk as ttk
from model.data_acsess.ticket_manager import *
from model.entity import ticket
from model.tools.ticket_data_lists import city_values, airline_values

ticket_list = read_from_file()

window = Tk()
window.title("Ticket Info")
window.geometry("1160x500")
window.config(cursor="hand2", background="light blue")


# # load data from file
def load_data(ticket_list):
    for row in table.get_children():
        table.delete(row)

    for ticket in ticket_list:
        table.insert("",END, values=ticket.to_tuple())


# ## btn_function:
# # save_btn
def save_ticket():pass

def edit_ticket():pass

def delete_ticket():pass


# # Clear_btn
def reset_ticket():
    # t_id.set(len(ticket_list) + 1)
    ticket_code.set("")
    source.set("Tehran")
    destination.set("Tabriz")
    airline.set("Iran Air")
    start_date.set("")
    start_time_h.set("")
    start_time_m.set("")
    end_date.set("")
    end_time_h.set("")
    end_time_m.set("")
#
#
# search_btn
def search_ticket():
    pass


def table_select(x):
    selected = table.item(table.focus())["values"]
    if selected:
        selected_ticket = ticket(*selected)
        if selected_ticket:
            t_id.set(selected_ticket.id)
            ticket_code.set(selected_ticket.code)
            source.set(selected_ticket.source)
            destination.set(selected_ticket.destination)
            airline.set(selected_ticket.airline)
            # start_time : "YYYY-MM-DD HH:MM"
            if " " in selected_ticket.start_time:
                start_d, start_t = selected_ticket.start_time.split(" ")
                start_date.set(start_d)
                start_h, start_m = start_t.split(":")
                start_time_h.set(start_h)
                start_time_m.set(start_m)
            else:
                start_date.set(selected_ticket.start_time)
                start_time_h.set("")
                start_time_m.set("")

            # end_time : "YYYY-MM-DD HH:MM"
            if " " in selected_ticket.end_time:
                end_d, end_t = selected_ticket.end_time.split(" ")
                end_date.set(end_d)
                end_h, end_m = end_t.split(":")
                end_time_h.set(end_h)
                end_time_m.set(end_m)
            else:
                end_date.set(selected_ticket.end_time)
                end_time_h.set("")
                end_time_m.set("")
            price.set(selected_ticket.price)
            seat_no.set(selected_ticket.seat_number)


## Entries:

# id
Label(window, text="ticket id:", background="light blue").place(x=20, y=20)
t_id = IntVar(value=1)
Entry(window, textvariable=t_id, state="readonly", width=23).place(x=82, y=20)

# ticket_code
Label(window, text="ticket code:", background="light blue").place(x=20, y=60)
ticket_code = StringVar()
Entry(window, textvariable=ticket_code).place(x=100, y=60)

# source
Label(window, text="source:", background="light blue").place(x=20, y=90)
source = StringVar(value="Tehran")
ttk.Combobox(window, textvariable=source, values=city_values, width=17).place(x=100, y=90)

# destination
Label(window, text="destination:", background="light blue").place(x=20, y=120)
destination = StringVar(value="Tabriz")
ttk.Combobox(window, textvariable=destination, values=city_values, width=17).place(x=100, y=120)

# airline
Label(window, text="airline:", background="light blue").place(x=20, y=150)
airline = StringVar(value="Iran Air")
ttk.Combobox(window, textvariable=airline, values=airline_values, width=17).place(x=100, y=150)

# start_date_time
Label(window, text="start_date_time:", background="light blue").place(x=20, y=180)
# day
start_date = StringVar(value="")
Entry(window, textvariable=start_date, width=8).place(x=110, y=180)
# start_time
# hour
start_time_h = StringVar()
Entry(window, textvariable=start_time_h, width=3).place(x=165, y=180)

Label(window, text=":", background="light blue").place(x=190, y=180)
# minute
start_time_m = StringVar()
Entry(window, textvariable=start_time_m, width=3).place(x=200, y=180)

# end_date_time
Label(window, text="end_date_time:", background="light blue").place(x=20, y=210)
# day
end_date = StringVar(value="")
Entry(window, textvariable=end_date, width=8).place(x=110, y=210)
# end_time
# hour
end_time_h = StringVar()
Entry(window, textvariable=end_time_h, width=3).place(x=165, y=210)

Label(window, text=":", background="light blue").place(x=190, y=210)
# minute
end_time_m = StringVar()
Entry(window, textvariable=end_time_m, width=3).place(x=200, y=210)

# price
Label(window, text="price:", background="light blue").place(x=20, y=240)
price = IntVar(value=0)
Entry(window, textvariable=price, width=14).place(x=100, y=240)
Label(window, text="تومان", background="light blue").place(x=190, y=240)

# seat_number
Label(window, text="seat no.:", background="light blue").place(x=20, y=280)
seat_no = IntVar(value=1)
Entry(window, textvariable=seat_no, width=7).place(x=100, y=280)
# # A-F
# seat_al = StringVar(value="A")
# ttk.Combobox(window, textvariable=seat_al, width=4).place(x=170, y=280)

# search_ticket:

# search_city
Label(window, text="city:", background="light blue").place(x=700, y=360)
search_city = StringVar(value="Tehran")
ttk.Combobox(window, textvariable=search_city, values=city_values, width=17).place(x=730, y=360)

# search_date
Label(window, text="date_time:", background="light blue").place(x=300, y=360)
search_date = StringVar(value="--")
ttk.Combobox(window, textvariable=search_date, width=17).place(x=370, y=360)

## Table:
table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6, 7, 8, 9], show="headings", height=15)

# table_heading
table.heading(1, text="ID")
table.heading(2, text="Code")
table.heading(3, text="Source")
table.heading(4, text="Destination")
table.heading(5, text="Airline")
table.heading(6, text="Start Time")
table.heading(7, text="End Time")
table.heading(8, text="Price")
table.heading(9, text="Seat No")

# table_column
table.column(1, width=60, anchor="center")
table.column(2, width=100, anchor="center")
table.column(3, width=100, anchor="center")
table.column(4, width=100, anchor="center")
table.column(5, width=100, anchor="center")
table.column(6, width=100, anchor="center")
table.column(7, width=100, anchor="center")
table.column(8, width=100, anchor="center")
table.column(9, width=100, anchor="center")

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=265, y=20)

## Buttons:

# save_btn
Button(window, text="Save", width=6, command=save_ticket).place(x=30, y=360)

# edit_btn
Button(window, text="Edit", width=6, command=edit_ticket).place(x=100, y=360)

# remove_btn
Button(window, text="Delete", width=6, command=delete_ticket).place(x=170, y=360)

# reset_btn
Button(window, text="Clear", width=26, command=reset_ticket).place(x=30, y=320)

# search_btn
Button(window, text="Search", width=6, command=search_ticket).place(x=1000, y=360)

# reset_form()

window.mainloop()
