from socket import *
from threading import Thread
import cmysql
def check_out(connfd):
    while True:
        cid=connfd.recv(1024)
        c=cid.decode()
        info_table=cmysql.get_coinfo(f'{c}')
        connfd.send(info_table[0].encode())
        connfd.recv(1024)
        connfd.send(info_table[1].encode())
        connfd.recv(1024)
        connfd.send(str(info_table[2]).encode())
        connfd.recv(1024)
        info=(info_table[0]+" "+info_table[1]+" "+str(info_table[2]))
        connfd.send(info.encode())
        if connfd.recv(1024)==b"##":
            break
    connfd.close()
def main():
    s=socket()
    HOST = "0.0.0.0"
    PORT = 7777
    ADDR = (HOST,PORT)
    s.bind(ADDR)
    s.listen(10)
    while True:
        try:
            connfd, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            return
        p = Thread(target=check_out, args=(connfd,))
        p.daemon = True
        p.start()
if __name__ == '__main__':
    main()
