import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt

adata_full = sc.read_h5ad('Mouse_brain_cell_bin.h5ad')

sc.pp.normalize_total(adata_full, target_sum=1e4)
sc.pp.log1p(adata_full)
adata_full.raw = adata_full

sc.pp.highly_variable_genes(adata_full, min_mean=0.0125, max_mean=3, min_disp=0.5)
adata_full = adata_full[:, adata_full.var.highly_variable]

sc.pp.scale(adata_full, max_value=10)
sc.tl.pca(adata_full, svd_solver='arpack')
sc.pp.neighbors(adata_full, n_neighbors=10, n_pcs=40)
sc.tl.umap(adata_full)

fig, ax = plt.subplots(figsize=(12, 7))
sc.pl.umap(adata_full, color='annotation', legend_loc='right margin', show=False, ax=ax)

plt.tight_layout()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.rcParams["font.family"] = "Arial"
plt.show()
