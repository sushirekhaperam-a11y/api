import requests
from requests.auth import HTTPBasicAuth

try:
    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }
    # make a get request to endpoint api
    response  = requests.get("https://videogamedb.uk:443/api/v2/videogame",auth = HTTPBasicAuth('username','password'),timeout=5,headers = headers)
    print (response)

    #
    if response.status_code == 200:
        print("Status code is 200 k")

        #parse the jso file
        data = response.json()
        print(data)
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")