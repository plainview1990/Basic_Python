import pyodbc

con = pyodbc.connect("driver=ODBC Driver 17 for SQL Server;server=Warehouse;database=SiS_Cloud;trusted_connection=yes")

cursor = con.cursor()
cursor.execute("""drop table person""")
con.commit()


