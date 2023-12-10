import hnswlib
import numpy as np
import pickle


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    for (n, t, h) in \
        (('commit_path', str, 'commits'),
         ('descr_path', str, 'descriptions'),
         ('index_path', str, 'embeddings')):
        parser.add_argument(n, type=t, help=h, required=True)
    args = parser.parse_args()

    commits = np.load(args.commit_path)
    with open(args.index_path, 'rb') as file:
        index = pickle.load(file)
    with open(args.descr_path, 'r') as file:
        descriptions = json.load(file)

    labels, distances = index.knn_query(data, k=1)
