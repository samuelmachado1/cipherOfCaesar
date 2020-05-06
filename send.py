import requests
import json

# This is the function responsible for sending the JSON file to the API
def send_form():
    POST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=YouToken"
    answer = {'answer': open('answer.json', 'rb')}
    submit = requests.post(POST, files=answer)
    
    print(submit.headers)
    

send_form()
