# pip install mysql
# pip install mysql-connector-python
# mysql.server start

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Here2please'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE zecrm")

print("All Done!")

# mysql.server stop