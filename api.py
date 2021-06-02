import requests

payload = {'username': 'cory', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

r_dict =r.json()
print(r_dict['form'])
