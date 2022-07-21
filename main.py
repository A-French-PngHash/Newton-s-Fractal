import cool_stuff
import polynomials

#cool_stuff.points_finding_roots_images(iterations=30, points_per_unit=100, resolution=200)

test_polynomial = {5: 1, 4 : -0.5, 2: 1, 1: -1, 0: 1}
known_roots = [(0, -1), (0, 1), (-1.32, 0), (0.66, -0.56), (0.66, 0.56)]
derivative = polynomials.derivate_polynomial(test_polynomial)

graph_scale = [[-2, 2], [-2, 2]]
points_per_unit = 50
while True:
    cool_stuff.points_final_location_closeness_to_root(iterations=10, points_per_unit=500, resolution=400, graph_scale=graph_scale)
    input("Press enter to zoom in ")
    graph_scale[0][0] *= 0.9
    graph_scale[0][1] *= 0.9
    graph_scale[1][0] *= 0.9
    graph_scale[1][1] *= 0.9
    points_per_unit *= 1.23456
