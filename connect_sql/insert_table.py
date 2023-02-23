import pyodbc

con = pyodbc.connect("driver=ODBC Driver 17 for SQL Server;server=Warehouse;database=SiS_Cloud;trusted_connection=yes")

cursor = con.cursor()
cursor.execute("""insert into person(id, gender, height, weight) 
            values 
            (1,'M',175,70),
            (2,'F',165,45)""")

con.commit()
