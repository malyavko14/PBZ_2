from Create import *
from Delete import *
from Edit import *
from FiveStarHotel import *
from PriceList import *
from tkinter import *
from tkinter import ttk


def tourClick():
    def buttonCreateTourClickActivator():
        buttonCreateTourClick(table)

    def buttonDeleteTourClickActivator():
        buttonDeleteTourClick(table)

    def buttonEditTourClickActivator():
        buttonEditTourClick(table)

    organizationTable.pack_forget()
    horizontalSliderOrganization.pack_forget()
    verticalSliderOrganization.pack_forget()
    hotelTable.pack_forget()
    verticalSliderHotel.pack_forget()

    table.heading(1, text='Организация')
    table.heading(2, text='Тип тура')
    table.heading(3, text='Начало тура')
    table.heading(4, text='Длительность')
    table.heading(5, text='Начальная точка')
    table.heading(6, text='Отель')
    table.heading(7, text='Вид транспорта')
    table.heading(8, text='Цена')

    buttonCreate = Button(buttonFrame, text='Создать', bg='#7fffd4', command=buttonCreateTourClickActivator)
    buttonDelete = Button(buttonFrame, text='Удалить', bg='#7fffd4', command=buttonDeleteTourClickActivator)
    buttonEdit = Button(buttonFrame, text='Редактировать', bg='#7fffd4', command=buttonEditTourClickActivator)
    buttonFiveStarHotel = Button(buttonFrame, text='Просмотр списка всех 5star отелей', bg='#7fffd4',
                                 command=buttonFiveStarHotelClick)
    buttonPriceList = Button(buttonFrame, text='Прайс лист на дату', bg='#7fffd4', command=buttonPriceListClick)

    horizontalSlider.pack(fill=BOTH)
    verticalSlider.pack(side=RIGHT, fill=BOTH, expand=False)
    table.pack(side=BOTTOM)
    buttonCreate.grid(row=0, column=0, sticky=W)
    buttonDelete.grid(row=0, column=1, sticky=W)
    buttonEdit.grid(row=0, column=2, sticky=W)
    buttonPriceList.grid(row=0, column=3, sticky=W)
    buttonFiveStarHotel.grid(row=0, column=4, sticky=W)
    seeTable(table, 'tour')


def hotelClick():
    def buttonCreateHotelClickActivator():
        buttonCreateHotelClick(hotelTable)

    def buttonDeleteHotelClickActivator():
        buttonDeleteHotelClick(hotelTable)

    def buttonEditHotelClickActivator():
        buttonEditHotelClick(hotelTable)

    organizationTable.pack_forget()
    horizontalSliderOrganization.pack_forget()
    verticalSliderOrganization.pack_forget()
    table.pack_forget()
    verticalSlider.pack_forget()
    horizontalSlider.pack_forget()

    hotelTable.heading(1, text='Название')
    hotelTable.heading(2, text='Количество звёзд')
    hotelTable.heading(3, text='Местоположение')

    buttonCreate = Button(buttonFrame, text='Создать', bg='#7fffd4', command=buttonCreateHotelClickActivator)
    buttonDelete = Button(buttonFrame, text='Удалить', bg='#7fffd4', command=buttonDeleteHotelClickActivator)
    buttonEdit = Button(buttonFrame, text='Редактировать', bg='#7fffd4', command=buttonEditHotelClickActivator)
    buttonFiveStarHotel = Button(buttonFrame, text='Просмотр списка всех 5star отелей', bg='#7fffd4',
                                 command=buttonFiveStarHotelClick)
    buttonPriceList = Button(buttonFrame, text='Прайс лист на дату', bg='#7fffd4', command=buttonPriceListClick)

    verticalSliderHotel.pack(side=RIGHT, fill=BOTH, expand=False)
    hotelTable.pack(side=BOTTOM)
    buttonCreate.grid(row=0, column=0, sticky=W)
    buttonDelete.grid(row=0, column=1, sticky=W)
    buttonEdit.grid(row=0, column=2, sticky=W)
    buttonPriceList.grid(row=0, column=3, sticky=W)
    buttonFiveStarHotel.grid(row=0, column=4, sticky=W)
    seeTable(hotelTable, 'hotel')


def organizationClick():
    def buttonCreateOrganizationClickActivator():
        buttonCreateOrganizationClick(organizationTable)

    def buttonDeleteOrganizationClickActivator():
        buttonDeleteOrganizationClick(organizationTable)

    def buttonEditOrganizationClickActivator():
        buttonEditOrganizationClick(organizationTable)

    table.pack_forget()
    horizontalSlider.pack_forget()
    verticalSlider.pack_forget()
    hotelTable.pack_forget()
    verticalSliderHotel.pack_forget()

    organizationTable.heading(1, text='Название')
    organizationTable.heading(2, text='Телефон')
    organizationTable.heading(3, text='Контактное лицо')
    organizationTable.heading(4, text='Место')
    buttonCreate = Button(buttonFrame, text='Создать', bg='#7fffd4', command=buttonCreateOrganizationClickActivator)
    buttonDelete = Button(buttonFrame, text='Удалить', bg='#7fffd4', command=buttonDeleteOrganizationClickActivator)
    buttonEdit = Button(buttonFrame, text='Редактировать', bg='#7fffd4', command=buttonEditOrganizationClickActivator)
    buttonFiveStarHotel = Button(buttonFrame, text='Просмотр списка всех 5star отелей', bg='#7fffd4',
                                 command=buttonFiveStarHotelClick)
    buttonPriceList = Button(buttonFrame, text='Прайс лист на дату', bg='#7fffd4', command=buttonPriceListClick)

    buttonOrganization.pack(side=LEFT)
    horizontalSliderOrganization.pack(fill=BOTH)
    verticalSliderOrganization.pack(side=RIGHT, fill=BOTH, expand=False)
    organizationTable.pack(side=BOTTOM)
    buttonCreate.grid(row=0, column=0, sticky=W)
    buttonDelete.grid(row=0, column=1, sticky=W)
    buttonEdit.grid(row=0, column=2, sticky=W)
    buttonPriceList.grid(row=0, column=3, sticky=W)
    buttonFiveStarHotel.grid(row=0, column=4, sticky=W)
    seeTable(organizationTable, 'organization')


window = Tk()
window['bg'] = '#ffe4c4'
window.title("Приложение для работы с базами данных")
window.wm_attributes('-alpha', 0.3)
window.geometry('750x450')
window.resizable(height=False, width=False)

canvas = Canvas(window, height=750, width=450)

frame = Frame(window, bg='#ffe4c4')
frame.place(relwidth=1, relheight=0.1, )
interpreterFrame = Frame(window, bg='#ffe4c4')
interpreterFrame.place(rely=0.1, relwidth=1, relheight=0.1)
tableFrame = Frame(window, bg='#ffe4c4')
tableFrame.place(rely=0.2, relwidth=1, relheight=0.7)
buttonFrame = Frame(window, bg='#ffe4c4')
buttonFrame.place(rely=0.9, relwidth=1, relheight=0.1)

title = Label(frame, text='Банк данных туристических путевок сети турбюро', bg='#ffe4c4', font="Arial 16")
title.pack()

buttonTour = Button(interpreterFrame, text='Туры', bg='#7fffd4', height=1, width=25, command=tourClick)
buttonHotel = Button(interpreterFrame, text='Отели', bg='#7fffd4', height=1, width=25, command=hotelClick)
buttonOrganization = Button(interpreterFrame, text='Организации', bg='#7fffd4', height=1, width=25,
                            command=organizationClick)

table = ttk.Treeview(tableFrame, columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height=300)
horizontalSlider = ttk.Scrollbar(tableFrame, orient="horizontal", command=table.xview)
verticalSlider = ttk.Scrollbar(tableFrame, orient="vertical", command=table.yview)
table.configure(xscrollcommand=horizontalSlider.set)
table.configure(yscrollcommand=verticalSlider.set)

hotelTable = ttk.Treeview(tableFrame, columns=(1, 2, 3), show='headings', height=300)
verticalSliderHotel = ttk.Scrollbar(tableFrame, orient="vertical", command=hotelTable.yview)
hotelTable.configure(yscrollcommand=verticalSliderHotel.set)

organizationTable = ttk.Treeview(tableFrame, columns=(1, 2, 3, 4), show='headings', height=300)
horizontalSliderOrganization = ttk.Scrollbar(tableFrame, orient="horizontal", command=organizationTable.xview)
verticalSliderOrganization = ttk.Scrollbar(tableFrame, orient="vertical", command=organizationTable.yview)
organizationTable.configure(xscrollcommand=horizontalSliderOrganization.set)
organizationTable.configure(yscrollcommand=verticalSliderOrganization.set)

buttonTour.pack(side=LEFT)
buttonHotel.pack(side=LEFT)
buttonOrganization.pack(side=LEFT)

tourClick()

window.mainloop()
