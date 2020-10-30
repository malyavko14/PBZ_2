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


def buttonEditTourClick(table):
    def buttonEditSave():
        cursor.execute(
            f"UPDATE tour SET organizations= '{organizationsAfter.get()}', typeOfTrip ='{typeOfTripAfter.get()}',"
            f"startDate='{startDateAfter.get()}', duration ={int(durationAfter.get())}, departurePoint = "
            f"'{departurePointAfter.get()}', hotel = '{hotelAfter.get()}', transport = '{transportAfter.get()}',  "
            f"price ={float(priceAfter.get())} WHERE organizations = '{organizationsBefore.get()}' AND "
            f"typeOfTrip ='{typeOfTripBefore.get()}' AND startDate='{startDateBefore.get()}' AND duration ="
            f"{int(durationBefore.get())} AND departurePoint = '{departurePointBefore.get()}' AND hotel = "
            f"'{hotelBefore.get()}'AND transport = '{transportBefore.get()}' AND price ={float(priceBefore.get())}")
        db.commit()
        mbox.showinfo("Успешно", "Новый тур добавлен")
        seeTable(table, 'tour')
        editWindow.destroy()

    editWindow = Toplevel()
    editWindow.title("Изменение данных")
    editWindow.resizable(False, False)
    Label(editWindow, text="Введите информацию о туре который хотите изменить и его изменения:").grid(row=0, column=0,
                                                                                                      columnspan=3)
    Label(editWindow, text="Организация").grid(row=1, column=0)
    Label(editWindow, text="Тип тура").grid(row=2, column=0)
    Label(editWindow, text="Дата").grid(row=3, column=0)
    Label(editWindow, text="Длительность").grid(row=4, column=0)
    Label(editWindow, text="Начальная точка").grid(row=5, column=0)
    Label(editWindow, text="Отель").grid(row=6, column=0)
    Label(editWindow, text="Вид транспорта").grid(row=7, column=0)
    Label(editWindow, text="Цена").grid(row=8, column=0)
    organizationsBefore = Entry(editWindow, width=15)
    organizationsBefore.grid(row=1, column=1, sticky=W)
    typeOfTripBefore = Entry(editWindow, width=15)
    typeOfTripBefore.grid(row=2, column=1, sticky=W)
    startDateBefore = Entry(editWindow, width=15)
    startDateBefore.grid(row=3, column=1, sticky=W)
    durationBefore = Entry(editWindow, width=15)
    durationBefore.grid(row=4, column=1, sticky=W)
    departurePointBefore = Entry(editWindow, width=15)
    departurePointBefore.grid(row=5, column=1, sticky=W)
    hotelBefore = Entry(editWindow, width=15)
    hotelBefore.grid(row=6, column=1, sticky=W)
    transportBefore = Entry(editWindow, width=15)
    transportBefore.grid(row=7, column=1, sticky=W)
    priceBefore = Entry(editWindow, width=15)
    priceBefore.grid(row=8, column=1, sticky=W)
    organizationsAfter = Entry(editWindow, width=15)
    organizationsAfter.grid(row=1, column=2, sticky=W)
    typeOfTripAfter = Entry(editWindow, width=15)
    typeOfTripAfter.grid(row=2, column=2, sticky=W)
    startDateAfter = Entry(editWindow, width=15)
    startDateAfter.grid(row=3, column=2, sticky=W)
    durationAfter = Entry(editWindow, width=15)
    durationAfter.grid(row=4, column=2, sticky=W)
    departurePointAfter = Entry(editWindow, width=15)
    departurePointAfter.grid(row=5, column=2, sticky=W)
    hotelAfter = Entry(editWindow, width=15)
    hotelAfter.grid(row=6, column=2, sticky=W)
    transportAfter = Entry(editWindow, width=15)
    transportAfter.grid(row=7, column=2, sticky=W)
    priceAfter = Entry(editWindow, width=15)
    priceAfter.grid(row=8, column=2, sticky=W)
    buttonSave = Button(editWindow, text='Создать', bg='#7fffd4', command=buttonEditSave)
    buttonSave.grid(row=9, column=1, sticky=W)


def buttonEditHotelClick(hotelTable):
    def buttonEditSave():
        cursor.execute(f"UPDATE hotel SET hotelName= '{hotelNameAfter.get()}', numberOfStar ={numberOfStarAfter.get()},"
                       f"location='{locationAfter.get()}' WHERE hotelName = '{hotelNameBefore.get()}' AND "
                       f"numberOfStar ='{numberOfStarBefore.get()}' AND location='{locationBefore.get()}'")
        db.commit()
        mbox.showinfo("Успешно", "Новый тур добавлен")
        seeTable(hotelTable, 'hotel')
        editWindow.destroy()

    editWindow = Toplevel()
    editWindow.title("Изменение данных")
    editWindow.resizable(False, False)
    Label(editWindow, text="Введите информацию о отеле который хотите изменить и его изменения:").grid(row=0, column=0,
                                                                                                       columnspan=3)
    Label(editWindow, text="Название отеля").grid(row=1, column=0)
    Label(editWindow, text="Количество звёзд").grid(row=2, column=0)
    Label(editWindow, text="Местонахождение").grid(row=3, column=0)
    hotelNameBefore = Entry(editWindow, width=15)
    hotelNameBefore.grid(row=1, column=1, sticky=W)
    numberOfStarBefore = Entry(editWindow, width=15)
    numberOfStarBefore.grid(row=2, column=1, sticky=W)
    locationBefore = Entry(editWindow, width=15)
    locationBefore.grid(row=3, column=1, sticky=W)
    hotelNameAfter = Entry(editWindow, width=15)
    hotelNameAfter.grid(row=1, column=2, sticky=W)
    numberOfStarAfter = Entry(editWindow, width=15)
    numberOfStarAfter.grid(row=2, column=2, sticky=W)
    locationAfter = Entry(editWindow, width=15)
    locationAfter.grid(row=3, column=2, sticky=W)
    buttonSave = Button(editWindow, text='Создать', bg='#7fffd4', command=buttonEditSave)
    buttonSave.grid(row=9, column=1, sticky=W)


def buttonEditOrganizationClick(organizationTable):
    def buttonEditSave():
        cursor.execute(f"UPDATE hotel SET organizationName= '{organizationNameAfter.get()}', telephone ="
                       f"'{telephoneAfter.get()}', location='{locationAfter.get()},' contact='{contactAfter.get()} "
                       f"WHERE organizationName = '{organizationNameBefore.get()}' AND "
                       f"telephone ='{telephoneBefore.get()}' AND location='{locationBefore.get()}'AND "
                       f"contact='{contactBefore.get()}'")
        db.commit()
        mbox.showinfo("Успешно", "Новый тур добавлен")
        seeTable(organizationTable, 'organization')
        editWindow.destroy()

    editWindow = Toplevel()
    editWindow.title("Изменение данных")
    editWindow.resizable(False, False)
    Label(editWindow, text="Введите информацию о организации который хотите изменить и его изменения:").\
        grid(row=0, column=0, columnspan=3)
    Label(editWindow, text="Название организации").grid(row=1, column=0)
    Label(editWindow, text="Телефон").grid(row=2, column=0)
    Label(editWindow, text="Контактное лицо").grid(row=3, column=0)
    Label(editWindow, text="Местонахождение").grid(row=4, column=0)
    organizationNameBefore = Entry(editWindow, width=15)
    organizationNameBefore.grid(row=1, column=1, sticky=W)
    telephoneBefore = Entry(editWindow, width=15)
    telephoneBefore.grid(row=2, column=1, sticky=W)
    contactBefore = Entry(editWindow, width=15)
    contactBefore.grid(row=3, column=1, sticky=W)
    locationBefore = Entry(editWindow, width=15)
    locationBefore.grid(row=4, column=1, sticky=W)
    organizationNameAfter = Entry(editWindow, width=15)
    organizationNameAfter.grid(row=1, column=2, sticky=W)
    telephoneAfter = Entry(editWindow, width=15)
    telephoneAfter.grid(row=2, column=2, sticky=W)
    contactAfter = Entry(editWindow, width=15)
    contactAfter.grid(row=3, column=2, sticky=W)
    locationAfter = Entry(editWindow, width=15)
    locationAfter.grid(row=4, column=2, sticky=W)
    buttonSave = Button(editWindow, text='Создать', bg='#7fffd4', command=buttonEditSave)
    buttonSave.grid(row=9, column=1, sticky=W)
