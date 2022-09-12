import pyodbc
server = 'ak-az-sqlserver.database.windows.net'
database = 'ak-az-sqlserver'
username = 'admin4'
password = '{P@ssword2021}'   
driver= '{ODBC Driver 17 for SQL Server}'
connectionString = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+';'


mssqldb = pyodbc.connect(connectionString)
mycursor = mssqldb.cursor()
mycursor.execute("SELECT TOP 3 * from PROJ5.SITE_TBL")
records = mycursor.fetchall()
print(records)