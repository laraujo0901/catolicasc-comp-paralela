import socket, time, sys

HOST = '127.0.0.1'
PORT = 65431

print("Iniciando cliente...")

if (len(sys.argv) == 4):
    ID = sys.argv[1]
    HOST = sys.argv[2]
    PORT = int(sys.argv[3])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Conectando ao servidor {}, port {}".format(HOST,PORT))
    s.connect((HOST, PORT))
    
    print("Iniciando ping-ping com o servidor...")

    while True:
        print("ping...")
        msg = f'ping {ID}'
        s.sendall(str.encode(msg))
        data = s.recv(1024)
        print(repr(data))
        time.sleep(1)   