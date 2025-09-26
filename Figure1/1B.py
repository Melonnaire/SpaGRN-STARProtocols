import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt


adata = sc.read_h5ad('/dellfsqd2/ST_OCEAN/USER/liuxiaobin/project/SpaGRN/StarProtocol/Mouse_brain_cell_bin.h5ad')
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
sc.pp.scale(adata, max_value=10)
sc.tl.pca(adata, svd_solver='arpack') 
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40) 
sc.tl.umap(adata)

umap_coords = adata.obsm['X_umap']
categories = adata.obs['annotation'].values
if 'annotation_colors' in adata.uns:
    category_colors = adata.uns['annotation_colors']
else:
    category_colors = None

unique_categories = np.unique(categories)

plt.figure(figsize=(8, 6))
for i, category in enumerate(unique_categories):
    indices = np.where(categories == category)[0]
    points = umap_coords[indices]
    plt.scatter(points[:, 0], points[:, 1], c=[category_colors[i]], label=f'{category}', s=1, alpha=0.6)

#plt.legend(title='Annotation', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel('UMAP1')
plt.ylabel('UMAP2')
plt.show()
