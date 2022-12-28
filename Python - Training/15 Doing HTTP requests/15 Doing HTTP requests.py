import requests 

try:
    x = requests.get('https://api.github.com/users/python')
    # print(x.status_code)
    print(x.text)
except:
    print("No internet connectivity.")