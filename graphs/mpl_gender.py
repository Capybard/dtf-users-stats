import json

import matplotlib.pyplot as plt

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

gender_data = data["gender"]

labels_raw = list(gender_data.keys())
sizes = list(gender_data.values())

total = sum(sizes)

labels = [
    f"{label} ({size / total * 100:.1f}%)"
    for label, size in zip(labels_raw, sizes)
]

plt.figure(figsize=(8, 8))

color_map = {
    "Мужчины": "skyblue",
    "Женщины": "pink"
}

colors = [color_map[label] for label in labels_raw]

plt.pie(
    sizes,
    labels=labels,
    startangle=90,
    colors=colors
)

plt.title("Какого пола DTFеры?", fontsize=18)

plt.text(
    0, -1.4,
    f'Всего: {total} человек',
    ha='center',
    fontsize=12
)

plt.show()