#!/usr/bin/python3
import ssl
import requests
import urllib3
import time
import json
import datetime
import time
import random
urllib3.disable_warnings()
date = datetime.datetime.now()
apiurl = 'https://10.10.20.50/api/v2/cmdb/system/interface/port3'
apitoken = '19q57y0Nzxms3qxmqcdGNpNky4fkdc'
headers = {'Authorization': "Bearer {}".format(apitoken)}
interface = requests.get(apiurl, headers=headers, verify=False)
results = interface.json()
data = results.get('results')
while True:
    zzz = random.uniform(30, 180)
    try:
        for x in data:
            if x['status'] == 'up':
                print('Switching from up to down')
                down = {'status':'down'}
                auth_response = requests.put(apiurl, headers=headers, json=down, verify=False)
                results = auth_response.json()
                status = requests.get(apiurl, headers=headers, verify=False)
                state = status.json()
                data = state.get('results')
                print(f"Status is now {data[0]['status']}")
            if x['status'] == 'down':
                print('Switching from down to up')
                up = {'status': 'up'}
                auth_response = requests.put(apiurl, headers=headers, json=up ,verify = False)
                results = auth_response.json()
                status = requests.get(apiurl, headers=headers, verify=False)
                state = status.json()
                data = state.get('results')
                print(f"Status is now {data[0]['status']}")
            print(f'Sleeping for {zzz}')
            time.sleep(zzz)
    except Exception as e:
        print(e)



