import sqlite3
db = sqlite3.connect('tables')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tour(
organizations char,
typeOfTrip char,
startDate char,
duration int,
departurePoint char,
hotel char,
transport char,
price decimal(5, 2)
)""")
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS hotel(
hotelName char,
numberOfStar int,
location char
)""")
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS organization(
organizationName char,
telephone char,
contact char,
location char
)""")
db.commit()
