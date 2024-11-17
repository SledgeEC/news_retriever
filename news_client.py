# client to request

import json
import zmq

this = zmq.Context()

print("Connecting to zero_server...")
# reply socket to communicate with server
rep_socket = this.socket(zmq.REQ)
rep_socket.connect("tcp://localhost:5555")

#  Do..while to run until return message is received
while True:
    # send request to zero_server
    print("Sending request")
    # send string to server
    rep_socket.send_string("Start API request")

    #  get reply
    response = rep_socket.recv_json()

    # print reply
    print(response)

    # end do..while if correct message received
    #if (response == "Response received"):
    if (response):
        break
