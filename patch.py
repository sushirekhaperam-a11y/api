import requests

try:
    data = {
        "name" : "Apple MacBook Pro 16(Updated name)8"
    }
    response = requests.patch("https://api.restful-api.dev/objects/ff8081819c5368bb019c55a44ccb046f",json=data)
    print(response)

    if response.status_code == 200:
        print("Status code is 200 k")
        data = response.json()
        print(data)
    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")