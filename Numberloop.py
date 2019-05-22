import csv
from requests.auth import HTTPBasicAuth
import requests
import json
file = open('Response.txt', 'w+')
with open('numbercheck.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        URL = "https://apix.aerialink.net/v4/numbers"
        Param = {'numbers': row[0]}
        response = requests.get(url = URL,params = Param,auth=HTTPBasicAuth('XXXXX','XXXXXX'))
        if (response.status_code >= 401):
            print("Error")
        else:
            a=json.loads(str(response))
            l = a['aerialink']['transactions']
            v = l['transaction']['number']['operator']['mcc']['mnc']['operatorType']['wireless']['country']['countryCode']['validNumber']['lastUpdated']
            file.write(v+'\n'+'\n')
    file.close()
