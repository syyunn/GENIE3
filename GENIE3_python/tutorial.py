import GENIE3_python.GENIE3 as genie

data_path = './co-citation.txt'
data = genie.loadtxt(data_path, skiprows=1)
f = open(data_path)
gene_names = f.readlines()[0]
f.close()


gene_names = gene_names.rstrip('\n').split('\t')

VIM = genie.GENIE3(data)

import numpy as np
np.save('./VIM_co-cites', VIM)
if __name__ == "__main__":
    pass
