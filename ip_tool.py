from requests import get
import sys

while(True):
    ip_search = input("Enter ip address: ")
    if ip_search == 'exit':
        sys.exit()
    else:
        search = get(f'http://ip-api.com/json/{ip_search}')
        print(search.json())

