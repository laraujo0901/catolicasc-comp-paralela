import socket, sys
from threading import Thread

HOST = '127.0.0.1'
PORT = 65431

if len(sys.argv) > 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

def manage_conn(conn, addr):
    with conn:
        print("Conexão recebida de {}. Vamos conversar...".format(addr))
        while True:
            data = conn.recv(1024)
            print("Recebido de {} ".format(addr), repr(data))
            if not data:
                print("Sem mais dados. Encerrando conexão!")
                break
            print("Enviando pong!")
            conn.sendall(b'pong!')
    

print("Iniciando servidor socket...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Realizando binding com servidor {}, porta {}...".format(HOST, PORT))
    s.bind((HOST, PORT))

    print("Escutando porta...")
    s.listen()

    while True:
        print("Aguardando conexões...")
        conn, addr = s.accept()
        
        # criar nova thread
        thread = Thread(target=manage_conn, args=(conn,addr))
        thread.start()
        