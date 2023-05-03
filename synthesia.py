import requests
import json

SYNTHESIA_API_KEY = '<your Synthesia API key here>'


def generate_video():
    # Set up the request headers and data
    headers = {
        'Authorization': f'Bearer {SYNTHESIA_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'scenarioId': '<scenario ID>',
        'data': {
            'actor': {
                'name': 'John Doe'
            },
            'text': 'Hello, world!'
        }
    }

    # Send the request to the API
    response = requests.post('https://api.synthesia.io/v1/videos', headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the video URL
        response_data = json.loads(response.text)
        video_url = response_data['url']
        print(f'Video generated successfully! URL: {video_url}')
    else:
        print(f'Error generating video! Status code: {response.status_code}, Message: {response.text}')
