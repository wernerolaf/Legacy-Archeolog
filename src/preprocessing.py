import json

def load_from_json(input_file):
    with open(input_file, 'r') as json_file:
        txt = json.load(json_file)
    return txt

def get_embedding(text, model="text-embedding-ada-002"):
   text = text.replace("\n", " ")
   return client.embeddings.create(
        input=[text],
        model=model).data[0].embedding

data = load_from_json('./commits.json')


