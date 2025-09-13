import datetime
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

# response = requests.post(graph_endpoint, json=graph_endpoint, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_config["id"]}"
date = datetime.date.today()
formatted_date = date.strftime("%Y%m%d")

pixel_config = {
    "date": formatted_date,
    "quantity": "1"
}

response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

#https://pixe.la/v1/users/andresre/graphs/graph1.html