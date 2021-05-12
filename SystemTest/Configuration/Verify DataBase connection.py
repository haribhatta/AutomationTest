import pyodbc
conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-LCQ7JSQ;"
                      "Database=Danphe_LPH_V1.9.0;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()
cursor.execute('select * from PAT_Patient where PatientCode = 2105000198')

for row in cursor:
    print('row = %r' % (row,))