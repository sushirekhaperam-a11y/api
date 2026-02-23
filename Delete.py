import requests

try:
    response = requests.delete("http://127.0.0.1:5000/users/1")
    print(response)

    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        print(data)
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")