import time, requests, traceback, os

import openai
import chatgpt
import dalee

import spacy
nlp = spacy.load("en_core_web_sm")

# Authenticate with the OpenAI API
openai.api_key = 'sk-*' #ask for a key at https://platform.openai.com/account/api-keys
dalee.headers['Authorization'] = f'Bearer {openai.api_key}'

q = 1
while True:
    user_input = input(f'Question {q}:\n')
    chatgpt.prompt = '\nUser: ' + user_input
    response = chatgpt.generate_response(chatgpt.prompt)
    print('ChatGPT:\n', response)

    question_folder = f'./q{q}/'
    if not os.path.isdir(question_folder): os.makedirs(question_folder)
    for step, prompt in enumerate(nlp(response).sents):
        filename = f'{question_folder}step{step + 1}.jpg'
        try:
            url = dalee.generate_image(str(prompt))
            for i in range(5):
                response = requests.get(url)
                if response.status_code == 200:
                    with open(filename, 'wb') as f: f.write(response.content)
                    print(f'Step {step + 1}: {prompt}')
                    print(f'Image for step: {step + 1} has been downloaded successfully as {filename} after {i+1} try!')
                    break
            else: raise Exception
        except:
            print(f'Failed to download image for step: {step+1} at url: {url}')
            traceback.print_exc()
            print()
    q = q + 1


