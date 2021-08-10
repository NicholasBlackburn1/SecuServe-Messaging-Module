"""
allows Secuserve Securtiy to send messges via zmq to be txted to the users
"""

import imports
import messageHandler
import const
import configparser 
import consoleLog
def main():
    
    
    PATH = str(imports.pathlib.Path().absolute())+"/data/"+"Config.ini"
    config_object = imports.ConfigParser()
    config_object.read(PATH)
    sms = config_object['SMS']
    consoleLog.Debug(PATH)
  
  
  
    
    # this is for reciving messages from the modles and sending the messages to the users
    context = imports.zmq.Context()
    message_socket =  context.socket(imports.zmq.SUB)
    message_socket.setsockopt(imports.zmq.SUBSCRIBE, b'')
    message_socket.connect("tcp://"+"127.0.0.1:5001")
    

    poller = imports.zmq.Poller()
    poller.register(message_socket, imports.zmq.POLLIN)
    Debug = sms['Debug']
    print(consoleLog.Warning("Starting the Messaging Module!"))
    print(Debug)
    if(Debug == sms['Debug']):
        Debug = False
        
    while True:
        evts = dict(poller.poll(timeout=100))
        if message_socket in evts:
        
            
            topic = message_socket.recv_string()
            status = message_socket.recv_json()
          
            
            if(topic == "PIPELINE" and Debug):
                messageHandler.sendDebugMessage(phoneNum=int(str(status['phonenum'])),message = str(status['status'])+" "+ status['pipelinePos']+" "+ status['time'], api = sms['textbelt-key'])
                
                
            if(topic == "USERS"):
                 messageHandler.sendMessage(message = "Eeeep there is a "+ status['status'] +" user named"+" "+str(status['usr'])+" "+"and here is there face"+ " "+status['image'], phoneNum=int(str(status['phonenum'])), api = sms['textbelt-key'])
                 imports.time.sleep(.5)
                
            if(topic == "ERROR" and status['ERROR']):
                imports.messageHandler.sendWarnMessage(message="SecuServe Secutity System"+status['pipelinePos'] + " "+ "at"+" "+status['time'],phoneNum=int(str(status['phonenum'])),api = imports.const.smsconfig['textbelt-key'])
            """
            if(recvstring == "CONTROL" and data['controller'] == "SHUTDOWN"):
                    imports.messageHandler.sendWarnMessage(message="Shutting down SecuServe Secutity System",phoneNum=data['phone'],api = imports.const.smsconfig['textbelt-key'])
                    exit(0)
            """        # this is only for the debug messages 
         

if __name__ == "__main__":
    main()
