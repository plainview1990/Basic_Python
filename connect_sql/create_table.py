import pyodbc

con = pyodbc.connect("driver=ODBC Driver 17 for SQL Server;server=Warehouse;database=SiS_Cloud;trusted_connection=yes")

cursor = con.cursor()
cursor.execute("""create table person(
           id int primary key,
           gender char(1),
           height real, 
           weight real
      )""")

con.commit()