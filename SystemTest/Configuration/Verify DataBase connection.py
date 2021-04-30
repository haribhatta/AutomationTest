import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-68UCKA5\SQLEXPRESS;'
                      'Database=LumbiniEMR_QA_V1.8.0;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM LumbiniEMR_QA_V1.8.0.dbo.ADT_Bed')

for row in cursor:
    print(row)