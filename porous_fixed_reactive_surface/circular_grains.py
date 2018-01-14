import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

# Set seed
np.random.seed(1448)

# Domain size, unit of h
L = 1.0
Nh = 64.0
h = L/Nh

# 42 grains of 1.3h
N1, r1 = 42, 1.3*h
# 18 grains of 2.5h
N2, r2 = 18, 2.5*h
# 17 grains of 3.75h
N3, r3 = 17, 3.75*h
# Total = 77
Npor = N1 + N2 + N3

# Get the combined list in random order of radius
radii = np.array([r1]*N1 + [r2]*N2 + [r3]*N3)
np.random.shuffle(radii)

# function to check overlapping
def is_overlapped(_x, _y, _r, _cs):
    _a = np.array((_x, _y))
    for _c in _cs:
        _b = np.array((_c[0], _c[1]))
        if (np.linalg.norm(_a - _b) <= (_r + _c[2])):
            return True
    return False

# Generate each point and make sure no overlapping
cs = []
for i in range(Npor):
    found_new = False
    while (not found_new):
        # Random the coordinates
        x = np.random.rand()*L
        y = np.random.rand()*L
        if (not is_overlapped(x, y, radii[i], cs)):
            cs.append((x, y, radii[i]))
            found_new = True

# Plot and show
fix, ax = plt.subplots()
patches = []

patches = []
for c in cs:
    x1, y1, r = c[0], c[1], c[2]
    circle = Circle((x1, y1), r)
    patches.append(circle)

p = PatchCollection(patches, alpha=1.0)
colors = 100*np.random.rand((len(patches)))
p.set_array(np.array(colors))
ax.add_collection(p)
plt.axis('equal')
plt.show()
