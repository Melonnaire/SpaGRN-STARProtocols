import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt


adata = sc.read_h5ad('Mouse_brain_cell_bin.h5ad') # Downloaded from https://db.cngb.org/stomics/mosta/download/ 
positions = adata.obsm['spatial']
annotations = adata.obs['annotation'].values
unique_categories = np.unique(annotations)
category_colors = ['#ffff00', '#1ce6ff', '#ff34ff', '#ff4a46', '#008941', '#006fa6',
       '#a30059', '#ffdbe5', '#7a4900', '#0000a6', '#63ffac', '#b79762',
       '#004d43', '#8fb0ff', '#997d87', '#5a0007', '#809693', '#6a3a4c',
       '#1b4400', '#4fc601', '#3b5dff', '#4a3b53', '#ff2f80', '#61615a',
       '#ba0900', '#6b7900', '#00c2a0', '#ffaa92', '#ff90c9']

plt.figure(figsize=(10, 10))
for i, category in enumerate(unique_categories):
    indices = np.where(annotations == category)[0]
    points = positions[indices]
    plt.scatter(points[:, 0], points[:, 1], c=[category_colors[i]], s=2, alpha=0.6)
plt.show()
