import requests
import json
class H1BEndpoint:
    def __init__(self):

        self.url = 'https://h1bgrader.com/api/listall'
        self.headers = {
            'authority': 'h1bgrader.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-GB,en;q=0.6',
            'cookie': 'cf_clearance=qhD2s.1.Ez8AJL9wqdw2GcuktNWvAwtSzwlJKO6nylc-1703700138-0-2-55f70b24.2758dcd1.a8265f96-0.2.1703700138',
            'referer': 'https://h1bgrader.com/h1b-sponsors',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
    
    def makeRequest(self, start=0, length=50000):
        params = {
            'employer': 'true',
            'startsWith': '',
            'draw': '1',
            # ... add other parameters as needed
            'start': str(start),
            'length': str(length),
            'search[value]': '',
            'search[regex]': 'false',
            '_': '1703702572474'
        }

        response = requests.get(self.url, headers=self.headers, params=params)

        if response.status_code == 200:
            data = str(response.json())
            return response
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

h1bSrc = H1BEndpoint()

limit = 450000

cur = 0

while cur < 450000:
    start = int(cur/1000)
    end = int((cur+50000)/1000)
    res = h1bSrc.makeRequest(cur)
    if res:
        file = open(f'./h1b_info/data/{start}k_{end}k.json', 'w')
        json_res = res.json()
        formatted_json = json.dumps(json_res, indent=4)
        str_res = str(formatted_json)
        str_res = str_res.replace("'", '"')
        file.write(str_res)
        file.close()
    else:
        print(f'no response for {start}k_{end}k')
    cur += 50000