import numpy as np
import matplotlib.pyplot as plt
from aquarel import load_theme

theme = load_theme("ambivalent")
theme.apply()

fig, ax = plt.subplots(figsize=(8, 8))

N = 80000
vertices = np.array(((0, 0), (1, 0), (1, 1), (0, 1), (0, 0.5), (0.5, 0), (1, 0.5), (0.5, 1)))

points = np.zeros((2, N))
points[:, 0] = np.random.random(), np.random.random()

for i in range(1, N):
	points[:, i] = (points[:, i - 1] + 2*vertices[np.random.randint(0, 8)]) / 3

plt.scatter(points[0, 10:], points[1, 10:], s=0.5)

theme.apply_transforms()
plt.savefig("SierpinskiSquare.png", dpi=300)
