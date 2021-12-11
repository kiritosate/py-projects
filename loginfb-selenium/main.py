
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

LOGIN_URL = 'https://www.facebook.com/login.php'

class FacebookLogin:

    def __init__(self, email, password, browser='Microsoft') -> None:
        
        self.email = email
        self.password = password

        self.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

        try:

            self.driver.get(LOGIN_URL)

        except:
            FacebookLogin()

        time.sleep(1)

    def login(self):

        self.emailEntry = self.driver.find_element_by_id('email')
        

        



