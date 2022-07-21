import math
import os
import PIL
from PIL import Image, ImageDraw


class PlotImage():
    """
    An Image to plot points. An instance must be created for every image.
    """
    colors = [(231, 143, 49), (238, 47, 54), (143, 105, 226), (112, 145, 225), (73, 190, 223)]

    def __init__(self, resolution: int, x_length: int, y_height: int, graph_scale: tuple):
        """
        :param resolution:
        :param x_lenght: Length of the graph on the x axis.
        :param y_height: Height of the graph on the y axis.
        :param graph_scale: A tuple of two tuple, which gives the dimension of the graph (ex : [(-1, 2), (-2, -2)]) The first tuple is the x size, second is the y.
        """
        self.graph_scale = graph_scale
        self.resolution = resolution

        x_max = x_length * resolution
        y_max = y_height * resolution

        self.img = Image.new('RGB', (x_max, y_max), color=1)
        self.img_draw = PIL.ImageDraw.ImageDraw(self.img)

    def _draw_graph_axis(self, image: PIL.ImageDraw.ImageDraw):
        top_y_axis = self._coordinates_for_point_on_graph((0, self.graph_scale[1][1]))
        bot_y_axis = self._coordinates_for_point_on_graph((0, self.graph_scale[1][0]))

        left_x_axis = self._coordinates_for_point_on_graph((self.graph_scale[0][0], 0))
        right_x_axis = self._coordinates_for_point_on_graph((self.graph_scale[0][1], 0))

        image.line((top_y_axis[0], top_y_axis[1], bot_y_axis[0], bot_y_axis[1]), width=1)
        image.line((left_x_axis[0], left_x_axis[1], right_x_axis[0], right_x_axis[1]), width=1)

    def _coordinates_for_point_on_graph(self, point: tuple) -> tuple:
        """

        :param point:
        :return: Coordinates for the image
        """
        cord_x = math.floor((point[0] - self.graph_scale[0][0]) * self.resolution)
        cord_y = math.floor((-point[1] + self.graph_scale[1][1]) * self.resolution)
        return (cord_x, cord_y)

    def plot_points(self, points: list, color_type : list, image_name="sqr.png"):
        """
        Plot the given points on an image. The point's position are as they were on the graph (for exemple (1; -1)).
        This function adapts the coordinates so that they can be plotted on an image (the coordinates of an image are
        at the top left.)
        :param points: List of (list of length two) containing the coordinates for each point.
        :param color_type: Every point has its own color type, just numbers, starting from zero.
        :param image_name:
        :return:
        """
        self._draw_graph_axis(self.img_draw)

        """
        Method to get the position of a pixel in an image from a point in a graph.
        The image (0, 0) is at the top left.

        What matters to calculate the position is the number of y graduation above 0 and the number of x graduation below 0.

        x_pos = x + nb_x_grad_below_zero
        y_pos = -y + nb_y_grad_above_zero

        Exemple : graph where 2 above zero for y and 2 below zero for x.
        point -> (1; -1)
        x_pos = 1 + 2 = 3
        y_pos = -(-1) + 2 = 3
        (3;3) is the position of the pixel on the image starting from the top left corner.
        Then you multiply this position by the resolution of the image. And floor it for it to be an integer.
        """
        print(len(points))
        for (index, value) in enumerate(points):
            if (self.graph_scale[0][0] < value[0] < self.graph_scale[0][1] and self.graph_scale[1][
                0] < value[1] <
                    self.graph_scale[1][
                        1]):
                cord_x, cord_y = self._coordinates_for_point_on_graph(value)
                self.img_draw.point((cord_x, cord_y), self.colors[color_type[index]])

        output_path = os.path.abspath(f"Output/{image_name}")
        self.img.save(output_path)

