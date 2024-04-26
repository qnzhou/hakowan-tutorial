#!/usr/bin/env python

import lagrange

bunny_0 = lagrange.io.load_mesh("bunny_0.obj")
lagrange.compute_normal(bunny_0)
lagrange.io.save_mesh("bunny_0.obj", bunny_0)

def add_facet_normal(filename):
    cage = lagrange.io.load_mesh(filename)
    for id in cage.get_matching_attribute_ids(usage=lagrange.AttributeUsage.Normal):
        cage.delete_attribute(cage.get_attribute_name(id))
    lagrange.compute_facet_normal(cage)
    lagrange.io.save_mesh(filename, cage)

for i in range(1, 8):
    add_facet_normal(f"bunny_{i}.obj")
