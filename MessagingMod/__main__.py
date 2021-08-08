"""
allows Secuserve Securtiy to send messges via zmq to be txted to the users
"""

import imports
import messageHandler
import const
def main():
   
    # this is for reciving messages from the modles and sending the messages to the users
    context = imports.zmq.Context()
    message_socket =  context.socket(imports.zmq.SUB)
    message_socket.setsockopt(imports.zmq.SUBSCRIBE, b'')
    message_socket.connect("tcp://"+"127.0.0.1:5001")
    

    poller = imports.zmq.Poller()
    poller.register(message_socket, imports.zmq.POLLIN)
    Debug = True
    while True:
        evts = dict(poller.poll(timeout=100))
        if message_socket in evts:
        
            
            topic = message_socket.recv_string()
            status = message_socket.recv_json()
            print(topic)
            
            if(topic == "PIPELINE" and Debug):
                messageHandler.sendDebugMessage(phoneNum=4123891615,message = str(status['status'])+" "+ status['pipelinePos']+" "+ status['time'], api = '')
                
                
            if(topic == "USERS"):
                 messageHandler.sendMessage(message = "Eeeep there is a "+ status['status'] +" user named"+" "+str(status['usr'])+ "and here is there face"+ " "+status['image'], phoneNum=4123891615, api = '')
                
            if(topic == "ERROR"):
                print(Fore.RED+f"Topic: {topic} => {status}")
                print(Fore.RESET)
            """
            if(recvstring == "CONTROL" and data['controller'] == "SHUTDOWN"):
                    imports.messageHandler.sendWarnMessage(message="Shutting down SecuServe Secutity System",phoneNum=data['phone'],api = imports.const.smsconfig['textbelt-key'])
                    exit(0)
            """        # this is only for the debug messages 
         

if __name__ == "__main__":
    main()
