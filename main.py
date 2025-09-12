import requests
import os
from dotenv import load_dotenv

load_dotenv()

username = "andresre"
api_token = os.getenv("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": api_token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "My Calories Tracker",
    "unit": "calory",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": api_token
}

response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(response.text)