import mysql.connector
from Account import Account
import hashlib
import re

class AccountManager:

    def check_mail(email : str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False

    def check_names(name : str):
        print(name.isalpha())
        return name.isalpha()

    def __init__(self, mysql_connection) -> None:

        accounts : list[Account] = []
        self.connection = mysql_connection
        

    def get_account(self, email : str, clear_password : str) -> bool | tuple:

        hashed_password = hashlib.sha256(clear_password.encode()).hexdigest()

        if AccountManager.check_mail(email) == False:
            return False
            
        with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM `accounts` WHERE `email` = '{email}' AND `password` = '{hashed_password}';")
                results = cursor.fetchall()
                for row in results:
                    print(row)


    def create_account(self, email, first_name, last_name, clear_password) -> bool:

        hashed_password = hashlib.sha256(clear_password.encode()).hexdigest()

        if AccountManager.check_mail(email) == False or AccountManager.check_names(first_name) == False or AccountManager.check_names(last_name) == False:
            return False
        

        with self.connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO `accounts` VALUES ({0}, '{email}', '{first_name}', '{last_name}', '{hashed_password}');")
            self.connection.commit()

        return True



