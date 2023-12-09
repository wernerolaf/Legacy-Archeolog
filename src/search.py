import hnswlib
import numpy as np
import pickle


dim = 128
num_elements = 10000

# Generating sample data
data = np.float32(np.random.random((num_elements, dim)))
ids = np.arange(num_elements)

def make_index(dim=128, ef_construction=200, M=16)
    # possible options are l2, cosine or ip
    index = hnswlib.Index(
        space='cosine',
        dim=dim,
    )
    index.init_index(
        max_elements=num_elements,
        ef_construction=ef_construction,
        M=M,
    )
    return index


index.add_items(data, ids)
index.set_ef(50)

def query(index, data):
    labels, distances = index.knn_query(data, k = 1)

def save_index(index, path):
    with open(path, 'wb') as file:
        pickle.dump(index, file)

def load_index(path):
    with open(path, 'rb') as file:
        index = pickle.load(path)
    return index

