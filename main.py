import hnswlib
import numpy as np
import pickle
import json
import src


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    for (n, t, h) in \
        (('descr_path', str, 'descriptions'),
         ('index_path', str, 'embeddings'),
         ('k', int, 'number of related commits')):
        parser.add_argument(n, type=t, help=h)
    args = parser.parse_args()

    # commits = np.load(args.commit_path)

    with open(args.index_path, 'rb') as file:
        index = pickle.load(file)
    with open(args.descr_path, 'r') as file:
        descriptions = json.load(file)

    client = src.utils.make_client()

    while True:
        print('-'*100)
        print('task> ', end=' ')
        task = input().strip()
        if len(task) == 0:
            continue
        if task == 'exit':
            break

        query = src.embed.get_embedding(client, task)
        labels, distances = index.knn_query(query, k=args.k)
        
        print('Related commits: ')
        print('.'*100)
        for label in labels[0]:
            print(descriptions[label])
            print()
            print('.'*100)
    print('-'*100)
