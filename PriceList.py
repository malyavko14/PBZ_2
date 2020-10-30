from SQL import *
from tkinter import *
from tkinter import ttk


def buttonPriceListClick():
    def filterTable():
        tableWindow = Toplevel()
        tableWindow.title(f"Туры на дату{date.get()}")
        tableWindow.resizable(False, False)
        tableWindow.geometry('750x250')
        filterTable = ttk.Treeview(tableWindow, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), show='headings')
        horizontalSliderFilter = ttk.Scrollbar(tableWindow, orient="horizontal", command=filterTable.xview)
        verticalSliderFilter = ttk.Scrollbar(tableWindow, orient="vertical", command=filterTable.yview)
        filterTable.configure(xscrollcommand=horizontalSliderFilter.set)
        filterTable.configure(yscrollcommand=verticalSliderFilter.set)
        filterTable.heading(1, text='Организация')
        filterTable.heading(2, text='Телефон')
        filterTable.heading(3, text='Контактное лицо')
        filterTable.heading(4, text='Адрес')
        filterTable.heading(5, text='Тип тура')
        filterTable.heading(6, text='Начало тура')
        filterTable.heading(7, text='Длительность')
        filterTable.heading(8, text='Начальная точка')
        filterTable.heading(9, text='Отель')
        filterTable.heading(10, text='Вид транспорта')
        filterTable.heading(11, text='Цена')
        horizontalSliderFilter.pack(fill=BOTH)
        verticalSliderFilter.pack(side=RIGHT, fill=BOTH, expand=False)
        filterTable.pack(side=BOTTOM)

        cursor.execute(f'SELECT organization.*, tour.typeOfTrip, tour.duration,  tour.startDate, tour.departurePoint, '
                       f'tour.hotel, tour.transport, tour.price FROM tour '
                       f'INNER JOIN organization ON organization.organizationName = tour.organizations '
                       f'WHERE tour.startDate = "{date.get()}" ')
        rows = cursor.fetchall()
        for i in rows:
            filterTable.insert('', 'end', values=i)

        filterWindow.destroy()

    filterWindow = Toplevel()
    filterWindow.title("Введите дату")
    filterWindow.resizable(False, False)
    Label(filterWindow, text="Введите информацию:").grid(row=0, column=0)
    Label(filterWindow, text="Дата").grid(row=1, column=0)
    date = Entry(filterWindow, width=15)
    date.grid(row=1, column=3, sticky=W)
    buttonSave = Button(filterWindow, text='Выбрать', bg='#7fffd4', command=filterTable)
    buttonSave.grid(row=8, column=3, sticky=W)
