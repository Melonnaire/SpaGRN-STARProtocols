import scanpy as sc
import matplotlib.pyplot as plt
from spagrn.regulatory_network import InferNetwork as irn

adata_full2 = sc.read_h5ad('Mouse_brain_cell_bin.h5ad')
adata_full2 = irn.preprocess(adata_full2, min_genes=1000, min_cells=300, min_counts=10, max_gene_num=4000)

sc.pp.normalize_total(adata_full2, target_sum=1e4)
sc.pp.log1p(adata_full2)
adata_full2.raw = adata_full2

sc.pp.highly_variable_genes(adata_full2, min_mean=0.0125, max_mean=3, min_disp=0.5)
adata_full2 = adata_full2[:, adata_full2.var.highly_variable]

sc.pp.scale(adata_full2, max_value=10)
sc.tl.pca(adata_full2, svd_solver='arpack')
sc.pp.neighbors(adata_full2, n_neighbors=10, n_pcs=40)
sc.tl.umap(adata_full2)

fig2, ax2 = plt.subplots(figsize=(12, 7))
sc.pl.umap(adata_full2, color='annotation', legend_loc='right margin', show=False, ax=ax2)

plt.tight_layout()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.rcParams["font.family"] = "Arial"
plt.show()
