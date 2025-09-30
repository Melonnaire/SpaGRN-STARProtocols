import matplotlib.pyplot as plt


sizes = [2670, 23209]
n = sum(sizes)
sizes = [round(x/n,2) for x in sizes]
colors = ['#ABC8E5', '#D8A0C1']
explode = (0.1, 0)  
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, autopct='%1.1f%%', shadow=True, startangle=0, colors=colors)
plt.show()
