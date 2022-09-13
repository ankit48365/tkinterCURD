#!/usr/bin/env python
import sys
import os
print (sys.argv[0] + " with argcount " + str(len(sys.argv)))
if len(sys.argv) < 2 or sys.argv[1] != "2":
    print ("doing recursion")
    os.system(sys.argv[0] + " 2");
else:
    print ("not doing recursion")

exit(0)



# import pyodbc
# server = 'ak-az-sqlserver.database.windows.net'
# database = 'ak-az-sqlserver'
# username = 'admin4'
# password = '{P@ssword2021}'   
# driver= '{ODBC Driver 17 for SQL Server}'
# connectionString = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';'


# mssqldb = pyodbc.connect(connectionString)
# mycursor = mssqldb.cursor()
# mycursor.execute("SELECT TOP 3 * from PROJ5.SITE_TBL")
# records = mycursor.fetchall()
# print(records)