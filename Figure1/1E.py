import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('../Data/more_stats.csv', sep='\t') 

gene_names = data.iloc[:, 0]
p_values = data[['FDR_C', 'FDR_I', 'FDR_G', 'FDR']]
long_data = pd.melt(p_values, var_name='Statistic', value_name='P-value')

plt.figure(figsize=(10, 6))
sns.violinplot(x='Statistic', y='P-value', data=long_data, inner='quartile')
plt.show()
