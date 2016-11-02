import requests

token = {"token": "376df7bbf6451c2670167ada5f7ebc86", "github":"https://github.com/shelbyheinecke/Code2040"}
resp = requests.post('http://challenge.code2040.org/api/reverse', json=token)
backward = resp.text[::-1]
back = {"token": "376df7bbf6451c2670167ada5f7ebc86","string":backward}
resp1 = requests.post('http://challenge.code2040.org/api/reverse/validate', json = back)
