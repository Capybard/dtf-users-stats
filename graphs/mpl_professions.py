import json

import matplotlib.pyplot as plt

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

profession_data = data["profession"]

sorted_data = sorted(profession_data.items(), key=lambda x: x[1], reverse=True)

professions = [item[0] for item in sorted_data]
counts = [item[1] for item in sorted_data]

fig, ax = plt.subplots(figsize=(12, 8))

base_colors = list(plt.cm.Set3.colors) + list(plt.cm.Pastel1.colors)

colors = [(r*0.8, g*0.8, b*0.8) for r, g, b in base_colors[:len(professions)]]

ax.barh(professions, counts, color=colors)

ax.invert_yaxis()

ax.set_title("Кем работают DTFеры?", fontsize=18)

ax.set_yticks(range(len(professions)))
ax.set_yticklabels(professions)

ax.yaxis.set_label_coords(1.05, 0.5)

ax.set_xlabel("Количество людей", fontsize=12)

ax.set_xticks(range(0, max(counts) + 1))
ax.grid(axis='x', alpha=0.3)

plt.subplots_adjust(left=0.25, right=0.85)

plt.show()