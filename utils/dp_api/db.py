import sqlite3
import os
class Database:
    def __init__(self, db_file) :
        print(os.getcwd())
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def user_exists(self, user_id):
        print(os.getcwd())
        with self.connection:
            result = self.cursor.execute("SELECT * from 'users' WHERE id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def user_data(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * from 'users' WHERE id = ?", (user_id,)).fetchall()
            return result
            
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute ("INSERT INTO 'users' ('id') VALUES (?)", (user_id,))
    
    def user_login(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT login from 'users' WHERE id = ?", (user_id,)).fetchone()[0]
            return result

    def change_login(self, user_id, login):
        with self.connection:
            result = self.cursor.execute("UPDATE users SET login = ? WHERE id = ?",(login, user_id,))
            return result
    
