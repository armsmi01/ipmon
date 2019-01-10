from requests import get
from datetime import datetime
from time import sleep
from sys import argv, exit

script, spause = argv
slptime = int(spause)

print('IP Address Monitor v1.0')
print('© 2019 Michael Armstrong, Toronto Canada')
print('Distributable under the MIT License\n')

while True:
    try:
        print((str(datetime.now())).split('.')[0],get('https://ipapi.co/ip/').text)
        sleep(slptime)
    except KeyboardInterrupt:
        break

print('\nThank you, goodbye')
exit()
