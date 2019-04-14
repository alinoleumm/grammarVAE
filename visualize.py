import pickle
import gzip
from rdkit.Chem import MolFromSmiles
from rdkit.Chem import Draw

def load_object(filename):
	with gzip.GzipFile(filename, 'rb') as source: result = source.read()
	ret = pickle.loads(result)
	source.close()
	return ret

mapping = {}
counter = 0
for j in range(1, 11):
	if j == 8:
		iteration = 2
	else:
		iteration = 5
	for i in range(iteration):
		smiles = load_object('smiles/sim{}/valid_smiles{}.dat'.format(j, i))
		for smile in smiles:
			if smile is None:
				continue
			mol = MolFromSmiles(smile)
			try:
				img = Draw.MolsToGridImage([mol], molsPerRow = 1, subImgSize=(300, 300), useSVG=True)
			except:
				pass
			print(smile)
			mapping.update({counter : smile})
			with open("molecule_images/" + str(counter) + ".svg", "w") as text_file:
			    text_file.write(img)
			counter += 1
with open('id_to_smile.pickle', 'wb') as handle:
	pickle.dump(mapping, handle, protocol=pickle.HIGHEST_PROTOCOL)
