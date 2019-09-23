import urllib.request, base64
TOKEN = 'HyzioY7LP6ZoO7nTYKbG8O4ISkyWnX1JvAEVAhtWKZumooCzqp41'
BASE_URL = 'https://nextar.flip.id/'
AUTHORIZATION = 'SHl6aW9ZN0xQNlpvTzduVFlLYkc4TzRJU2t5V25YMUp2QUVWQWh0V0tadW1vb0N6cXA0MTo='

def disburse():

    authentication_param = TOKEN+":"
    bin_auth = authentication_param.encode("utf-8")
    encoded_auth = base64.standard_b64encode(bin_auth)

    string_auth = encoded_auth.decode('ascii')
    headers = {
        'Authorization':'Basic ' + string_auth,
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0'
    }

    param = 'disburse/1'
    
    request = urllib.request.Request(url=BASE_URL+param, headers=headers)

    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(repr(html))

disburse()