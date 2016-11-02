import requests

token = {"token": "376df7bbf6451c2670167ada5f7ebc86", "github":"https://github.com/shelbyheinecke/Code2040"}
resp = requests.post('http://challenge.code2040.org/api/haystack', json=token)
dictionary = resp.json()
needle= dictionary['needle']
haystack = dictionary['haystack']
n = haystack.index(needle)
sendback = {"token": "376df7bbf6451c2670167ada5f7ebc86","needle":n}
resp1 = requests.post('http://challenge.code2040.org/api/haystack/validate', json = sendback)

