import pyodbc
from TestActionLibrary import A


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LCQ7JSQ;'
                      'Database=DanpheEMR_Beta-V1.46;'
                      'Trusted_Connection=no;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM [DanpheEMR_Beta-V1.46].[dbo].[PHRM_NarcoticSaleRecord]')

for row in cursor:
    print(row)
