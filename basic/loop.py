#This program is practice loop / import

import sys

while True:
    print('Type exit to exit.')
    response = input();
    if response == 'exit':
        sys.exit();
    print('your Type is ' + response)
