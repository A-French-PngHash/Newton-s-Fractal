import math

import newton_method
import operations
import plot_image
import polynomials


def points_finding_roots_images(iterations : int, points_per_unit = 50, resolution = 200):
    """
    Generates images of the points finding the roots of a polynomial
    :param iterations:
    :param points_per_unit: Number of points to plot for each unit (between x:1 and x:2 for exemple)
    :return:
    """
    test_polynomial = {5: 1, 2: 1, 1: -1, 0: 1}
    derivative = polynomials.derivate_polynomial(test_polynomial)

    roots_found = {}  # Where each initial point "ended up". The key is the initial coordinate, and the value is the final coordinate after every iteration using newtons method.

    graph_scale = ((-2, 2), (-2, 2))  # We are placing ourself in a complex graph

    x_length = graph_scale[0][1] - graph_scale[0][0]
    y_height = graph_scale[1][1] - graph_scale[1][0]
    nb_x_points = (x_length) * points_per_unit  # Number of pixels on x axis
    nb_y_points = (y_height) * points_per_unit  # Number of pixels on y axis

    initial_points = [(graph_scale[0][0] + (x / points_per_unit), graph_scale[1][0] + (y / points_per_unit)) for x in
                      range(nb_x_points + 1) for y in range(nb_y_points + 1)]

    points = initial_points.copy()

    for iteration in range(iterations):
        fractal = plot_image.PlotImage(resolution=resolution, x_length=x_length, y_height=y_height, graph_scale=graph_scale)
        fractal.plot_points(points, [0 for _ in points], str(iteration) + ".png")
        print(f"Image {iteration + 1} generated !")
        for (index, value) in enumerate(points):
            cord_x = value[0]
            cord_y = value[1]
            points[index] = newton_method.apply_newtons_method_complex(test_polynomial, derivative, [cord_x, cord_y], 1)


def points_final_location_closeness_to_root(iterations : int, points_per_unit = 50, resolution = 200, graph_scale = ((-2, 2), (-2, 2))) -> (list, list):
    """
    How close each point is after applying the newton's algorithm.
    :param iterations:
    :param points_per_unit: Number of points to plot for each unit (between x:1 and x:2 for exemple)
    :return: The position for every point. The second list is the point they are the closest from.
    """
    test_polynomial = {5: 1, 2: 1, 1: -1, 0: 1}
    derivative = polynomials.derivate_polynomial(test_polynomial)
    roots = [(0, -1), (0, 1), (-1.32, 0), (0.66, -0.56), (0.66, 0.56)]

    # roots_found = {}  # Where each initial point "ended up". The key is the initial coordinate, and the value is the final coordinate after every iteration using newtons method.

    x_length = math.floor(graph_scale[0][1] - graph_scale[0][0])
    y_height = math.floor(graph_scale[1][1] - graph_scale[1][0])
    nb_x_points = (x_length) * points_per_unit  # Number of pixels on x axis
    nb_y_points = (y_height) * points_per_unit  # Number of pixels on y axis

    initial_points = [(graph_scale[0][0] + (x / points_per_unit), graph_scale[1][0] + (y / points_per_unit)) for x in
                      range(nb_x_points + 1) for y in range(nb_y_points + 1)]

    closest_root = []

    for (index, value) in enumerate(initial_points):
        cord_x = value[0]
        cord_y = value[1]
        new_cord_x, new_cord_Y = newton_method.apply_newtons_method_complex(test_polynomial, derivative, [cord_x, cord_y], iterations=iterations)
        min_distance = -1
        root_index = 0
        for (rind, element) in enumerate(roots):
            ndist = operations.distance_between_points((new_cord_x, new_cord_Y), element)
            if ndist < min_distance or min_distance == -1:
                min_distance = ndist
                root_index = rind
        closest_root.append(root_index)
    fractal = plot_image.PlotImage(resolution=resolution, x_length=x_length, y_height=y_height, graph_scale=graph_scale)
    fractal.plot_points(initial_points, closest_root)

    return initial_points, closest_root

