import json
import requests
from data import dimensionData;
from config import headers;

def send_dimensions_request():

    # Convert to dictionary
    json_data = json.dumps(dimensionData)

    url = "https://jmeds112--full.sandbox.my.salesforce.com/services/data/v56.0/sobjects/:SOBJECT_API_NAME"
    response = requests.post(url, headers=headers, data=json_data)

    if response.status_code == 200:
        print("GREAT!")
        print(response.json())  # Get the response
    else:
        print("ERROR")
        print(response.text)  # Get the error

if __name__ == "__main__":
    send_dimensions_request()
