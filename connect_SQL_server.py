'''
le minh huu @LeHuu02 ictu - 8/12/2022
connection data from python to sql server
pip install pyodbc
'''
import pyodbc

#my price data

#loop through all the drivers we have access to
for driver in pyodbc.drivers():
    print(driver)

#driver name: DESKTOP-TQQ9EUA
#define the server name and the database name
server = 'DESKTOP-TQQ9EUA'
database = 'Python_test'

#define or connection string
cnxn = pyodbc.connect('DRIVER={ODBC Drive 17 for SQL Server}'
                      SERVER='+ server + ';\
                      DATABASE=' +database+';\
                      Trusted_Connection=yes;')

#create the connection cursor
cursor = cnxn.cursor()

#definer our insert query
insert_quary = '''INSERT INTO Python_test (id, ten, tuoi, dia chi)
                VALUES(?,?,?,?);'''

#loop through each row in the matrix
for row in price_data:
    #define the values to insert
    values = (row[0],row[1],row[2],row[3])
    #insert the data into the database
    cursor.execute(insert_query, values)

#commit the inserts
cnxn.commit()

#grab all the rows in our database table
cursor.execute('SELECT * FROM Python_test')

#loop through the results
for row in cursor:
    print(row)

#close the connection and remover the cursor
cursor.close()
cnxn.close())