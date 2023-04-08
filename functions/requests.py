import requests
import json

input_data = { "key": "value" }

# Create a POST requeest to a server's API
def create_something(input_data):
    # convert data to json
    json_data = json.dumps(input_data)

    # Get our url
    url = "www.workday.com/api/somethings"

    # define headers
    headers = {
        'Content-Type': 'application/json',
    }

    # send the request / store response in response
    response = requests.post(url, headers=headers, data=json_data)

    # deserialize the response
    response_data = response.json()

    # return the response
    return response_data


print(create_something(input_data))
