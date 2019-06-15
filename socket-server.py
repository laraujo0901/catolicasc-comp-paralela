import socket

HOST = '127.0.0.1'
PORT = 65431

print("Iniciando servidor socket...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Realizando binding com servidor {}, porta {}...".format(HOST, PORT))
    s.bind((HOST, PORT))
    print("Escutando porta...")
    s.listen()
    print("Aguardando conexões...")
    conn, addr = s.accept()
    with conn:
        print("Conexão recebida de {}. Vamos conversar...".format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                print("Sem mais dados. Encerrando conexão!")
                break
            conn.sendall(data)