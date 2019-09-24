import sys
import slightlyBigFlipLibrary as flip_lib


if __name__ == '__main__':
    conn = flip_lib.create_connection('./bank.db')
    flip_lib.create_table(conn)

    if len(sys.argv) == 2:
        _, _id = sys.argv
        response = flip_lib.disburse_status(_id)
        if response:
            print(response)
            flip_lib.update_to_db(
                conn,
                response['id'],
                response['status'],
                response['receipt'],
                response['time_served']
                )
        else:
            print("Problem with connection")
    else:
        print("Wrong number of arguments")