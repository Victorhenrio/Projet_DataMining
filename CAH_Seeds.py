import pandas as pd
#importation des données
seeds_header = pd.read_csv('info_wheat.txt', sep ="\n", index_col=None, header = None)
print(seeds_header)

import pandas as pd
#importation des données
#from io import StringIO

#seeds_test = pd.read_csv(StringIO(''.join(l.replace('\t\t','\t') for l in open('seeds_dataset.txt'))))
#seeds_test

seeds = pd.read_csv('seeds_dataset.txt', sep ='\s+', header = seeds_header)
seeds
#seeds.columns = header_seeds
#df.columns = ['a', 'b']

#dimension des données
#print(seeds.shape)

#statistiques descriptives
#seeds.describe()