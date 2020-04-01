import json
import requests
import time

a = requests.get('http://camnet.camelotpnw.tech/api/v1/members?page=1')
b = requests.get('http://camnet.camelotpnw.tech/api/v1/members?page=2')
c = requests.get('http://camnet.camelotpnw.tech/api/v1/members?page=3')

with open('Camelot_Warchest_{}.json'.format(time.strftime("%Y%m%d-%H%M%S")), 'w') as my_data_file:
    json.dump(a.json(), my_data_file)
    json.dump(b.json(), my_data_file)
    json.dump(c.json(), my_data_file)
