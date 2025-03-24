import requests

# Define the API URL
url = "http://127.0.0.1:5000/event"

# Define the event data (JSON)
data = {
    "event": "fire_alarm"
}

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response:", response.json())
