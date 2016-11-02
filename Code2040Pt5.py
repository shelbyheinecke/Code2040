import requests
from datetime import datetime, timedelta

token = {"token": "376df7bbf6451c2670167ada5f7ebc86", "github":"https://github.com/shelbyheinecke/Code2040"}
resp = requests.post('http://challenge.code2040.org/api/dating', json=token)
dictionary = resp.json()
datestamp = dictionary['datestamp']
interval = float(dictionary['interval'])

timestamp_parsed = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
timestamp_toseconds = (timestamp_parsed - datetime(1970, 1, 1)).total_seconds()
newseconds = timestamp_toseconds + interval

newtime = datetime(1970, 1, 1) + timedelta(seconds=newseconds)
newtimestamp = newtime.strftime('%Y-%m-%dT%H:%M:%SZ')


sendback = {"token": "376df7bbf6451c2670167ada5f7ebc86","datestamp":newtimestamp}
resp1 = requests.post('http://challenge.code2040.org/api/dating/validate', json = sendback)
