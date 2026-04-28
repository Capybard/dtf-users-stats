import json

import matplotlib.pyplot as plt

with open('data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

country_data = data["country"]

sorted_data = sorted(country_data.items(), key=lambda x: x[1], reverse=True)

countries = [item[0] for item in sorted_data]
counts = [item[1] for item in sorted_data]

plt.figure(figsize=(11, 6))

colors = [
    "#8ecae6",
    "#90be6d",
    "#f9c74f",
    "#f4a261",
    "#cdb4db",
    "#bde0fe"
]

plt.barh(countries, counts, color=colors[:len(countries)])

plt.gca().invert_yaxis()

plt.title("Из каких стран DTFеры?", fontsize=18)
plt.xlabel("Количество людей", fontsize=12)

plt.xticks(range(0, max(counts) + 1))
plt.grid(axis='x', alpha=0.3)

plt.show()