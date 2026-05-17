import socket
import os


PORTS = [21,22,23,25,53,80,111,135,139,443,3389]

def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def scan(ip: str) -> None:
    count = 0
    for port in PORTS:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip,port))
        if code == 0:
            if count == 0:
                print('\033[1;37m┌'+'─'*31+'┐\033[0;0m')
                print('\033[1;37m│\033[1;31mPort\tState\033[0;0m\t\t\t\033[1;37m│')
            count += 1
            print (f'\033[1;37m│{port}\t\033[0;32m open\t\t\t\033[1;37m│\033[0;0m')
    if count > 0:
        print ('\033[1;37m└'+'─'*31+'┘\033[0;0m')
    print('\033[1;37m┌'+'─'*30+'┐\033[0;0m')
    print(f'│found \033[0;32m{count}\033[0;0m ports!                │')
    print ('\033[1;37m└'+'─'*30+'┘\033[0;0m')

def main() -> None:
    while(True):
        ip = input('>> ')
        if ip == 'clear':
            clear_console()
        elif ip == 'exit':
            print('bye')
            break
        else:
            try:
                scan(ip)
            except Exception as error:
                print(f'Error: {error}')

if __name__ == '__main__':
    main()
