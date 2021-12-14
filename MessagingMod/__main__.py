"""
allows Secuserve Securtiy to send messges via zmq to be txted to the users
TODO: allow messags from the lets say manager to create status messages sent to user
"""


from messager import messageHandler
import const
from utils import consoleLog
import pathlib 
from configparser import ConfigParser
import zmq
from datetime import time

def main():
    
    
    PATH = str(pathlib.Path().absolute())+"/data/"+"Config.ini"
    config_object = ConfigParser()
    config_object.read(PATH)
    sms = config_object['SMS']
    consoleLog.Debug(PATH)
  
  
  
    
    # this is for reciving messages from the modles and sending the messages to the users
    context = zmq.Context()
    message_socket =  context.socket(zmq.SUB)
    message_socket.setsockopt(zmq.SUBSCRIBE, b'')
    message_socket.connect("tcp://"+"127.0.0.1:5001")
    

    poller = zmq.Poller()
    poller.register(message_socket, zmq.POLLIN)
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
                 time.sleep(.5)
                
            if(topic == "ERROR" and status['ERROR']):
                messageHandler.sendWarnMessage(message="SecuServe Secutity System"+status['pipelinePos'] + " "+ "at"+" "+status['time'],phoneNum=int(str(status['phonenum'])),api = const.smsconfig['textbelt-key'])
            """
            if(recvstring == "CONTROL" and data['controller'] == "SHUTDOWN"):
                    messageHandler.sendWarnMessage(message="Shutting down SecuServe Secutity System",phoneNum=data['phone'],api = const.smsconfig['textbelt-key'])
                    exit(0)
            """        # this is only for the debug messages 
         

if __name__ == "__main__":
    main()
