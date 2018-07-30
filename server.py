import socket
#import sys
#import time

s_server1=socket.socket()
s_server2=socket.socket()
host=socket.gethostname()

print("Server will start on host : ",host)

port1=8000
port2=8910

s_server1.bind((host,port1))
s_server2.bind((host,port2))

print("server done binding to host and port successfully")
print("Server is waiting for incoming connections")

s_server1.listen(1)
s_server2.listen(1)

#print(type(s.accept()))

#print("Address is ",Address," type : ",type(Address))
#print("Connection is ",conn," type : ",type(conn))

print("waiting for client1 to get connected ...")

conn1,Address1=s_server1.accept()
print("Client1 ",Address1," has connected to the server\n")

print("waiting for client2 to get connected ...")

conn2,Address2=s_server2.accept()
print("Client2 ",Address2," has connected to the server\n")

while 1:
	send_msg=input(str(">> "))
	send_msg=send_msg.encode()
	conn1.send(send_msg)
	conn2.send(send_msg)
	print("message has been sent ...")
	print("")

	incoming_msg1=conn1.recv(1024)
	incoming_msg1=incoming_msg1.decode()
	print("Client1 : ",incoming_msg1,"\n")

	print("Waiting for Client2 to send message ...\n")

	incoming_msg2=conn2.recv(1024)
	incoming_msg2=incoming_msg2.decode()
	print("Client2 : ",incoming_msg2,"\n")