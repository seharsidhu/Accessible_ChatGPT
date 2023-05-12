import openai
import time

# Authenticate with the OpenAI API
# openai.api_key = None

# Define the prompt for ChatGPT
prompt = "Can you number the steps of heart working?"

# Define the length and temperature of the response
length = 2048
temperature = 0.5

# Define the function to generate a response from ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=length,
        temperature=temperature
    )
    return response.choices[0].text.strip()

# Call ChatGPT and print the response
# while True:
#     user_input = input("You: ")
#     prompt += "\nUser: " + user_input
#     response = generate_response(prompt)
#     print("ChatGPT:", response)
#     time.sleep(1)



#### Sample response from ChatGBT
# ChatGPT: The steps of heart working are:
#
# 1. The heart contracts and pumps blood into the arteries.
#
# 2. The arteries carry the blood to the tissues and organs.
#
# 3. The organs and tissues use the oxygen and nutrients in the blood.
#
# 4. The blood picks up carbon dioxide and other waste products from the tissues and organs.
#
# 5. The blood returns to the heart.
#
# 6. The heart relaxes and fills with blood.
#
# 7. The cycle starts over.
#
# Process finished with exit code 0
