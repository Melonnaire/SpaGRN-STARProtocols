import scanpy as sc
import numpy as np
import plotly.graph_objects as go


def calculate_mean_expression(adata, celltype, gene):
    adata_gene = adata[adata.obs['annotation'] == celltype, adata.var.index.str.lower() == gene.lower()]
    return np.mean(adata_gene.X.toarray())


receptors = ['Cntnap2', 'Erbb4', 'Nrxn3']
targets =  ["Elavl2","Vstm2a","Gad1","Arl4c","Sema3c","Adarb2","Mtss1","Cnr1","Gad2","Synpr","Reln","Sst"]
tf = 'Dlx1'

data=sc.read_h5ad('/dellfsqd2/ST_OCEAN/USER/liuxiaobin/project/SpaGRN/StarProtocol/Mouse_brain_cell_bin.h5ad')
receptor_exp = [calculate_mean_expression(data, 'IN Sst+', x) for x in receptors]
target_exp = [calculate_mean_expression(data, 'IN Sst+', x) for x in targets]

receptor_weight = receptor_exp/sum(receptor_exp)
target_weight = target_exp/sum(target_exp)

nodes = receptors + [tf] + targets

links = {
    "source": [],
    "target": [],
    "value": []
}

for receptor in receptors:
    links["source"].append(nodes.index(receptor))
    links["target"].append(nodes.index(tf))
    links["value"].append(receptor_weight[receptors.index(receptor)]) 


for target in targets:
    links["source"].append(nodes.index(tf))
    links["target"].append(nodes.index(target))
    links["value"].append(target_weight[targets.index(target)])  


fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes
    ),
    link=dict(
        source=links["source"],
        target=links["target"],
        value=links["value"]
    ))])


fig.update_layout(title_text="Sankey Diagram: Receptors, TF, and Targets", font_size=10)
fig.write_html("sankey_weighted_Dlx1.html")
