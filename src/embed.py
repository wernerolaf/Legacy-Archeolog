import numpy as np
import json
import src.utils
import openai
from tqdm import tqdm


def read_file(path):
    try: 
        with open(path, 'r') as file:
            txt = file.read()
    except Exception as e:
        print('ERROR: Unable to read a file.')
        txt = ' '
    return txt


def load_from_json(input_file):
    with open(input_file, 'r') as json_file:
        txt = json.load(json_file)
    return txt


def get_embedding(client, text, model='text-embedding-ada-002'):
    try:
        text = text.replace('\n', ' ')
        text = text if len(text) > 0 else ' '
        embedding = np.array(
            client.embeddings.create(
                input=[text],
                model=model
            ).data[0].embedding
        )
    except Exception as e:
        print(e)
        embedding = np.array([])
    return embedding



def describe_commit(client, commit, system_role, model='gpt-4'):
    try:
        description = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_role
                },
                {
                    'role': 'user',
                    'content': json.dumps(commit, indent=4),
                }
            ],
            model='gpt-4',
        ).choices[0].message.content
    except Exception as e:
        print(e)
        description = commit['message']

    return description


def embed_files(client, path, env):
    if path not in env:
        if os.path.isfile(path):
            env[path] = get_embedding(client, read_file(path))
        else:
            env[path] = sum([
                embed_files(os.path.join(path, item), env)
                for item in os.listdir(path)
            ])
    return env[path]




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    for (n, t, h) in \
        (('input_path', str, 'path to the commits'),
         ('descr_path', str, 'description output file'),
         ('embed_path', str, 'embeddings output file'),
         ('system_role', str, 'system role file path')):
        parser.add_argument(n, type=t, help=h)
    args = parser.parse_args()

    # client = openai.OpenAI(
    #     api_key=src.utils.load_args()['api_key'],
    #)
    client = src.utils.make_client()
    
    system_role = read_file(args.system_role)
    print("System role: ")
    print(system_role)
    print()

    commit_data = load_from_json(args.input_path)

    descriptions = [
        describe_commit(
            client,
            commit,
            system_role
        )
        for commit in tqdm(commit_data)
    ]

    embeddings = [
        get_embedding(client, description)
        for description in tqdm(descriptions)
    ]
    zero = np.zeros((max([emb.shape[0] for emb in embeddings]),))
    embeddings = np.stack([
        zero if emb is emb.shape[0] == 0 else emb
        for emb in embeddings
    ])
    
    # SAVING
    with open(args.descr_path, 'w') as json_file:
        json.dump(descriptions, json_file, indent=2)
    np.save(args.embed_path, embeddings)
