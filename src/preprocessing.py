import json
import src.embed
import src.utils



if __name__ == "__main__":
    with open('system_role.txt', 'r') as file:
        system_role = file.read()
    

    data = load_from_json('data/commits.json')

    embeddings = [src.embed.embed_commit(client, commit, embed) for commit in data]

    
