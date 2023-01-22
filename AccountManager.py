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

    def user_db_to_account(data : tuple) -> int:
        account = data[0]
        return account

    def get_data_from_id(self, id : int):

        with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM `accounts` WHERE `id` = {id};")
                results = cursor.fetchall()[0]

                if len(results) > 0:
                    return True, {'email' : results[1],'first_name' : results[2], 'last_name' : results[3]}
                else:
                    return False, None


    def __init__(self, mysql_connection) -> None:

        self.connection = mysql_connection
        

    def get_account(self, email : str, clear_password : str) -> bool | tuple:

        hashed_password = hashlib.sha256(clear_password.encode()).hexdigest()

        if AccountManager.check_mail(email) == False:
            return False, None
            
        with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM `accounts` WHERE `email` = '{email}' AND `password` = '{hashed_password}';")
                results = cursor.fetchall()

                if len(results) > 0:
                    return True, AccountManager.user_db_to_account(results[0])
                else:
                    return False, None

        


    def create_account(self, email, first_name, last_name, clear_password) -> bool:

        hashed_password = hashlib.sha256(clear_password.encode()).hexdigest()

        if AccountManager.check_mail(email) == False or AccountManager.check_names(first_name) == False or AccountManager.check_names(last_name) == False:
            return False
        

        with self.connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO `accounts` VALUES ({0}, '{email}', '{first_name}', '{last_name}', '{hashed_password}');")
            self.connection.commit()

        return True



