import sys
import slightlyBigFlipLibrary as flip_lib

if __name__ == '__main__':
    print((sys.argv))
    if len(sys.argv) == 5:
        _, _id, status, receipt, time_served = sys.argv
        response = flip_lib.disburse(_id, status, receipt, time_served)
        if response:
            flip_lib.update_database(
                response['id'],
                response['status'],
                response['receipt'],
                response['time_served']
                )
        else:
            print("Problem with connection")
    else:
        print("Wrong number of arguments")