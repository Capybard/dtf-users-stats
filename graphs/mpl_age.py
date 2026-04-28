import json

import matplotlib.pyplot as plt

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

age_data = data["age"]

ages = []
for age, count in age_data.items():
    ages.extend([int(age)] * count)

mean_age = sum(ages) / len(ages)

plt.figure(figsize=(11, 6))

bins = list(range(15, 45, 5))

counts, bin_edges, patches = plt.hist(ages, bins=bins)

for i, patch in enumerate(patches):
    intensity = 1 - (0.6 * (i / len(patches)))
    patch.set_facecolor((0, intensity, 0))

plt.xticks(bins)

plt.title("Возраст DTFеров (по группам)", fontsize=18)
plt.xlabel("Возрастные группы", fontsize=12)
plt.ylabel("Количество людей", fontsize=12)

plt.grid(axis='y', alpha=0.3)

plt.text(
    0.98, 0.96,
    f'Средний возраст: {int(mean_age)}',
    transform=plt.gca().transAxes,
    ha='right',
    va='top',
    bbox=dict(facecolor='white', alpha=0.8)
)

plt.show()