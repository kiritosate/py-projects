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
                print(self.key())
                print('invalid qid, please try again...')
    
    def register(self):
        pass

    def login(self):
        pass

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


if __name__ == '__main__':
    Main()

