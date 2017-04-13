# client.py

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting a client to the server 
soc.connect(("127.0.0.1", 12345))

clients_input = input("Type the message\n")  
soc.send(clients_input.encode("utf8")) # we must encode the string to bytes  
result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode

print("Result from server is {}".format(result_string))

import logging

logging.basicConfig(level=logging.INFO, filename='file.log',					# log to this file (all data will be saved to this file)
format='%(asctime)s %(message)s')                                				# include timestamp
logging.info('on 127.0.0.1 port 12345 Result from server is - '+result_string)	#saving the data in log file in this format
