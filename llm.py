import openai

openai.api_key = "your-api-key-here"

# Function to generate a reply
def generate_reply(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        message=[
            {"role": "system", "content": "You write professional and concise email replies."},
            {"role": "user", "content": f"Write a reply to this urgent message:\n{message}"}
        ]
    )
    return response.choices[0].message['content']