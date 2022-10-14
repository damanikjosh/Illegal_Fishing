import numpy as np
from stl.mesh import Mesh
# plt.show()
# plt.pause(1)

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

# Generate surface
x, y = np.meshgrid(np.arange(100), np.arange(100), indexing='ij')
z = np.zeros_like(x)
z[:50, :] = -10

# Plot the generated surface
fig, ax = plt.subplots(1, subplot_kw={'projection': '3d'})
# surf = ax.plot_surface(x, y, z, lw=0, antialiased=False)
# plt.show()
# plt.pause(1)

# Flatten
output = np.zeros((x.size, 3))
output[:, 0] = x.flatten()
output[:, 1] = y.flatten()
output[:, 2] = z.flatten()

tri = Triangulation(output[:, 0], output[:, 1])
# ax.plot_trisurf(tri, output[:, 2], cmap=plt.cm.CMRmap, shade=True, linewidth=0.1)
# plt.show(block=True)

mesh = Mesh(np.zeros(tri.triangles.shape[0], dtype=Mesh.dtype))

for i, f in enumerate(tri.triangles):
    for j in range(3):
        mesh.vectors[i][j] = output[f[j]]

mesh.save('../stl/mesh.stl')