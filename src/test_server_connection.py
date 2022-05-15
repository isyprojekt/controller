import zmq

ctx = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
sub = ctx.socket(zmq.SUB)
sub.connect("tcp://127.0.0.1:5555")
sub.setsockopt(zmq.CONFLATE, True)
sub.setsockopt(zmq.SUBSCRIBE, b'')

#  Do 10 requests, waiting each time for a response
for _ in range(10):
    message: dict = sub.recv_json()
    print(message)
sub.close()
