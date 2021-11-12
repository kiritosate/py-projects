# loginsystempython
# by kiritosate

import random

class Main:

    def __init__(self) -> None:
        
        self.main()
    
    def main(self):
        '''
        
        '''
        while True:

            qidentry = input("[0]Login\n[1]Register\n[2]Quit\n[qid]: ")

            if qidentry == '2':
                break
            elif qidentry == '1':
                self.register()
            elif qidentry == '0':
                self.login()
            else:
                print('invalid qid, please try again...')
    
    def register(self):
        pass

    def login(self):
        pass


if __name__ == '__main__':
    Main()

