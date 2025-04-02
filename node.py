import time
import requests

API_URL = "http://localhost:5000/add_node"

def register_node():
    response = requests.post(API_URL, json={"cpu": 4})  # Register with 4 CPU cores
    print(response.json())

if __name__ == "__main__":
    time.sleep(2)  # Wait for API to start
    register_node()
    while True:
        time.sleep(10)  # Simulate node activity
