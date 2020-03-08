import json
import requests
import time

a = requests.get('https://camelotpnw.tech/api/v1/members?page=1')
b = requests.get('https://camelotpnw.tech/api/v1/members?page=2')

with open('Camelot_Warchest_{}.json'.format(time.strftime("%Y%m%d-%H%M%S")), 'w') as my_data_file:
    json.dump(a.json(), my_data_file)
    json.dump(b.json(), my_data_file)
