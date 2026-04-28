import json

import matplotlib.pyplot as plt

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

emotes_data = data["emotes"]

sorted_data = sorted(emotes_data.items(), key=lambda x: x[1], reverse=True)

emotes = [item[0] for item in sorted_data]
counts = [item[1] for item in sorted_data]

plt.figure(figsize=(14, 6))

base_colors = list(plt.cm.Set3.colors) + list(plt.cm.Pastel1.colors)
colors = [(r*0.8, g*0.8, b*0.8) for r, g, b in base_colors[:len(emotes)]]

plt.bar(emotes, counts, color=colors)

plt.title("Какие эмоции DTFеры испытывают чаще всего?", fontsize=18)
plt.ylabel("Количество людей", fontsize=12)

plt.xticks(rotation=45, ha='right', fontsize=9)

plt.yticks(range(0, max(counts) + 1))
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()

plt.show()