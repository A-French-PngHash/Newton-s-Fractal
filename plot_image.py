import math
import os
import PIL
from PIL import Image, ImageDraw


class Fractal():
    def __init__(self, resolution: int, x_length: int, y_height: int, graph_scale: list):
        """

        :param resolution:
        :param x_lenght: Lenght of the graph on the x axis.
        :param y_height: Height of the graph on the y axis.
        :param graph_scale: A list of two tupple, which gives the dimension of the graph (ex : [(-1, 2), (-2, -2)])
        """
        self.resolution = resolution
        self.graph_scale = graph_scale

        x_max = x_length * resolution
        y_max = y_height * resolution

        self.img = Image.new('RGB', (x_max, y_max), color=1)
        self.img_draw = PIL.ImageDraw.ImageDraw(self.img)

    def plot_points(self, points: list, image_name="sqr.png"):
        """
        Plot the given points on an image. The point's position are as they were on the graph (for exemple (1; -1)).
        This function adapts the coordinates so that they can be plotted on an image (the coordinates of an image are
        at the top left.)
        :param points: List of (list of length two)
        :param image_name:
        :return:
        """

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

        for value in points:
            if (self.graph_scale[0][0] < value[0] < self.graph_scale[0][1] and self.graph_scale[1][0] < value[1] <
                    self.graph_scale[1][
                        1]):
                cord_x = math.floor((value[0] - self.graph_scale[0][0]) * self.resolution)
                cord_y = math.floor((-value[1] + self.graph_scale[1][1]) * self.resolution)

                self.img_draw.point((cord_x, cord_y), ((155, 155, 155)))

        output_path = os.path.abspath(f"Output/{image_name}")
        self.img.save(output_path)
