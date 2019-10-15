"ASUS\SQLEXPRESS2017"

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ASUS\SQLEXPRESS2017;'
                      'Database=BATTALGAZI_DELIGHT;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('select * from BATTALGAZI_DELIGHT.dbo.CITY order by city_id')

for row in cursor:
    print(row)


