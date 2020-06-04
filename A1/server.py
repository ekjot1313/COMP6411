"""
BASIC SOCKETSERVER CODE IS TAKEN FROM PYTHON3.x DOCUMENTATION WHICH CAN BE FOUND AT https://docs.python.org/3/library/socketserver.html
@author EKJOT SINGH(40082643)
"""

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        print("\n"+self.client_address[0]+" connected.")

        # recieve infinte requests from a client
        while True:
            self.data = self.request.recv(1024)
            # if data from client is null, it might have disconnected
            if not self.data:
                print("\n{} disconnected.\n".format(self.client_address[0]))
                break;
            
            # spliting incoming data bytestream into a list having option and name, age, address or phone based on option
            dlist=str(self.data,"utf-8").rstrip("\n").split('|')
            option=int(dlist[0])

            reply=""

            # if option is to print report, send back sorted contents
            if option==7:
                for name in sorted(Dict.keys(), key=lambda x:x.lower()):
                    reply=reply+name+"|"+Dict[name]["age"]+"|"+Dict[name]["address"]+"|"+Dict[name]["phone"]+"\n"

            # if option is other than print report
            else:
                name=dlist[1].strip()

                # if name sent by client is null
                if not name:
                    reply="Entered name is null."
                else:
                    # if option is Add customer
                    if option==2:
                        # if name already exists in dictionary
                        if name in Dict.keys():
                            reply="Customer already exists."
                        else:
                            # if age is digit or empty, add data into dictionary
                            if dlist[2].strip().isdigit() or (not dlist[2].strip()):
                                Dict[name]={"age":dlist[2],"address":dlist[3],"phone":dlist[4]}
                                reply="Customer added successfully."
                            else:
                                reply="Age should be empty or a number."

                    # if option is other than Add customer and name already exists in dictionary
                    elif name in Dict.keys():
                        # if option is Find customer
                        if option==1:
                            reply=name+"|"+Dict[name]["age"]+"|"+Dict[name]["address"]+"|"+Dict[name]["phone"]+"\n"

                        # else if option is Delete cutomer, delete from dictionary
                        elif option==3:
                            del Dict[name]
                            reply="Customer deleted successfully."

                        # else if option is Update customer age
                        elif option==4:
                            # if age is digit or empty, update age in dictionary
                            if dlist[2].strip().isdigit() or (not dlist[2].strip()):
                                Dict[name]["age"]=dlist[2]
                                reply="Customer age updated successfully."
                            else:
                                reply="Age should be empty or a number."

                        # else if option is Update customer address, update address in dictionary
                        elif option==5:
                            Dict[name]["address"]=dlist[2]
                            reply="Customer address updated successfully."

                        # else if option is Update customer phone, update phone in dictionary
                        elif option==6:
                            Dict[name]["phone"]=dlist[2]
                            reply="Customer phone updated successfully."

                    else:
                        reply="Customer does not exist."

            # send back reply to client in bytestream
            self.request.sendall(bytes(str(reply),"utf-8"))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    print("Server Started.")

    datafile=open("Data.txt","r")
    datalines=datafile.read().splitlines()
    Dict={}
    for line in datalines:
        lst=line.split('|')
        # lst[0] is name
        lst[0]=lst[0].strip()
        # if name is valid and age is empty or digit, add detail in dictionary
        if lst[0] and (not lst[1].strip() or lst[1].strip().isdigit()):
            # if it has name and its age is empty or a digit
            Dict[lst[0]]={"age":lst[1],"address":lst[2],"phone":lst[3]}




    

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()