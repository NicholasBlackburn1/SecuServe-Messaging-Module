"""
allows Secuserve Securtiy to send messges via zmq to be txted to the users
"""

import __init__

def main():
    # this is for reciving messages from the modles and sending the messages to the users
    context = __init__.zmq.Context()
    message_socket =  context.socket(__init__.zmq.SUB)
    message_socket.setsockopt(__init__.zmq.SUBSCRIBE, b'')
    message_socket.connect("tcp://"+"127.0.0.1:5002")
    
    while message_socket.recv_json() !=None:
        recvstring = message_socket.recv_string()
        recvmsg = message_socket.recv_json()
        data = __init__.json.load(recvmsg)
        
        
        # this is only for the debug messages 
        if(recvstring == "PIPE"):
            __init__.messageHandler.sendDebugMessage(str(data['status'])+" "+ data['pipelinePos']+" "+ data['time'], api = __init__.const.smsconfig['textbelt-key'])
            
        
        if(recvstring == "REC"):
            __init__.messageHandler.sendMessage(message = "Eeeep there is a "+ data['status'] +" user named"+" "+str(data['user'])+ "and here is there face"+ " "+data['imgurl'], phoneNum=data['phone'], api = __init__.const.smsconfig['textbelt-key'])
            
        if(recvstring == "CONTROL" and data['controller'] == "SHUTDOWN"):
                __init__.messageHandler.sendWarnMessage(message="Shutting down SecuServe Secutity System",phoneNum=data['phone'],api = __init__.const.smsconfig['textbelt-key'])
                exit(1001)
            

if __name__ == "__main__":
    main()
