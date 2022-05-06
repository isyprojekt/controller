import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5555")
socket.setsockopt(zmq.SUBSCRIBE, b'')

#  Do 10 requests, waiting each time for a response
while True:
    #  Get the reply.

    message = socket.recv()
    print(message)
    # message = pub.recv()
    # print("Received reply %s [ %s ]" % (message))
