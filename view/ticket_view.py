from model.entity.ticket import Ticket
from model.tools.ticket_data_lists import city_values, airline_values
from controller.ticket_controller import TicketController
from view import *

ticket_controller = TicketController()


class TicketView:

    # ## btn_function:
    # # save_btn
    def save_ticket(self):

        try:
            ticket = Ticket(
                t_id=self.t_id.get(),
                ticket_code=self.ticket_code.get(),
                source=self.source.get(),
                destination=self.destination.get(),
                airline=self.airline.get(),
                start_date=self.start_date.get(),
                end_date=self.end_date.get(),
                price=self.price.get(),
                seat_no=self.seat_no.get(),
                sold=self.sold.get()
            )

            # sold_tag:
            if self.sold.get():
                tag = "Ticket sold"
            elif not self.sold.get():
                tag = "Ticket not sold"
            else:
                msg.showinfo("Info", "somthing went wrong!!!")



            result = ticket_controller.save(ticket)
            for ticket in result:
                self.table.insert("", "end", values=(
                    ticket.t_id,
                    ticket.ticket_code,
                    ticket.source,
                    ticket.destination,
                    ticket.airline,
                    ticket.start_date,
                    ticket.end_date,
                    ticket.price,
                    ticket.seat_no,
                    ticket.sold
                ),tags=tag)

            msg.showinfo("Result", result)
            self.load_table_data()  # جدول رو به‌روز کن

        except Exception as e:
            msg.showerror("Error", str(e))

    def edit_ticket(self):
        try:
            ticket = Ticket(
                t_id=self.t_id.get(),
                ticket_code=self.ticket_code.get(),
                source=self.source.get(),
                destination=self.destination.get(),
                airline=self.airline.get(),
                start_date=self.start_date.get(),
                end_date=self.end_date.get(),
                price=self.price.get(),
                seat_no=self.seat_no.get(),
                sold=self.sold.get()
            )

            result = ticket_controller.edit(ticket)
            msg.showinfo("Result", result)
            self.load_table_data()

        except Exception as e:
            msg.showerror("Error", str(e))

    def delete_ticket(self):
        try:
            selected_item = self.table.focus()
            if not selected_item:
                msg.showerror("Error", "Please select a ticket from the table")
                return

            values = self.table.item(selected_item, "values")
            if not values or len(values) == 0:
                msg.showerror("Error", "Invalid selection")
                return

            t_id = values[0]  # ستون اول جدول شناسه تیکت هست

            confirm = msg.askyesno("Confirm Delete", f"Are you sure you want to delete ticket with ID '{t_id}'?")
            if not confirm:
                return

            result = ticket_controller.remove(t_id)
            msg.showinfo("Result", result)
            self.load_table_data()
            self.reset_ticket()

        except Exception as e:
            msg.showerror("Error", str(e))

        except Exception as e:
            msg.showerror("Error", str(e))

    # # Clear_btn
    def reset_ticket(self):
        self.t_id.set(ticket_controller.get_ticket_count() + 1)
        self.ticket_code.set(111)
        self.source.set("Tehran")
        self.destination.set("Tabriz")
        self.airline.set("Iran Air")
        self.start_date.set("")
        self.start_time_h.set("")
        self.start_time_m.set("")
        self.end_date.set("")
        self.end_time_h.set("")
        self.end_time_m.set("")
        self.price.set(0)
        self.seat_no.set("123")
        self.sold.set(True)

    # search_btn
    def search_ticket(self):
        try:
            city_name = self.search_city.get()
            if not city_name:
                msg.showerror("Error", "Please select a city to search")
                return

            result = ticket_controller.search_by_city(city_name)

            # پاک کردن جدول
            for item in self.table.get_children():
                self.table.delete(item)



            # پر کردن جدول با نتایج
            for ticket in result:
                self.table.insert("", "end", values=(
                    ticket.t_id,
                    ticket.ticket_code,
                    ticket.source,
                    ticket.destination,
                    ticket.airline,
                    ticket.start_date,
                    ticket.end_date,
                    ticket.price,
                    ticket.seat_no,
                    ticket.sold
                ))

            if not result:
                msg.showinfo("Result", "No tickets found for this city.")

        except Exception as e:
            msg.showerror("Error", str(e))

    def load_table_data(self):
        # جدول رو پاک کن
        for item in self.table.get_children():
            self.table.delete(item)

        # لیست جدید بگیر
        ticket_list = ticket_controller.get_all()

        # اضافه کن به جدول
        for ticket in ticket_list:
            self.table.insert("", "end", values=(
                ticket.t_id,
                ticket.ticket_code,
                ticket.source,
                ticket.destination,
                ticket.airline,
                ticket.start_date,
                ticket.end_date,
                ticket.price,
                ticket.seat_no,
                ticket.sold
            ))

    def table_select(self, event):
        selected = self.table.item(self.table.focus())["values"]
        if selected:
            selected_ticket = Ticket(*selected)
            if selected_ticket:
                self.t_id.set(selected_ticket.t_id)
                self.ticket_code.set(selected_ticket.ticket_code)
                self.source.set(selected_ticket.source)
                self.destination.set(selected_ticket.destination)
                self.airline.set(selected_ticket.airline)
                self.start_date.set(selected_ticket.start_date)
                self.end_time_h.set(selected_ticket.end_date)
                self.price.set(selected_ticket.price)
                self.seat_no.set(selected_ticket.seat_no)
                self.sold.set(selected_ticket.sold)

    def __init__(self):
        window = Tk()
        window.title("Ticket Info")
        window.geometry("1260x500")
        window.config(cursor="hand2", background="light blue")

        ## Entries:

        # id
        Label(window, text="ticket id:", background="light blue").place(x=20, y=20)
        self.t_id = IntVar(value=1)
        Entry(window, textvariable=self.t_id, state="readonly", width=23).place(x=82, y=20)

        # ticket_code
        Label(window, text="ticket code:", background="light blue").place(x=20, y=60)
        self.ticket_code = IntVar()
        Entry(window, textvariable=self.ticket_code).place(x=100, y=60)

        # source
        Label(window, text="source:", background="light blue").place(x=20, y=90)
        self.source = StringVar(value="Tehran")
        ttk.Combobox(window, textvariable=self.source, values=city_values, width=17).place(x=100, y=90)

        # destination
        Label(window, text="destination:", background="light blue").place(x=20, y=120)
        self.destination = StringVar(value="Tabriz")
        ttk.Combobox(window, textvariable=self.destination, values=city_values, width=17).place(x=100, y=120)

        # airline
        Label(window, text="airline:", background="light blue").place(x=20, y=150)
        self.airline = StringVar(value="Iran Air")
        ttk.Combobox(window, textvariable=self.airline, values=airline_values, width=17).place(x=100, y=150)

        # start_date_time
        Label(window, text="start_date_time:", background="light blue").place(x=20, y=180)
        # day
        self.start_date = StringVar()
        Entry(window, textvariable=self.start_date, width=8).place(x=110, y=180)
        # start_time
        # hour
        self.start_time_h = StringVar()
        Entry(window, textvariable=self.start_time_h, width=3).place(x=165, y=180)

        Label(window, text=":", background="light blue").place(x=190, y=180)
        # minute
        self.start_time_m = StringVar()
        Entry(window, textvariable=self.start_time_m, width=3).place(x=200, y=180)

        # end_date_time
        Label(window, text="end_date_time:", background="light blue").place(x=20, y=210)
        # day
        self.end_date = StringVar()
        Entry(window, textvariable=self.end_date, width=8).place(x=110, y=210)
        # end_time
        # hour
        self.end_time_h = StringVar()
        Entry(window, textvariable=self.end_time_h, width=3).place(x=165, y=210)

        Label(window, text=":", background="light blue").place(x=190, y=210)
        # minute
        self.end_time_m = StringVar()
        Entry(window, textvariable=self.end_time_m, width=3).place(x=200, y=210)

        # price
        Label(window, text="price:", background="light blue").place(x=20, y=240)
        self.price = IntVar(value=0)
        Entry(window, textvariable=self.price, width=14).place(x=100, y=240)
        Label(window, text="تومان", background="light blue").place(x=190, y=240)

        # seat_number
        Label(window, text="seat no.:", background="light blue").place(x=20, y=280)
        self.seat_no = StringVar(value="123")
        Entry(window, textvariable=self.seat_no, width=7).place(x=100, y=280)
        # # A-F
        # seat_al = StringVar(value="A")
        # ttk.Combobox(window, textvariable=seat_al, width=4).place(x=170, y=280)

        # search_ticket:

        # search_city
        Label(window, text="city:", background="light blue").place(x=700, y=360)
        self.search_city = StringVar(value="Tehran")
        ttk.Combobox(window, textvariable=self.search_city, values=city_values, width=17).place(x=730, y=360)

        # search_date
        Label(window, text="date_time:", background="light blue").place(x=300, y=360)
        self.search_date = StringVar(value="--")
        ttk.Combobox(window, textvariable=self.search_date, width=17).place(x=370, y=360)

        # sold_checkbox:
        self.sold = BooleanVar()
        Checkbutton(window, text="Sold", variable=self.sold, background="light blue").place(x=159, y=280)

        ## Table:
        self.table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], show="headings", height=15)

        # table_heading
        self.table.heading(1, text="ID")
        self.table.heading(2, text="Code")
        self.table.heading(3, text="Source")
        self.table.heading(4, text="Destination")
        self.table.heading(5, text="Airline")
        self.table.heading(6, text="Start Time")
        self.table.heading(7, text="End Time")
        self.table.heading(8, text="Price")
        self.table.heading(9, text="Seat No")
        self.table.heading(10, text="Sold Status")

        # table_column
        self.table.column(1, width=60, anchor="center")
        self.table.column(2, width=100, anchor="center")
        self.table.column(3, width=100, anchor="center")
        self.table.column(4, width=100, anchor="center")
        self.table.column(5, width=100, anchor="center")
        self.table.column(6, width=100, anchor="center")
        self.table.column(7, width=100, anchor="center")
        self.table.column(8, width=100, anchor="center")
        self.table.column(9, width=100, anchor="center")
        self.table.column(10, width=100, anchor="center")

        # table_tags
        self.table.tag_configure("Ticket sold", background="light green")
        self.table.tag_configure("Ticket not sold", background="black")

        self.table.bind("<<TreeviewSelect>>", self.table_select)

        self.table.place(x=265, y=20)

        ## Buttons:

        # save_btn
        Button(window, text="Save", width=6, command=self.save_ticket).place(x=30, y=360)

        # edit_btn
        Button(window, text="Edit", width=6, command=self.edit_ticket).place(x=100, y=360)

        # remove_btn
        Button(window, text="Delete", width=6, command=self.delete_ticket).place(x=170, y=360)

        # reset_btn
        Button(window, text="Clear", width=26, command=self.reset_ticket).place(x=30, y=320)

        # search_btn
        Button(window, text="Search", width=6, command=self.search_ticket).place(x=1000, y=360)

        self.reset_ticket()

        window.mainloop()
