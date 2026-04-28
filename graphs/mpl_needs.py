import json

import matplotlib.pyplot as plt
import numpy as np

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

needs_data = data["needs"]

sorted_data = sorted(needs_data.items(), key=lambda x: x[1], reverse=True)[:15]

labels = [item[0] for item in sorted_data]
counts = [item[1] for item in sorted_data]

fig, ax = plt.subplots(figsize=(10, 7))

colors = plt.cm.Greens_r(np.linspace(0.3, 0.9, len(labels)))

bars = ax.barh(labels, counts, color=colors, height=0.7)

ax.invert_yaxis()

ax.set_title("Топ-15 потребностей DTFеров", fontsize=18)
ax.set_xlabel("Количество людей", fontsize=12)

ax.set_xticks(range(0, max(counts) + 2, 2))
ax.tick_params(axis='x', labelsize=11)
ax.tick_params(axis='y', labelsize=10)

ax.grid(axis='x', alpha=0.3)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.2,
        bar.get_y() + bar.get_height() / 2,
        str(int(width)),
        va='center',
        fontsize=10
    )

plt.subplots_adjust(left=0.2)
plt.show()