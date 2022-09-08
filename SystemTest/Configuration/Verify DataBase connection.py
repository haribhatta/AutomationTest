   #################Test Action: DB Connection###########
import pyodbc
import pandas as pd

conn = pyodbc.connect("Driver={SQL Server};"
                    "Server=DESKTOP-68UCKA5\SQLEXPRESS;"  # DESKTOP-68UCKA5\SQLEXPRESS
                    "Database=TEST_LIVE_DanpheEMR_MMH_NewV2;"  # TEST_LIVE_DanpheEMR_MMH_NewV2
                    "Trusted_Connection=yes;")


query = "select WardName from ADT_MST_Ward where WardID = (select TOP(1) WardId from ADT_Bed where IsReserved = 0)"
df = pd.read_sql(query, conn)
WardName = df.at[0, 'WardName']
print("WardName Name:", WardName)
