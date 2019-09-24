import sys
import slightlyBigFlipLibrary as flip_lib

if __name__ == '__main__':

    conn = flip_lib.create_connection()
    create_table(conn)


    if len(sys.argv) == 5:
        _, _id, status, receipt, time_served = sys.argv
        response = flip_lib.disburse(_id, status, receipt, time_served)
        if response:
            response['amount'] = int(response['amount'])
            response['fee'] = int(reponse['fee'])
            flip_lib.add_to_db(response)
        else:
            print("Problem with connection")
    else:
        print("Wrong number of arguments")