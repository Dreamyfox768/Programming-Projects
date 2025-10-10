#Implementing AI in python is easy 
# install package prefered AI agent
import openai

# Replace with your actual API key 
openai.api_key = "YOUR_API_KEY"

# Get user input
prompt = input("Enter a prompt: ")

# Create a chat completion
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

# Print the assistant's reply
print(response['choices'][0]['message']['content'])
