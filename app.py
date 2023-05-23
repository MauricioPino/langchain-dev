import json
import requests
from data import dimensionData;
from config import headers;
from endpoints import get_endpoint, post_endpoint

def main():

    # POST request
    post_response = requests.post(post_endpoint, headers=headers, data=json.dumps(dimensionData))
    if post_response.status_code == 200:
        print("GREAT!")
        print(post_response.json())
    else:
        print("Error sending POST request")
        print(post_response.text)

    # GET dimensions
    get_response = requests.get(get_endpoint, headers=headers)
    if get_response.status_code == 200:
        dimensions_data = get_response.json()
        print("Dimensions from FF sandbox: ")
        print(dimensions_data)
    else:
        print("Error sending GET request")
        print(get_response.text)

if __name__ == '__main__':
    main()
