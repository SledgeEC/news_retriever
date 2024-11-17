import json
import requests
import zmq

# news retriever API for OSU - CS 361 microservice

# thenewsapi api key
key = "lE1ZStZbsrXC9v10aOU2ZrVJW8gdg99ARPHXj3ld"
url = "https://api.thenewsapi.com/v1/news/top?locale=us&language=en&api_token="

# context for ZeroMQ
this = zmq.Context()

# get reply socket for comms
rep_socket = this.socket(zmq.REP)

# localhost to send and recive messages
rep_socket.bind("tcp://*:5555")


def api_call():
    try:
        # make call to API
        site = url + key
        response = requests.get(site)

        data = {}

        # check if response successful
        if response.status_code == 200:
            posts = response.json()

            if posts:
                counter = 0

                for post in posts["data"]:
                    title = post.get("title")
                    summary = post.get("description")
                    link = post.get("url")

                    article = {
                        "article_name": title,
                        "article_summary": summary,
                        "article_url": link
                    }

                    data[counter] = article
                    counter = counter + 1
                
                return data
            
        else:
            return response
    except requests.exceptions.RequestException as e:
        return {"Error": e.args}
    

# main function to receive request and return response
def main():
    # do..while to wait for client requests
    while True:
        # wait for client request
        message = rep_socket.recv_string()
        # call API
        result = api_call()
        # return result
        rep_socket.send_json(result)


# call main to run loop and wait for client requests
main()


