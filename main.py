from solid import *
from solid.utils import *

zf = 0.01

cube_size = 6
hole_size = 5
hole_edge = cube_size / 2 - hole_size / 2

model = cube(cube_size)

model -= translate([hole_edge, -zf, hole_edge])(
    cube([hole_size, cube_size + zf * 2, hole_size])
)

model -= translate([-zf, hole_edge, hole_edge])(
    cube([cube_size + zf * 2, hole_size, hole_size])
)

model -= translate([hole_edge, hole_edge, -zf])(
    cube([hole_size, hole_size, cube_size + zf * 2])
)

model += translate([cube_size / 2, cube_size / 2, cube_size / 2])(
    sphere(cube_size / 2 + 0.25, segments = 100)
)


scad_render_to_file(model, 'model.scad')
