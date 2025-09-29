import matplotlib.pyplot as plt
import numpy as np

gene_numbers = [1000, 5000, 10000, 15000, 20000, 23472]
user_time = [1, 1, 1, 1, 18, 47]
max_memory = [290, 376, 294, 8436, 33242, 77170]
x_indices = np.arange(len(gene_numbers))

fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()
ax3 = ax1.twinx()

ax3.set_zorder(1)
ax1.set_zorder(2)
ax2.set_zorder(3)

bar_heights = gene_numbers
ax3.bar(x_indices, bar_heights, color='#b2dfdb', width=0.6, alpha=0.8)
ax3.set_ylim(0, max(gene_numbers) * 1.15)
ax3.yaxis.set_visible(False)
for i, height in enumerate(gene_numbers):
    label_text = f'{height:,}'
    ax3.annotate(label_text, (x_indices[i], height), textcoords="offset points", 
                 xytext=(0, 5), ha='center', color='black')

color_time_line = 'indianred' 
ax1.set_ylabel('User Time (min)', color='black', fontsize=12) 
line1 = ax1.plot(x_indices, user_time, color=color_time_line, marker='*', linestyle='-', label='Time')
ax1.patch.set_visible(False) 
ax1.set_ylim(0, 60)

color_memory_line = 'steelblue' 
ax2.set_ylabel('Maximum Memory (MB)', color='black', fontsize=12) 
line2 = ax2.plot(x_indices, max_memory, color=color_memory_line, marker='o', linestyle='--', label='Memory')
ax2.patch.set_visible(False) 
ax2.set_ylim(0, 81920)

ax1.set_title('', fontsize=16, color='black')
ax1.set_xlabel('Gene number', fontsize=12, color='black')
ax1.set_xticks([])
ax1.set_xticklabels([])
ax1.grid(False)
ax2.grid(False)
ax3.grid(False)
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=False, fontsize=10, labelcolor='black')
fig.tight_layout()

plt.savefig('gene.pdf', bbox_inches='tight')
plt.show()
