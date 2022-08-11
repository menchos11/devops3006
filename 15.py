import requests
try:
    response = requests.get("htsdps://github.com")
except Exception as e:
    print("something went wrong")
    print(e.args)
