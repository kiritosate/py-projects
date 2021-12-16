
import random
from os import system
import time
from urllib import request, error
from urllib.parse import urlencode
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class madLib:

    def __init__(self) -> None:
        
        while True:

            name = input("your name: ")
            age = input("your age: ")

            print(f"my name is {name} i am {age}")

class guessTheNumberComputer:

    def __init__(self) -> None:
        
        while True:
            
            yNumber = input("choose a number from 1-5: ")
            hNumber = random.randint(1,5)
            if yNumber == hNumber:
                print(f"you guessed it right! it is {yNumber}")
            else:
                print(f"you guessed it wrong! it is {hNumber}")

class guessTheNumberUser:

    def __init__(self) -> None:
        
        while True:

            hNumber = input("choose your hidden number from 1-5: ")
            cNumber = random.randint(1,5)

            if cNumber == hNumber:
                print(f"the computer guessed it right! it is {cNumber}")
            else:
                print(f"the computer guessed it wrong! it is {hNumber}")

class rockPaperScissors:

    def __init__(self) -> None:
        
        choices = ["Rock","Paper","Scissors"]

        while True:
            system("cls")
            mChoice = input("[0]Rock, [1]Paper, or [2]Scrissors!: ")
            temp = random.choice(choices)

            for choice in choices:
                print(choice+" !!")
                time.sleep(1)


            if temp == mChoice or temp == choices[int(mChoice)]:
                print(f"correct!!! {temp}")
            else:
                print(f"wrong !! it is {temp}")
            
            system("pause")

class countDownTimer:

    def __init__(self) -> None:
        
        while True:

            count = int(input("countdown number: "))

            while count >= 0:
                print(count)
                time.sleep(1)
                count-=1

class passwordGenerator:

    def __init__(self) -> None:

        while True:
        
            pLength = int(input("enter password length: "))

            numerics = "abcdefghijklmnopqrstuvwxyz1234567890"

            password = ""

            print(pLength)

            while pLength>0:
                
                temp = random.randint(1,3)

                if 1 == temp:
                    password += numerics[random.randint(1, 35)].upper()
                else:
                    password += numerics[random.randint(1, 35)]
                
                pLength-=1
            
            return password

class encoderDecoder:

    def decode():

        numerics = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        while True:

            string = input("enter text to decode: ")
            key = int(input("enter a key [1-100]: "))
            newString = ""

            for char in string:

                temp = numerics.index(char)

                newString += numerics[temp-key]
                
            print(f"decoded string [ {newString} ] :key {key}")

    def encode():

        numerics = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        
        while True:

            string = input("enter text to encode: ")
            key = int(input("enter a key [1-100]: "))
            newString = ""

            for char in string:

                temp = numerics.index(char)

                newString += numerics[temp+key]
                
            print(f"encoded string [ {newString} ] :key {key}")

class randomUserApi:

    def __init__(self) -> None:
        
        global results

        URL = 'https://randomuser.me/api/'

        results = json.loads(requests.get(URL).content)

        cleaned_results = json.dumps(results, sort_keys=True, indent=2)

    def _name(self):

        self._first = results["results"][0]["name"]["first"]
        self._last = results["results"][0]["name"]["last"]

        self._fullname = f"{self._first} {self._last}"

        return self

    def _picture(self):

        self._large = results["results"][0]["picture"]["large"]
        self._medium = results["results"][0]["picture"]["medium"]
        self._thumbnail = results["results"][0]["picture"]["thumbnail"]

        return self
    
    def _login(self):

        self._md5 = results["results"][0]["login"]["md5"]
        self._password = results["results"][0]["login"]["password"]
        self._username = results["results"][0]["login"]["username"]

        return self
    
    def _info(self):

        self._age = results["results"][0]["dob"]["age"]
        self._phone = results["results"][0]["cell"]
        self._gender = results["results"][0]["gender"]
        self._email = results["results"][0]["email"]

        return self

    def _userdata(self):

        self.data = []

        self.data.append(self._name()._fullname)
        self.data.append(self._info()._age)
        self.data.append(self._info()._gender)
        self.data.append(self._info()._email)
        self.data.append(self._picture()._thumbnail)

        return self.data

class myDice:

    def __init__(self) -> int:

        while True:
        
            roll = input("roll? [yes/y/Y || no/n/N: ")

            if roll == "y" or roll == "yes":

                print(random.randint(1,6))

            else: 

                break

class daysTo:

    def __init__(self) -> None:
        
        while True:

            days = int(input("Enter no. of days: "))

            years = int(days / 365)
            months = int((days-(years*365))/30)
            day = int((days-(years*365))-(30*months))

            print(f"{years} Year(s)\n{months} Month(s)\n{day} Day(s)")

class fbLoginWSelenium:

    def __init__(self) -> None:
        
        self.driver = webdriver.Edge()

        self.driver.get("https://www.facebook.com/login")

