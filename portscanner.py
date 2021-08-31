import socket
import termcolor


def scan(target, ports):
    print(termcolor.colored(f'\n-- Starting Scan for {target}... --', 'green'))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f'[+] Port {port} Opened')
        sock.close()
    except:
        pass

targets = input('[*] Enter Targets To Scan(split them by ,): ')
ports = int(input('[*] Enter How Many Ports You Want To Scan: '))

if ',' in targets:
    print(termcolor.colored(('[*] Scanning Multiple Targets'), 'green'))
    for ip in targets.split(','):
        scan(ip.strip(' '), ports)
else:
    scan(targets, ports)

