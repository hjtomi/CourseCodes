import pandas as pd
from matplotlib import pyplot as plt
import random


def random_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


df = pd.read_excel('Beérkező áruk-2022.szeptember.xls')
# Csak azokat tartjuk meg amelyeknek osszesen tobb mint 0 volt
df = df[df['osszesen'] > 0]

plt.xticks(rotation=45)

nevek = []
for nev, osszesen in zip(df['nev'], df['osszesen']):
    i = 10
    while nev[:i] in nevek:
        i += 1

    plt.bar(nev[:i], osszesen, color=random_color(), width=0.8)
    nevek.append(nev[:i])

plt.ylim([0, 500])
plt.grid()
plt.ylabel("Osszesen")
plt.xticks(fontsize=7)
plt.tight_layout()

plt.show()
