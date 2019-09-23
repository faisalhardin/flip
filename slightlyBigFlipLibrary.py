import urllib.request, base64, json
TOKEN = 'HyzioY7LP6ZoO7nTYKbG8O4ISkyWnX1JvAEVAhtWKZumooCzqp41'
BASE_URL = 'https://nextar.flip.id/'
AUTHORIZATION = 'SHl6aW9ZN0xQNlpvTzduVFlLYkc4TzRJU2t5V25YMUp2QUVWQWh0V0tadW1vb0N6cXA0MTo='



def get_header():
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

    return headers

def disburse_status(id):

    param = 'disburse/'+id
    request = urllib.request.Request(url=BASE_URL+param, headers=get_header())

    try:
        with urllib.request.urlopen(request) as response:
            json_response = json.load(response)
            return json_response
    except:
        return None

def disburse(bank_code, account_number, amount, remark):

    param = 'disburse'
    values = {
        'bank_code' : bank_code,
        'account_number' : account_number,
        'amount' : amount,
        'remark' : remark
    }

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    request = urllib.request.Request(url=BASE_URL+param, data=data, headers=get_header())

    try:
        with urllib.request.urlopen(request) as response:
            json_response = json.load(response)
            return json_response
    except:
        return None

def update_database(id, status, receipt, time_served):
    #connect to local server and update
    pass

    

