import requests

token = {"token": "376df7bbf6451c2670167ada5f7ebc86", "github":"https://github.com/shelbyheinecke/Code2040"}
resp = requests.post('http://challenge.code2040.org/api/prefix', json=token)
dictionary = resp.json()
prefix = dictionary['prefix']
array = dictionary['array']
finalarray = []
for i in range(len(array)):
    if (array[i].startswith(prefix) == 0):
        finalarray.append(array[i])

sendback = {"token": "376df7bbf6451c2670167ada5f7ebc86","array":finalarray}
resp1 = requests.post('http://challenge.code2040.org/api/prefix/validate', json = sendback)
