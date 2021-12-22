
import requests
from bs4 import BeautifulSoup as bsoup

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/601.1.10 (KHTML, like Gecko) Version/8.0.5 Safari/601.1.10",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; ; NCT50_AAP285C84A1328) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
]

_URl = "https://m.facebook.com"
_URl2 = "https://m.facebook.com/messages"
_LOGIN_URL = "https://m.facebook.com/login.php"

class fbScraper:

    def __init__(self, email, password):
        
        self.session = requests.Session()
        
        self._data = {
            'email':email,
            'pass':password,
            'login': "Log In",
        }

        self.messData = {
            'body':'hi kdasdad',
        }

    def _login(self):

        self._r = self.session.get(_URl)

        with self.session.post(_LOGIN_URL, data=self._data) as self.r:

            if "save-device" in self.r.url:
                self.session.get("https://m.facebook.com/login/save-device/cancel/")

            self._results = self.session.get(_URl2)
    
    def _parseData(self):

        self._DATA = bsoup(self._results.content, "html.parser")
        self._result = self._DATA.find_all("td", attrs={'class':not None})
        
        self._pdata = []
        for item in self._result:
            a = item.find("span")
            b = item.find("a")
            try:
                if(b.text and a.text):
                    self._pdata.append({
                        'author': b.text,
                        'message': a.text,
                        'convo_link': b.get('href')
                    })
            except:
                pass

        #for i in self._pdata:
            #print(i)

        d = self.session.get(_URl+self._pdata[0]['convo_link'])

        self.messData['sid'] = d.headers.get("sid")
        self.messData['cid'] = d.headers.get("cid")
        self.messData['region'] = d.headers.get("region")

        print(self.messData)

        pos = self.session.post(_URl+"/messages/send/", data=self.messData)
        tem = bsoup(pos.content, "html.parser")

        print(tem.prettify())
        print(pos.url)
        #print(f"{bsoup(d.content,'html.parser').prettify()} || {d.status_code}")
    def getUid(self):

        print(self.session.cookies.get_dict().get("c_user"))
        print(self.session.cookies.get_dict().get("cid"))
    
    def now(self):
        return int(self.time() * 1000)
    
    def time(self):
        return 3123123

Client = fbScraper()
Client._login()
Client._parseData()
Client.getUid()

