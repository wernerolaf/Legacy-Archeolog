import numpy as np
import os
from openai import OpenAI
from dotenv import load_dotenv
from utils import load_args


args = load_args()

client = OpenAI(
    api_key=args['api_key'], 
)


def list_dirs(path):
    return [f for f in os.listdir() if not os.path.isfile(f)]


def get_embedding(text, model='text-embedding-ada-002'):
   text = text.replace('\n', ' ')
   text = text if len(text) > 0 else ' '
   return np.array(
        client.embeddings.create(
            input=[text],
            model=model
        ).data[0].embedding
   )


def read_file(path):
    try: 
        with open(path, 'r') as file:
            txt = file.read()
    except Exception as e:
        print(path)
        txt = ' '
    return txt


def embed(path, env):
    if path not in env:
        print(path)
        if os.path.isfile(path):
            env[path] = get_embedding(read_file(path))
        else:
            env[path] = sum([
                embed(os.path.join(path, item), env)
                for item in os.listdir(path)
            ])
    return env[path]
