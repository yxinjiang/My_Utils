import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
import seaborn as sns
sns.set(style="whitegrid")

df = pd.read_csv('summary_results_3.csv')
print(df.head())
df['Score'] = df['Score'].str.replace(r'%', r'.0').astype('float') / 100.0


g = sns.factorplot("Location",'Score','Configuration',data=df,kind='bar',col='KPI',legend=False)
ax1 = g.axes[0][0]
ax1.axhline(0.88,color='r',ls='-.')
trans = transforms.blended_transform_factory(ax1.get_yticklabels()[0].get_transform(), ax1.transData)
ax1.text(0,0.88, "{:.2f}".format(0.88), color="red", transform=trans,  ha="right", va="center")
for label in ax1.get_xticklabels():
    label.set_ha("right")
    label.set_rotation(45)
ax2 = g.axes[0][1]
ax2.axhline(0.48,color='r',ls='-.')
#trans = transforms.blended_transform_factory(ax2.get_yticklabels()[0].get_transform(), ax2.transData)
ax2.text(0,0.48, "{:.2f}".format(0.48), color="red",  ha="right", va="center")
for label in ax2.get_xticklabels():
    label.set_ha("right")
    label.set_rotation(45)

ax3 = g.axes[0][2]
ax3.axhline(0.49,color='r',ls='-.')
#trans = transforms.blended_transform_factory(ax3.get_yticklabels()[0].get_transform(), ax3.transData)
ax3.text(0,0.49, "{:.2f}".format(0.49), color="red",  ha="right", va="center")
for label in ax3.get_xticklabels():
    label.set_ha("right")
    label.set_rotation(45)

g.fig.subplots_adjust(top=0.8)
g.fig.suptitle('Summary of results for trained, validated, and tested on footage of CCTVs that have category 3 rainfall')
lines = Line2D([0], [0], color='r', linewidth=1, linestyle='-.')
lengend_data = g._legend_data
labels= ["2 - train on 4 CCTV's"]
labels.extend(list(lengend_data.keys()))
shapes = []
shapes.append(lines)
shapes.extend(list(lengend_data.values()))

plt.legend(shapes,labels)
plt.show()
