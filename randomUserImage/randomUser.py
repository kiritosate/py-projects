import json
import requests

class RandomUserData:

    def _userdata():
        global results

        URL = 'https://randomuser.me/api/'
        results = json.loads(requests.get(URL).content)
        data = []

        _firstname = results["results"][0]["name"]["first"]
        _lastname = results["results"][0]["name"]["last"]
        _fullname = f"{_firstname} {_lastname}"
        
        _age = results["results"][0]["dob"]["age"]

        _gender = results["results"][0]["gender"]

        _email = results["results"][0]["email"]

        _image = results["results"][0]["picture"]["large"]

        data.append(_fullname)
        data.append(_age)
        data.append(_gender)
        data.append(_email)
        data.append(_image)

        return data