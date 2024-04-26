#!/usr/bin/env python

import numpy as np
import hakowan as hkw
import lagrange

np.random.seed(0)

point_cloud = np.random.random((100, 3))
orig_sphere = np.arange(100)
radius = np.random.random(100) / 10

mesh = lagrange.SurfaceMesh()
mesh.add_vertices(point_cloud)
mesh.create_attribute("index", initial_values=orig_sphere)
mesh.create_attribute("radius", initial_values=radius)

lagrange.io.save_mesh("data/point_cloud.ply", mesh)
