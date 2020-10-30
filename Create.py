from SQL import *
from tkinter import *
from tkinter import messagebox as mbox


def seeTable(table, tableName):
    x = table.get_children()
    for item in x:
        table.delete(item)

    cursor.execute(f'SELECT * FROM {tableName} ')
    rows = cursor.fetchall()
    for i in rows:
        table.insert('', 'end', values=i)


def buttonCreateTourClick(table):
    def buttonSave():
        cursor.execute(f"SELECT * FROM tour WHERE organizations = '{organizations.get()}' AND typeOfTrip = "
                       f"'{typeOfTrip.get()}' AND startDate = '{startDate.get()}' AND duration = {duration.get()} AND "
                       f"departurePoint ='{departurePoint.get()}' AND  hotel = '{hotel.get()}' AND transport= "
                       f"'{transport.get()}' AND price= {price.get()} ")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO tour  (organizations, typeOfTrip, startDate, duration, departurePoint, "
                           f"hotel, transport, price) VALUES(?,?,?,?,?,?,?,?)",
                           (str(organizations.get()), str(typeOfTrip.get()), str(startDate.get()), int(duration.get()),
                            str(departurePoint.get()), str(hotel.get()), str(transport.get()), float(price.get())))
            db.commit()
            mbox.showinfo("Успешно", "Новый тур добавлен")
            seeTable(table, 'tour')
        else:
            print('Такая строка имеется!')
        entryWindow.destroy()

    entryWindow = Toplevel()
    entryWindow.title("Создание тура")
    entryWindow.resizable(False, False)
    Label(entryWindow, text="Организация").grid(row=0, column=0)
    Label(entryWindow, text="Тип тура").grid(row=1, column=0)
    Label(entryWindow, text="Начало тура").grid(row=2, column=0)
    Label(entryWindow, text="Длительность").grid(row=3, column=0)
    Label(entryWindow, text="Начальная точка").grid(row=4, column=0)
    Label(entryWindow, text="Отель").grid(row=5, column=0)
    Label(entryWindow, text="Вид транспорта").grid(row=6, column=0)
    Label(entryWindow, text="Цена").grid(row=7, column=0)

    organizations = Entry(entryWindow, width=15)
    organizations.grid(row=0, column=3, sticky=W)
    typeOfTrip = Entry(entryWindow, width=15)
    typeOfTrip.grid(row=1, column=3, sticky=W)
    startDate = Entry(entryWindow, width=15)
    startDate.grid(row=2, column=3, sticky=W)
    duration = Entry(entryWindow, width=15)
    duration.grid(row=3, column=3, sticky=W)
    departurePoint = Entry(entryWindow, width=15)
    departurePoint.grid(row=4, column=3, sticky=W)
    hotel = Entry(entryWindow, width=15)
    hotel.grid(row=5, column=3, sticky=W)
    transport = Entry(entryWindow, width=15)
    transport.grid(row=6, column=3, sticky=W)
    price = Entry(entryWindow, width=15)
    price.grid(row=7, column=3, sticky=W)
    buttonSave = Button(entryWindow, text='Создать', bg='#7fffd4', command=buttonSave)
    buttonSave.grid(row=8, column=3, sticky=W)


def buttonCreateHotelClick(hotelTable):
    def buttonSave():

        cursor.execute(f"SELECT * FROM hotel WHERE hotelName= '{hotelName.get()}' AND numberOfStar = "
                       f"{numberOfStar.get()} AND location = '{location.get()}' ")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO hotel (hotelName, numberOfStar, location) VALUES(?,?,?)",
                           (hotelName.get(), numberOfStar.get(), location.get(),))
            db.commit()
            mbox.showinfo("Успешно", "Новый тур добавлен")
            seeTable(hotelTable, 'hotel')
        else:
            print('Такая строка имеется!')
        entryWindow.destroy()

    entryWindow = Toplevel()
    entryWindow.title("Создание гостиницы")
    entryWindow.resizable(False, False)
    Label(entryWindow, text="Название отеля").grid(row=0, column=0)
    Label(entryWindow, text="Количество звёзд").grid(row=1, column=0)
    Label(entryWindow, text="Местонахождение").grid(row=2, column=0)
    Label(entryWindow, text="Длительность").grid(row=3, column=0)

    hotelName = Entry(entryWindow, width=15)
    hotelName.grid(row=0, column=3, sticky=W)
    numberOfStar = Entry(entryWindow, width=15)
    numberOfStar.grid(row=1, column=3, sticky=W)
    location = Entry(entryWindow, width=15)
    location.grid(row=2, column=3, sticky=W)
    buttonSave = Button(entryWindow, text='Создать', bg='#7fffd4', command=buttonSave)
    buttonSave.grid(row=3, column=3, sticky=W)


def buttonCreateOrganizationClick(organizationTable):
    def buttonSave():
        cursor.execute(f"SELECT * FROM organization WHERE organizationName = '{organizationName.get()}' AND telephone ="
                       f"'{telephone.get()}' AND contact = '{contact.get()}' AND location= '{location.get()}' ")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO organization  (organizationName ,telephone, contact, location) "
                           f"VALUES(?,?,?,?)",
                           (organizationName.get(), telephone.get(), contact.get(), location.get()))
            db.commit()
            mbox.showinfo("Успешно", "Новый тур добавлен")
            seeTable(organizationTable, 'organization')
        else:
            print('Такая строка имеется!')
        entryWindow.destroy()

    entryWindow = Toplevel()
    entryWindow.title("Создание организации")
    entryWindow.resizable(False, False)
    Label(entryWindow, text="Организация").grid(row=0, column=0)
    Label(entryWindow, text="Телефон").grid(row=1, column=0)
    Label(entryWindow, text="Контактное лицо").grid(row=2, column=0)
    Label(entryWindow, text="Местонахождение").grid(row=3, column=0)

    organizationName = Entry(entryWindow, width=15)
    organizationName.grid(row=0, column=3, sticky=W)
    telephone = Entry(entryWindow, width=15)
    telephone.grid(row=1, column=3, sticky=W)
    contact = Entry(entryWindow, width=15)
    contact.grid(row=2, column=3, sticky=W)
    location = Entry(entryWindow, width=15)
    location.grid(row=3, column=3, sticky=W)
    buttonSave = Button(entryWindow, text='Создать', bg='#7fffd4', command=buttonSave)
    buttonSave.grid(row=8, column=3, sticky=W)
