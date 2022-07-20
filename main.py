
import newton_method
import polynomials
import plot_image

cached_derivated = {}



test_polynomial = {5 : 1, 2 : 1, 1 : -1, 0 : 1}
derivative = polynomials.derivate_polynomial(test_polynomial)

iterations = 50
roots_found = {} # Where each initial point "ended up". The key is the initial coordinate, and the value is the final coordinate after every iteration using newtons method.


graph_scale = ((-3, 1), (-2, 2)) # We are placing ourself in a complex graph
points_per_unit = 20 # Number of points to plot for each unit (between x:1 and x:2 for exemple)

x_length = graph_scale[0][1] - graph_scale[0][0]
y_height = graph_scale[1][1] - graph_scale[1][0]
nb_x_points = (x_length) * points_per_unit # Number of pixels on x axis
nb_y_points = (y_height) * points_per_unit # Number of pixels on y axis

for x in range(nb_x_points + 1):
    for y in range(nb_y_points + 1):
        cord_x = graph_scale[0][0] + (x / points_per_unit)
        cord_y = graph_scale[1][0] + (y / points_per_unit)
        #  Here x is the real part, and y is the imaginary part
        roots_found[(cord_x, cord_y)] = newton_method.apply_newtons_method_complex(test_polynomial, derivative, [cord_x, cord_y], iterations)
print(roots_found.values())

fractal = plot_image.Fractal(resolution=200, x_length=x_length, y_height=y_height, graph_scale=graph_scale)
fractal.plot_points(roots_found.values())
