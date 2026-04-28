import json
import numpy as np

import matplotlib.pyplot as plt

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fear_data = data["fear"]

sorted_data = sorted(fear_data.items(), key=lambda x: x[1], reverse=True)

labels = [item[0] for item in sorted_data]
counts = [item[1] for item in sorted_data]

plt.figure(figsize=(14, 6))

colors = plt.cm.Reds_r(np.linspace(0.3, 0.9, len(labels)))

plt.bar(labels, counts, color=colors)

plt.title("Чего боятся DTFеры?", fontsize=18)
plt.ylabel("Количество людей", fontsize=12)

plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(range(0, max(counts) + 1))
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()