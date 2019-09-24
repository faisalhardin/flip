import slightlyBigFlipLibrary as flip_lib
import json
import sys

def populate():
    conn = flip_lib.create_connection('./bank.db')
    flip_lib.create_table(conn)

    filename = 'population.json'
    with open(filename, 'r') as f:
        queries = json.load(f)

    for query in queries:
        print(flip_lib.add_to_db(conn, query))

def show_all():
    conn = flip_lib.create_connection('./bank.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bank")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'populate':
            populate()
        elif sys.argv[1] == 'show':
            show_all()
        else:
            print('Wrong command')
    else:
        print('Wrong number of arguments')