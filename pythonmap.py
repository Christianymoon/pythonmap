import nmap
import argparse
import os, time
from colorama import init, Fore, Back

#initialize colors 
init()

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group() # fix confilctive parameters
#Automatized command line 
parser.add_argument('--superscan', help='high speed exhaustive super scan (very noisy)', action="store_true")
#Essentials parameters
parser.add_argument('-t', '--target', help='ip address of the target host', type=str)
group.add_argument('-p', '--port', help='specifies host port', nargs='*', type=int)
group.add_argument('--allports', help='scann all ports', action="store_true")
parser.add_argument('-v', '--verbose', help="prints additional data on output", action="store_true")
parser.add_argument('--open', help='scan only open ports', action='store_true')
args = parser.parse_args()

nm = nmap.PortScanner()# nnmap object 

def validatePortsList(ports):
    validPortsList = []
    for port in ports:
        if port > 0 and port <= 65536:
            validPortsList.append(port)
        else:
            print(f'the port is {Fore.RED}unreachable{Fore.RESET} {port} skipping...')
            time.sleep(1.5)
    validPortsStr = ', '.join(map(str, validPortsList))

    return validPortsStr

def getActivePorts(activeHosts):
    for host in activeHosts:
        print('----------------------------------------------------')
        print(f'Ip adress: {host} | state: {nm[host].state()}')
        ports = nm[host]['tcp'].keys()
        print(f'\nACTIVE PORTS TCP SYN PORT SCAN\n')
        time.sleep(1)
        for port in ports:
            portInfo = nm[host]['tcp'][port]        
            print(Fore.CYAN + f'HOST {host} | PORT {port}\n' + Fore.RESET)
            print(Fore.WHITE + f"\t\tPort state : {portInfo['state']}\n" + Fore.RESET)
            print(Fore.WHITE + f"\t\tService    : {portInfo['name']}\n" + Fore.RESET)
            print(Fore.WHITE + f"\t\tReason     : {portInfo['reason']}\n" + Fore.RESET)
            print(Fore.CYAN + '----------------------------------------------------\n' + Fore.RESET)
            time.sleep(1)
        if args.open:
            print(Fore.CYAN + "targeted file has been created or updated\n" + Fore.RESET)
    print(Back.BLUE + Fore.WHITE + '\bSCAN FINISHED' + Fore.RESET + Back.RESET)

if args.verbose and args.target and args.port or args.superscan:
    print( Fore.CYAN + f'\nWelcome to port scanner by Christian VR aka Kittay\n' + Fore.RESET)
    print(f'TARGETED IP ADRESS {args.target}')
    print(f'TARGETED PORT HOST {args.port}\n')

#TCP SYN Port scann (-sS)
if args.target and args.port and not args.superscan:

    validPorts = validatePortsList(args.port)
    print(f'\nInitializing normal scan in {args.target} port: {validPorts}\n')
    nm.scan(args.target, validPorts, arguments='-n') #argumentos para escaneo normal   
    nm.command_line()
    nm.scaninfo()
    hosts = nm.all_hosts() 
    getActivePorts(hosts)

elif args.allports or args.port and args.superscan:
    print(f'\nInitializing super exhaustive scan in {args.target} port: {args.port}\n')

    if args.allports and args.open:
        nm.scan(args.target, '0-65535', arguments= '--open -sS -n --min-rate 5000 -oN targeted') #argumentos para super escaneo 
        nm.command_line()
        nm.scaninfo()
        hosts = nm.all_hosts()
    elif args.allports and not args.open:
        nm.scan(args.target, '0-65535', arguments= '-sS -n --min-rate 5000 -oN targeted') #argumentos para super escaneo 
        nm.command_line()
        nm.scaninfo()
        hosts = nm.all_hosts()
    else:
        validPorts = validatePortsList(args.port)
        nm.scan(args.target, validPorts, arguments= '-sS -n --min-rate 5000') #argumentos para super escaneo de puertos individuales
        nm.command_line()
        nm.scaninfo()
        hosts = nm.all_hosts()

    getActivePorts(hosts)

else:
    print(Back.RED + Fore.WHITE + "INVALID OPTIONS OR BAD OPTIONS" + Fore.RESET + Back.RESET)
