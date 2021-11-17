# loginsystempython
# by kiritosate

try:
    
    import mysql.connector as myconnect
except ImportError as e:
    print(e)   

import random
import os
import getpass

class Main:

    def __init__(self) -> None:

        self.mydb = None
        self.dbcursor=''
        
        self.dbcon('root', 'root', 'localhost', 'pydb')

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

            
            self.new_user = input("Type q to return.\nUsername: ")
            if self.username == 'q': self.main()
            if len(self.new_user) > 5:
                self.new_pass = getpass.getpass("password: ")
                if len(self.new_pass) > 6: 
                    self.new_pass2 = getpass.getpass("confirm password: ")
                else: 
                    print('password is weak, should be 6 or more character. try again.')
                    os.system('pause')
                    self.register()
            else:
                print('username character length should be 5 or more. try again.'), os.system('pause'), self.register()

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
            self.username = input("Type q to return.\nUsername: ")

            if self.username == 'q': self.main()

            self.dbcursor.execute(f'SELECT * FROM users WHERE username="{self.username}"')
            self.logindata = ''

            for data in self.dbcursor.fetchall(): self.logindata = data

            if self.logindata :
                self.password = getpass.getpass("Password: ")

                if self.password == self.logindata[2]:
                    goto = Dashboard(self.logindata, self.mydb)
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

    def __init__(self, logindata, connect) -> None:

        print(f"Welcome @user_{logindata[1]}!")

        self.dashboard()

    def dashboard(self):

        '''
        
        '''

        print("==========\n=DASHBOARD=\n===========\n")
        self.entry = input("[3]show users\n[2]change password\n[1]logout\n[0]delete account: ")

        if self.entry == '3': self.listuser & self.main
        elif self.entry == '2': self.changepassword
        elif self.entry == '1': self.logout
        elif self.entry == '0': self.deleteaccount
    
    def changepassword(self):
        pass
    def deleteaccount(self):
        pass
    def logout(self):
        pass
if __name__ == '__main__':
    Main()

