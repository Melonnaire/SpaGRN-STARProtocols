import plotly.graph_objects as go


receptors = ['Cntnap2', 'Erbb4', 'Nrxn3']
targets =  ["Elavl2","Vstm2a","Gad1","Arl4c","Sema3c","Adarb2","Mtss1","Cnr1","Gad2","Synpr","Reln","Sst"]
tf = 'Dlx1'

nodes = receptors + [tf] + targets

links = {
    "source": [],
    "target": [],
    "value": []
}

for receptor in receptors:
    links["source"].append(nodes.index(receptor))
    links["target"].append(nodes.index(tf))
    links["value"].append(4) 


for target in targets:
    links["source"].append(nodes.index(tf))
    links["target"].append(nodes.index(target))
    links["value"].append(1)  


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
fig.write_html("sankey_Dlx1.html")
