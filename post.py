import requests

url = 'http://127.0.0.1:6000/new_block'
data = {'transaction': 3,
        'amount': 200,
        'customerID': 1}

x = requests.post(url, data = data)

print(x.text)