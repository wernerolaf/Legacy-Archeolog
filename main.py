import os
from openai import OpenAI
from dotenv import load_dotenv
from utils import load_args

args = load_args()

client = OpenAI(
    api_key=args['api_key'], 
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': 'Say this is a test',
        }
    ],
    model='gpt-4',
)

print(chat_completion)
