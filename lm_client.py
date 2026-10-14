import requests


def send(History,Command):
    History.append({"role": "user", "content": Command})
    payload= {"model": "gemma4-26b-a4b-qat-uncensored-hauhaucs-balanced-mtp", "messages":History}
    response = requests.post("http://localhost:1234/v1/chat/completions", json=payload, timeout=120)
    response.raise_for_status()
    result= response.json()
    answer = result['choices'][0]['message']['content']
    History.append({"role": "assistant", "content": answer})
    print("Status:", response.status_code)
    print("Result: ", answer)

history= []
    
while True:
        try: 
            command = input("Enter a command, or stop: ")

            if command == "stop":
                break
            
            send(history,command)

        except requests.exceptions.Timeout:
            print("LM Studio took too long to respond.") 
            history.pop()

        except requests.exceptions.HTTPError as error:
            print("HTTP error:", error.response.status_code)
            print("Details:", error.response.text)
            history.pop()
            
        except requests.exceptions.ConnectionError:
            print ("Cannot connect to LM Studio. Check that the server is running.")
            history.pop()
            

   



