import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "sxxxse"  # Name of your choice
TOKEN = "fkxxxgir3293"  # Your chosen token
graph_id = "graph1"  # Name of your graph

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# To create new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Workout Graph",
    "unit": "mins",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# To create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you workout today? ")
}

# To add pixel to the graph
response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


put_delete_endpoint = f"{post_pixel_endpoint}/{pixel_config['date']}"

put_config = {
    "quantity": "18"
}

# To update
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

# To delete
# response = requests.delete(url=put_delete_endpoint, headers=headers)
# print(response.text)
