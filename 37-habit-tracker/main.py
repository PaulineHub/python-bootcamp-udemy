import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fbiwuy398yr5huhwr983h"
USERNAME = "paulinehub"
GRAPH_ID = "graph1"

# ------------------------------------------------------------
## Create the user account on Pixela https://pixe.la/

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ---------------------------------------------------------
## Create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "sport graph",
    "unit": "min",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response)

# ---------------------------------------------------------
## Add pixels to the graph with POST

graph_id_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.today().strftime("%Y%m%d")
quantity = "30"

pixel_params = {
    "date": today,
    "quantity": quantity
}

# response = requests.post( url=graph_id_endpoint, json=pixel_params, headers=headers)
# print(response)

# ---------------------------------------------------------
## Update pixels with PUT

date_to_update = today
graph_date_endpoint = f"{graph_id_endpoint}/{date_to_update}"

pixel_to_update_params = {
    "quantity": "40"
}

# response = requests.put(url=graph_date_endpoint,json=pixel_to_update_params, headers=headers)
# print(response)

# ---------------------------------------------------------
## Delete pixels with DELETE

response = requests.delete(url=graph_date_endpoint,headers=headers)
print(response)
