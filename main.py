import cool_stuff
import polynomials

cool_stuff.points_finding_roots_images(iterations=10, nb_points_column=500, nb_points_line=500)

test_polynomial = {5: 1, 4 : -0.5, 2: 1, 1: -1, 0: 1}
known_roots = [(0, -1), (0, 1), (-1.32, 0), (0.66, -0.56), (0.66, 0.56)]
derivative = polynomials.derivate_polynomial(test_polynomial)

graph_scale = [[-1, 1], [-1, 1]]
points_per_unit = 50

for i in range(10):
    #cool_stuff.points_final_location_closeness_to_root(iterations=10, nb_points_line=1600, nb_points_column=1600, graph_scale=graph_scale, file_name=f"fractal{i}.png")
    graph_scale[0][0] /= 2
    graph_scale[0][1] /= 2
    graph_scale[1][0] /= 2
    graph_scale[1][1] /= 2
