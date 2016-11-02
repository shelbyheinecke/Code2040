import requests

connect = {"token": "376df7bbf6451c2670167ada5f7ebc86", "github":"https://github.com/shelbyheinecke/Code2040"}
resp = requests.post('http://challenge.code2040.org/api/register', json=connect)
if resp.status_code != 200:
    print("error")
else:    
    print('Done with Step 1.')
