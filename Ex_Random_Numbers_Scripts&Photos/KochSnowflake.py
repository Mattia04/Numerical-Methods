import numpy as np
import matplotlib.pyplot as plt
from aquarel import load_theme

theme = load_theme("ambivalent")
theme.apply()

fig, ax = plt.subplots(figsize=(8, 8))

N = 40000
vertices = np.array(((1.0, 0.0), (0.5, 0.8660), (-0.5, 0.8660), (-1.0, 0.0),
                     (-0.5, -0.8660), (0.5, -0.8660)))

points = np.zeros((2, N))
points[:, 0] = np.random.random()-0.5, np.random.random()-0.5

for i in range(1, N):
	points[:, i] = (points[:, i - 1] + 2 * vertices[
		np.random.randint(0, 6)]) / 3

plt.scatter(points[0, 10:], points[1, 10:], s = 0.5)

theme.apply_transforms()
plt.savefig("KochSnowflake.png", dpi=300)
