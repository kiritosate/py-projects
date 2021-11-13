# loginsystempython
# by kiritosate

try:
    import random
    import mysql.connector as myconnect
except ImportError as e:
    print(e)

import os
import getpass

class Main:

    def __init__(self) -> None:

        self.mydb = None
        self.dbcursor=''
        
        self.dbcon('root', 'root', 'localhost', 'loginsystempydb')

        print('MySqlConnection Success! At == {0}'.format(self.mydb))

        self.main()
    
    def dbcon(self, username, password, host, database):

        try:
            self.mydb = myconnect.connect(
                host = host,
                user = username,
                password = password,
                database = database
            )
            self.dbcursor = self.mydb.cursor()
            return self.mydb
        except ConnectionError as e:
            return e
    
    def main(self):
        '''
        
        '''
        
        while True:
            self.ccLine()
            print('=================================\n========== DATA SYSTEM ==========\n=================================')
            qidentry = input("[0]Login\n[1]Register\n[2]Quit\n[3]show users\n[qid]: ")

            if qidentry == '2':
                break
            elif qidentry == '1':
                self.register()
            elif qidentry == '0':
                self.login()
            elif qidentry == '3':
                self.listuser()
            else:
                print('invalid qid, please try again...')

    def listuser(self):
        self.ccLine()
        self.dbcursor.execute("SELECT username FROM users ")
        self.data = self.dbcursor.fetchall()
        self.temp = []

        for i in range(10):
            try:
                self.temp.append(self.data[i][0])
            except:
                break
        
        try:
            print('===================================\n========== LIST OF USERS ==========\n===================================')
            for data in self.temp:
                print(f"USER: [{data}]")
        except:
            print('===================================\n========== LIST OF USERS ==========\n===================================\nNONE')
        
        os.system('pause')
        
        self.main()

    def register(self):
        '''
        
        '''
        while True:
            print('======================================\n=============== REGISTER =============\n======================================\n')
            self.keystr = self.key()
            self.new_user = input("Username: ")
            self.new_pass = getpass.getpass("password: ")
            self.new_pass2 = getpass.getpass("confirm password: ")

            if self.new_pass == self.new_pass2: 

                self.dbcursor.execute(f'INSERT INTO users (username, password, userskey) VALUES ("{self.new_user}", "{self.new_pass}", "{self.keystr}")')
                self.mydb.commit()
                self.listuser()
                os.system('pause')
                return False
            else:
                print('The password is now the same. try again')

    def login(self):

        while True:
            print('===================================\n=============== LOGIN =============\n===================================\n')
            self.username = input("username: ")

            self.dbcursor.execute(f'SELECT * FROM users WHERE username="{self.username}"')
            self.logindata = ''

            for data in self.dbcursor.fetchall(): self.logindata = data

            if self.logindata :
                self.password = getpass.getpass("Password: ")

                if self.password == self.logindata[2]:

                    print(f"Welcome @user_{self.username}!")
                    os.system('pause')
                    self.main()
                else:
                    print(f"your password invalid. try again.")
            else:
                print(f"user: {self.username} does not exist. try again.")

            os.system('pause')
            self.ccLine()
    def key(self):
        alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'
        self.keystring = ''
        self.style = 0

        for i in range(25):
            
            self.style = random.randint(0,1)

            if self.style == 1:
                self.keystring = str(self.keystring) + str(alpha[random.randint(0, 34)].upper())
            else:
                self.keystring = str(self.keystring) + str(alpha[random.randint(0,34)])
        
        return self.keystring
    
    def ccLine(self):

        try:
            os.system('cls')
        except:
            os.system('clear')

class Dashboard:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    Main()

