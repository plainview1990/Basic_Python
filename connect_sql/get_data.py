import pyodbc

con = pyodbc.connect("driver=ODBC Driver 17 for SQL Server;server=Warehouse;database=SiS_Cloud;trusted_connection=yes")

cursor = con.cursor()
sql_query = 'select * from person'
cursor.execute(sql_query)

for row in cursor:
    print(row)

