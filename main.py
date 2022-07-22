import math

from numpy.polynomial import Polynomial
import multiprocessing as mp
import cool_stuff

nice_polys = [
    [
        {5: 1, 2: 1, 1: -1, 0: 1},
        ((0, -1), (0, 1), (-1.32, 0), (0.66, -0.56), (0.66, 0.56)),
        [[-2, 2], [-2, 2]]
    ],
     [
        {6 : 3, 5 : -2.4, 4 : -3.8, 3 : 6, 2 : 4, 1 : -1},
        ((0.1988585661, 0), (0, 0), (1.92866548, 0.7957212202), (1.92866548, -0.7957212202), (-0.8922958314, 0.1380430748), (-0.8922958314, -0.1380430748)),
        [[-2.616, 1.384], [-1.792, 2.208]]
     ]
]
"""
A list of polynomials to use to generate nice images. The first element of each subset is the polynomial itself, the 
second its roots and the third, the preferred range to observe it (graph scale)"""


def main_func():
    #cool_stuff.points_finding_roots_images(iterations=10, nb_points_column=1000, nb_points_line=1000,
                                           #polynomial=nice_polys[1][0], graph_scale=nice_polys[1][2])


    nb_points_line = 1000
    nb_points_column = 1000
    args = []
    polynomial = nice_polys[0][0]
    root = nice_polys[0][1]
    graph_scale = nice_polys[0][2]
    width = -graph_scale[0][0] + graph_scale[0][1]
    height = -graph_scale[1][0] + graph_scale[1][1]
    for i in range(20):
        gscale = [i.copy() for i in graph_scale]
        gscale[0][0] -= math.copysign(1, gscale[0][0]) * (width - width/2**i)/2 # (gscale[0][0] / math.sqrt(gscale[0][0]**2)) is the sign of gscale[0][0]
        gscale[0][1] -= math.copysign(1, gscale[0][1]) * (width - width/2**i)/2
        gscale[1][0] -= math.copysign(1, gscale[1][0]) * (height - height/2**i)/2
        gscale[1][1] -= math.copysign(1, gscale[1][1]) * (height - height/2**i)/2
        print(gscale)
        args.append((10, nb_points_line, nb_points_column, polynomial, root, gscale, f"fractal{i}.png"))

    with mp.Pool(8) as p:
        p.starmap(cool_stuff.points_final_location_closeness_to_root, args)


if __name__ == '__main__':
    main_func()
