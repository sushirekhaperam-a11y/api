#Write a Python script to send a GET request to https: // jsonplaceholder.typicode.com / users and print only name and email.
import requests
import json
from requests.auth import HTTPBasicAuth

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)

    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        for user in data:
            print(user['name'])
            print(user['email'])
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")

#Send a GET request with query parameter userId=2 and print number of posts returned.
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",{"id":2})
    print(response)

    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        print(len(data))
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")
#Write a POST request to create a new resource and verify status code 201.
try:
    data = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    response = requests.post("https://jsonplaceholder.typicode.com/users",json=data)
    print(response)

    if response.status_code == 201:
        print("Status code is 201 ")
        data = response.json()
        print(data)
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")
# Write code to check if response status code is not 200 and raise an exception.

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)

    if response.status_code != 200:
        raise Exception(f"Request failed with status code:{response.status_code}")
        data = requests.json()
        for user in data:
            print(user)

except Exception as e:
    print(f"An error has occurred:{e}")
#Fetch all users and print usernames in uppercase.
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)

    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        for user in data:
            print(user['name'].upper())
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")

#Implement timeout handling (2 seconds) and catch Timeout exception.

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)
    print(response)
    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        for user in data:
            print(user['name'],user['email'])
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.Timeout:
    print("The request timedout after 2 seconds")
#Use Session object to send multiple requests and demonstrate cookie persistence.
#Upload a file using requests and print server response.
file_path = "C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//simple.json"
files = {"file":open(file_path,'rb')}
try:
    response = requests.post("https://jsonplaceholder.typicode.com/users",files=files)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")
finally:
    files['file'].close()
#Fetch posts and save response JSON into a file named posts.json.
response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)
print(response)
if response.status_code == 200:
    print("Status code is 200 k")
    data = response.json()
    with open("C://Users//Sushi//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//dataformats//posts.json",'w')as file:
        json.dump(data,file,indent=4)
    print("completed")


