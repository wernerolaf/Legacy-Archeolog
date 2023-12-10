import hnswlib
import numpy as np
import pickle


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    for (n, t, h) in \
        (('input_path', str, 'embeddings path'),
         ('output_path', str, 'index output path'),
         ('num_elements', int, 'maximmum number of elements')):
        parser.add_argument(n, type=t, help=h)
    args = parser.parse_args()


    data = np.load(args.input_path)

    index = hnswlib.Index(
        space='cosine',
        dim=data.shape[1],
    )
    index.init_index(
        max_elements=args.num_elements,
        ef_construction=200,
        M=16,
    )
    
    ids = np.arange(data.shape[0])
    index.add_items(data, ids)
    index.set_ef(50)

    with open(args.output_path, 'wb') as file:
        pickle.dump(index, file)

