import socket
#import sys
#import time

s_client=socket.socket()

host=input(str("please enter the hostname of the server :"))
port=8000
s_client.connect((host,port))

print("Connection established to the server ")
while 1:
	incoming_msg=s_client.recv(1024)
	incoming_msg=incoming_msg.decode()
	print("Server : ",incoming_msg,"\n")
	print("Your turn to send msg ...")	
	send_msg=input(str(">> "))
	send_msg=send_msg.encode()
	s_client.send(send_msg)
	print("message has been sent ...")
	print("")