#!/usr/bin/env python

import hakowan as hkw

# Configuration setup
config = hkw.config()
config.z_up()
config.sensor.location = [2.5, -2.5, 0]

# Base layer
l0 = hkw.layer("data/powell_sabin.ply").transform(
    hkw.transform.Compute(component="comp_ids")
)
hkw.render(l0, config, filename="results/l0.png")

# Update marks
l1 = l0.mark("Point").channel(size=0.015)
l2 = l0.mark("Curve").channel(size=0.005)
l3 = l0.mark("Surface")

hkw.render(l1, config, filename="results/l1.png")
hkw.render(l2, config, filename="results/l2.png")
hkw.render(l3, config, filename="results/l3.png")

# Update material channels
l4 = l1.material(
    "Principled",
    hkw.texture.ScalarField(
        "vertex_label", colormap=["steelblue", "green", "yellow", "red"]
    ),
    roughness=0,
    metallic=0.3,
)
l5 = l2.material("Conductor", "Cr")
l6 = l3.material(
    "Principled",
    color=hkw.texture.ScalarField("comp_ids", colormap="set1", categories=True),
)

hkw.render(l4, config, filename="results/l4.png")
hkw.render(l5, config, filename="results/l5.png")
hkw.render(l6, config, filename="results/l6.png")

# Combine layers
l7 = l4 + l5 + l6
hkw.render(l7, config, filename="results/l7.png")

# Apply explode transform
l8 = l7.transform(hkw.transform.Explode("comp_ids", magnitude=0.5))
hkw.render(l8, config, filename="results/l8.png")
