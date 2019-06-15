import socket

HOST = '127.0.0.1'
PORT = 65431

print("Iniciando cliente...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Conectando ao servidor {}, port {}".format(HOST,PORT))
    s.connect((HOST, PORT))
    
    print("Enviando dados para o servidor...")
    s.sendall(b'Hello, world')

    print("Recebendo dados do servidor...")
    data = s.recv(1024)

print('Recebido: ', repr(data))