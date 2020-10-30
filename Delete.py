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


def buttonDeleteTourClick(table):
    def buttonDelete():
        cursor.execute(f"DELETE FROM tour WHERE organizations = '{organizations.get()}' AND typeOfTrip = "
                       f"'{typeOfTrip.get()}' AND price = {price.get()}")
        db.commit()
        seeTable(table, 'tour')
        mbox.showinfo("Успешно", "Тур удалён")
        deleteWindow.destroy()

    deleteWindow = Toplevel()
    deleteWindow.title("Удаление тура")
    deleteWindow.resizable(False, False)
    Label(deleteWindow, text="Введите информацию:").grid(row=0, column=0)
    Label(deleteWindow, text="Организация").grid(row=1, column=0)
    Label(deleteWindow, text="Тип тура").grid(row=2, column=0)
    Label(deleteWindow, text="Цена").grid(row=3, column=0)
    organizations = Entry(deleteWindow, width=15)
    organizations.grid(row=1, column=3, sticky=W)
    typeOfTrip = Entry(deleteWindow, width=15)
    typeOfTrip.grid(row=2, column=3, sticky=W)
    price = Entry(deleteWindow, width=15)
    price.grid(row=3, column=3, sticky=W)
    buttonSave = Button(deleteWindow, text='Удалить', bg='#7fffd4', command=buttonDelete)
    buttonSave.grid(row=8, column=3, sticky=W)


def buttonDeleteHotelClick(hotelTable):
    def buttonDelete():
        cursor.execute(f"DELETE FROM hotel WHERE hotelName = '{hotelName.get()}' AND numberOfStar = "
                       f"'{numberOfStar.get()}' AND location = {location.get()}")
        db.commit()
        seeTable(hotelTable, 'hotel')
        mbox.showinfo("Успешно", "Тур удалён")
        deleteWindow.destroy()

    deleteWindow = Toplevel()
    deleteWindow.title("Удаление отеля")
    deleteWindow.resizable(False, False)
    Label(deleteWindow, text="Введите информацию:").grid(row=0, column=0)
    Label(deleteWindow, text="Название отеля").grid(row=1, column=0)
    Label(deleteWindow, text="Количество звёзд").grid(row=2, column=0)
    Label(deleteWindow, text="Местоположение").grid(row=3, column=0)
    hotelName = Entry(deleteWindow, width=15)
    hotelName.grid(row=1, column=3, sticky=W)
    numberOfStar = Entry(deleteWindow, width=15)
    numberOfStar.grid(row=2, column=3, sticky=W)
    location = Entry(deleteWindow, width=15)
    location.grid(row=3, column=3, sticky=W)
    buttonSave = Button(deleteWindow, text='Удалить', bg='#7fffd4', command=buttonDelete)
    buttonSave.grid(row=8, column=3, sticky=W)


def buttonDeleteOrganizationClick(organizationTable):
    def buttonDelete():
        cursor.execute(f"DELETE FROM organization WHERE organizationName = '{organizationName.get()}' AND telephone = "
                       f"'{location.get()}'")
        db.commit()
        seeTable(organizationTable, 'organization')
        mbox.showinfo("Успешно", "Тур удалён")
        deleteWindow.destroy()

    deleteWindow = Toplevel()
    deleteWindow.title("Удаление тура")
    deleteWindow.resizable(False, False)
    Label(deleteWindow, text="Введите информацию:").grid(row=0, column=0)
    Label(deleteWindow, text="Организация").grid(row=1, column=0)
    Label(deleteWindow, text="Местонахождение").grid(row=2, column=0)
    organizationName = Entry(deleteWindow, width=15)
    organizationName.grid(row=1, column=3, sticky=W)
    location = Entry(deleteWindow, width=15)
    location.grid(row=2, column=3, sticky=W)
    buttonSave = Button(deleteWindow, text='Удалить', bg='#7fffd4', command=buttonDelete)
    buttonSave.grid(row=8, column=3, sticky=W)
