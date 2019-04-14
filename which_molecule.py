import pickle
import sys

with open('id_to_smile.pickle', 'rb') as handle:
    mapping = pickle.load(handle)

print(mapping[int(sys.argv[1])])