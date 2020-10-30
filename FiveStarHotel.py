from SQL import *
from tkinter import *
from tkinter import ttk


def buttonFiveStarHotelClick():
    filterWindow = Toplevel()
    filterWindow.title("Пятизвёздочные отели")
    filterWindow.resizable(False, False)

    hotelTable = ttk.Treeview(filterWindow, columns=(1, 2, 3), show='headings')
    verticalSliderHotel = ttk.Scrollbar(filterWindow, orient="vertical", command=hotelTable.yview)
    hotelTable.configure(yscrollcommand=verticalSliderHotel.set)
    hotelTable.heading(1, text='Название')
    hotelTable.heading(2, text='Количество звёзд')
    hotelTable.heading(3, text='Местоположение')
    verticalSliderHotel.pack(side=RIGHT, fill=BOTH, expand=False)
    hotelTable.pack(side=BOTTOM)

    cursor.execute('SELECT * FROM hotel WHERE numberOfStar = 5 ')
    rows = cursor.fetchall()

    for i in rows:
        hotelTable.insert('', 'end', values=i)
