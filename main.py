import threading
from threading import Thread
import multiprocessing as mp
import cool_stuff
import polynomials
def main_func():
    #cool_stuff.points_finding_roots_images(iterations=10, nb_points_column=1000, nb_points_line=1000)

    graph_scale = [[-10, 10], [-10, 10]]
    #cool_stuff.points_final_location_closeness_to_root(iterations=10, nb_points_line=1600, nb_points_column=1600,
                                                       #graph_scale=graph_scale, file_name=f"fractal{i}.png")
    nb_points_line=500
    nb_points_column=500
    graph_scale=graph_scale
    args = []
    for i in range(20):
        gscale = graph_scale.copy()
        gscale[0][0] /= 2 ** i
        gscale[0][1] /= 2 ** i
        gscale[1][0] /= 2 ** i
        gscale[1][1] /= 2 ** i
        print(gscale)
        args.append((10, nb_points_line, nb_points_column, gscale, f"fractal{i}.png"))

    with mp.Pool(8) as p:
        p.starmap(cool_stuff.points_final_location_closeness_to_root, args)


if __name__ == '__main__':
    main_func()