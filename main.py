import os
from openai import OpenAI
from dotenv import load_dotenv
from src.utils import load_args

args = load_args()

client = OpenAI(
    api_key=args['api_key'], 
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You give short answers and you ask, if you should explain specific things in more detail."
        },
        {
            'role': 'user',
            'content': 'based on this git difference file, tell me what have chagned: ',
        }
    ],
    model='gpt-4',
)

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

text = diff.replace('\n', ' ')
model = 'text-embedding-ada-002'
emb = client.embeddings.create(input=[text], model=model)

emb.data[0].embedding

print(chat_completion)


