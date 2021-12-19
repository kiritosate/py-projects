from attr import attr
import requests
from bs4 import BeautifulSoup as bsoup
from requests import sessions



_URL = "https://m.facebook.com"

LOGIN_URL = "https://m.facebook.com/login.php"
FACEBOOK_URL = "https://m.facebook.com/"
MESSAGES_URL = "https://m.facebook.com/messages"
MESSENGER_URL = "https://www.messenger.com"

#VARS
s = None

#MAIN CLASS
class facebook():
    def __init__(self):
        self.s = requests.session()
        self.login()

    def login(self):
        #GET DEFAULT VALUES FROM PAGE
        r = self.s.get(FACEBOOK_URL)
        soup = bsoup(r.text, "html.parser")
        #GET DEFAULT VALUES
        data = {
            
        }
        data['email'] = EMAIL
        data['pass'] = PASSW
        data['login'] = 'Log In'
        self._data = None

        with self.s.post(LOGIN_URL, data=data) as main:
            if "save-device" in main.url:
                self.s.get("https://m.facebook.com/login/save-device/cancel/")

            self._DATA = self.s.get(MESSAGES_URL, allow_redirects=True)
            self._data = bsoup(self._DATA.content, "html.parser")

            data = self.getData(self._data)
            print(data)
            print(3423423)
            for dat in data:
                print(dat)
    
    def getData(self, results):

        self._DATA = []
        self.temp = results.find_all("td", attrs={"class":"s bv bw"})

        for item in self.temp:
            self.conv_name = item.find("a")
            self.conv_name.text
            self.conv_prev = item.find("span")
            self.conv_prev.text
            print("dasdasdsa")

            self._DATA.append({
                'author':self.conv_name,
                'message':self.conv_prev,
            })
        
        return self._DATA


fb = facebook()