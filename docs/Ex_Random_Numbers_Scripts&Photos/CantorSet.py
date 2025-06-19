import numpy as np
import matplotlib.pyplot as plt
from aquarel import load_theme

theme = load_theme("ambivalent")
theme.apply()

fig, ax = plt.subplots(figsize=(8, 2))

N = 80000
vertices = np.array(((0, 0), (1, 0)))

points = np.zeros((2, N))
points[:, 0] = np.random.random(), 0

for i in range(1, N):
	points[:, i] = (points[:, i - 1] + 2*vertices[np.random.randint(0, 2)]) / 3

plt.scatter(points[0, 10:], np.random.random((N - 10)), s=0.2, marker=".", linewidths=0)

theme.apply_transforms()
plt.tight_layout()
plt.savefig("CantorSet.png", dpi=600)
