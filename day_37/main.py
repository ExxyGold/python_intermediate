import requests
from datetime import datetime

USERNAME = "exaltgod"
TOKEN = "Exxy12345"
GRAPH_ID = "graph12"
pixela_endpoint = "https://pixe.la/v1/users"


user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"}


# response = requests.post(url = pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url= graph_endpoint, json= graph_config, headers= header)
# print(response.text)

today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_config = {
    "date": date,
    "quantity": input("How many Kilometers did you cycle today? ")
}

pi_response = requests.post(url = pixel_endpoint, json = pixel_config, headers= header)
print(pi_response.text)

update_pixel = {
    "quantity": "12"
}


# update_pi = requests.put(url = f"{pixel_endpoint}/{date}", json = update_pixel, headers= header)
# print(update_pi.text)


# delete_pi = requests.delete(url = f"{pixel_endpoint}/{date}", headers= header)
# print(update_pi.text)