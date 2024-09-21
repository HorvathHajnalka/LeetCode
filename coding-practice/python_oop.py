import requests

class MyClass:
    def __init__(self, myparam1, myparam2):
        self.myparam1 = myparam1
        self.myparam2 = myparam2
    def myAdd(self):
        return self.myparam1 + self.myparam2
    
class InheritedClass(MyClass):
    def __init__(self, myparam1, myparam2, inparam1, inparam2):
        MyClass.__init__(self, myparam1, myparam2)
        self.inparam1 = inparam1
        self.inparam2 = inparam2
    
    def myAdd(self):
        return self.inparam1 + self.inparam2
    
myClass = MyClass(1,1)
inClass = InheritedClass(1,1,2,2)

print(myClass.myAdd())
print(inClass.myAdd())

response = requests.get('https://catfact.ninja/fact')
response_nationality = requests.get('https://api.nationalize.io/?name=hajnalka')
if response.status_code == 200:
    response_json = response.json()
    print('fact: ' + response_json['fact'])
    print('length: ' + str(response_json['length']))
else:
    print(response.status_code)
if response_nationality.status_code == 200:  
    nationality_json = response_nationality.json()
    print('country: '+ nationality_json['country'][0]['country_id'])
else:
    print(response.status_code)

