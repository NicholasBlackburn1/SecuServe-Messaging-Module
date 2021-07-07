"""
allows Secuserve Securtiy to send messges via zmq to be txted to the users
"""

from zmq.sugar.frame import Message
import __init__

def main():
    # this is for reciving messages from the modles and sending the messages to the users
    context = __init__.zmq.Context()
    message_socket =  context.socket(__init__.zmq.SUB)
    message_socket.setsockopt(__init__.zmq.SUBSCRIBE, b'')
    message_socket.connect("tcp://"+"127.0.0.1:5001")
    
    recvmsg = message_socket.recv_json()
    


if __name__ == "__main__":
    main()
