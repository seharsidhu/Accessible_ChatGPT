import requests
import json

# Replace YOUR_API_KEY with your OpenAI API key
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ???',
}

# Define the prompt for DALL-E
prompt = "The heart pumps blood through the body in a process called circulation."

# Define the size of the output image
size = "512x512"

# Define the function to generate an image from DALL-E
def generate_image(prompt):
    data = {
        'model': 'image-alpha-001',
        'prompt': prompt,
        'size': size,
    }
    response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, data=json.dumps(data))
    response_data = json.loads(response.content.decode())
    return response_data['data'][0]['url']

# # Call DALL-E and print the image URL
# image_url = generate_image(prompt)
# print(image_url)
