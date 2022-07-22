import math

import newton_method
import operations
import plot_image
import polynomials


def points_finding_roots_images(iterations : int, nb_points_line : int, nb_points_column : int):
    """
    Generates images of the points finding the roots of a polynomial
    :param iterations:
    :param points_per_unit: Number of points to plot for each unit (between x:1 and x:2 for exemple)
    :return:
    """
    test_polynomial = {5: 1, 2: 1, 1: -1, 0: 1}
    derivative = polynomials.derivate_polynomial(test_polynomial)
    
    graph_scale = ((-2, 2), (-2, 2))  # We are placing ourself in a complex graph

    x_length = math.floor(graph_scale[0][1] - graph_scale[0][0])
    y_height = math.floor(graph_scale[1][1] - graph_scale[1][0])

    initial_points = [(graph_scale[0][0] + (x / nb_points_line)*x_length, graph_scale[1][0] + (y / nb_points_column)*y_height) for x in
                      range(nb_points_line + 1) for y in range(nb_points_column + 1)]

    print(initial_points)
    points = initial_points.copy()

    for iteration in range(iterations):
        fractal = plot_image.PlotImage(nb_points_line=nb_points_line, nb_points_column=nb_points_column, x_length_unit=x_length, y_height_unit=y_height, graph_scale=graph_scale)
        fractal.plot_points(points, [0 for _ in points], str(iteration) + ".png")
        print(f"Image {iteration + 1} generated !")
        for (index, value) in enumerate(points):
            cord_x = value[0]
            cord_y = value[1]
            points[index] = newton_method.apply_newtons_method_complex(test_polynomial, derivative, [cord_x, cord_y], 1)


def points_final_location_closeness_to_root(iterations : int, nb_points_line, nb_points_column, graph_scale = ((-2, 2), (-2, 2)), file_name : str = None) -> (list, list):
    """
    How close each point is after applying the newton's algorithm.
    :param iterations:
    :param nb_points_line: The number of points there is on a line.
    :param nb_points_column: The number of points there is on a column.
    :return: The position for every point. The second list is the point they are the closest from.
    """
    test_polynomial = {5: 1, 2: 1, 1: -1, 0: 1}
    derivative = polynomials.derivate_polynomial(test_polynomial)
    roots = [(0, -1), (0, 1), (-1.32, 0), (0.66, -0.56), (0.66, 0.56)]
    print(graph_scale)
    x_length_unit = graph_scale[0][1] - graph_scale[0][0]
    y_height_unit = graph_scale[1][1] - graph_scale[1][0]

    initial_points = [
        (graph_scale[0][0] + (x / nb_points_line) * x_length_unit, graph_scale[1][0] + (y / nb_points_column) * y_height_unit) for
        x in
        range(nb_points_line + 1) for y in range(nb_points_column + 1)]

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
    fractal = plot_image.PlotImage(nb_points_line = nb_points_line, nb_points_column = nb_points_column, x_length_unit=x_length_unit, y_height_unit=y_height_unit, graph_scale=graph_scale)
    fractal.plot_points(initial_points, closest_root, image_name=file_name)

    return initial_points, closest_root

