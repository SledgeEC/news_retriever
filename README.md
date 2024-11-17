News retriever API for OSU - CS361 microservice

To request data from the microservice:
The server-client relationship for this microservice utilizes the request / reply pattern. To initiate, the client needs a request socket connected to tcp://localhost:5555, then to send a string to the server (any string will do).
Example from python: 
this = zmq.Context()
socket.connect(‘tcp://localhost:5555’)
socket.send_string(‘GO!’)

To receive the response from the service:
To obtain the reply, the client should use a loop to wait for the server to respond and then store the JSON.
Example from python:
response = socket.recv_json()

UML sequence diagram:
![news_retriever UML](https://github.com/user-attachments/assets/83fa1883-ab96-4a3b-9a7c-b7b993217060)
