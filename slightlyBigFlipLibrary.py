import urllib.request, base64, json
import sqlite3
from sqlite3 import Error
TOKEN = 'HyzioY7LP6ZoO7nTYKbG8O4ISkyWnX1JvAEVAhtWKZumooCzqp41'
BASE_URL = 'https://nextar.flip.id/'
AUTHORIZATION = 'SHl6aW9ZN0xQNlpvTzduVFlLYkc4TzRJU2t5V25YMUp2QUVWQWh0V0tadW1vb0N6cXA0MTo='
	 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_f3ile)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
    return conn

def create_table(conn):
    sql_create_bank_table = """ CREATE TABLE IF NOT EXISTS bank (
                                        id integer PRIMARY KEY,
                                        status text NOT NULL,
                                        timestamp text,
                                        bank_code text,
                                        account_number text,
                                        beneficiary_name text,
                                        remark text,
                                        receipt text,
                                        fee integer,
                                        time_served text
                                    ); """

    if conn is not None:
        create_table(conn, sql_create_bank_table)
    else:
        print("Error! cannot create the database connection.")

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
            # print(json_response)
            return json_response
    except:
        return None

def add_to_db(id, status, receipt, time_served):
    pass

def update_to_db(id, status, receipt, time_served):
    #connect to local server and update
    pass


disburse_status('1')
