from mysql.connector import connect, Error
from getpass import getpass
from AccountManager import AccountManager

HOST = 'localhost'
USER = 'root'
print(f"Connecting to [{HOST}] with user [{USER}]")
database_password = getpass("Enter password : ")
connection = None

try: 
   
    connection = connect(
        host = "localhost",
        user = "root",
        password = database_password,
        database = 'cob'
    )

except Error as e:
    print(e)

manager = AccountManager(connection)

print(manager.create_account("max@test.com", "test", "test", "hlm"))
manager.get_account("max@test.com", "hlm")
