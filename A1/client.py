"""
BASIC SOCKETSERVER CODE IS TAKEN FROM PYTHON3.x DOCUMENTATION WHICH CAN BE FOUND AT https://docs.python.org/3/library/socketserver.html
@author EKJOT SINGH(40082643)
"""

import socket
import sys



HOST, PORT = "localhost", 9999

# this function split (name|age|address|phone) string into a list and display it on screen
def printDetails(detail):
	if detail:
		lst=detail.split("|")
		print("Name: "+lst[0]+"\n\t Age: "+lst[1]+"\n\t Address: "+lst[2]+"\n\t Phone: "+lst[3])


# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    # repeat user-menu infinitely
    while True:
    	print("\nPython DB Menu\n")
    	print("1. Find customer")
    	print("2. Add customer")
    	print("3. Delete customer")
    	print("4. Update customer age")
    	print("5. Update customer address")
    	print("6. Update customer phone")
    	print("7. Print report")
    	print("8. Exit\n")
    	option=int(input("Select:"))

    	data=str(option)

    	if option==1:
    		name=input("Enter customer name: ")
    		
    		data=data+"|"+name
    		

    	elif option==2:
    		name=input("Enter customer name: ")
    		age=input("Enter customer age: ")
    		address=input("Enter customer address: ")
    		phone=input("Enter customer phone: ")

    		data=data+"|"+name+"|"+age+"|"+address+"|"+phone

    	elif option==3:
    		name=input("Enter customer name: ")

    		data=data+"|"+name

    	elif option==4:
    		name=input("Enter customer name: ")
    		age=input("Enter customer new age: ")

    		data=data+"|"+name+"|"+age

    	elif option==5:
    		name=input("Enter customer name: ")
    		address=input("Enter customer new address: ")

    		data=data+"|"+name+"|"+address

    	elif option==6:
    		name=input("Enter customer name: ")
    		phone=input("Enter customer new phone: ")

    		data=data+"|"+name+"|"+phone

    	elif option==7: 
    		data=data
    	elif option==8:
    		print("Good Bye.")
    		sock.close()
    		break

    	else:
    		print("Select valid option.")
    		continue

    	# sending option selected and other details to server as a bytestream
    	sock.sendall(bytes(data + "\n", "utf-8"))
    	# Receive data bytestream from the server and convert to string
    	received = str(sock.recv(1024), "utf-8")
    	
    	# if recieved data is of form (name|age|address|phone) ,i.e., Find customer or Print report option
    	if "|" in received:

    		# if data has many records ,i.e., data recieved for print report option
    		if "\n" in received:
    			lst=received.split("\n")
    			
    			# for all records
    			for detail in lst:
    				printDetails(detail)
    		else:
    			printDetails(received)
    	else:
    		print("\n"+received)
