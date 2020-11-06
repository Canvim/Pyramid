"""A Hacky Svg Base Entity Class"""

from abc import abstractmethod
from os import path
import tempfile

import cairo
import svgpathtools

from .vector_entity import VectorEntity


class HackySvgBaseEntity(VectorEntity):
    """
    The base class for Entities that can draw themselves to a Cairo context
    to then be turned into pure svg to then be turned into paths
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context: cairo.Context = None

    def generate_paths(self):
        """
        This method creates a temporary cairo context on to which implementations
        can draw shapes to. The context's surface is then turned into an svg file
        which is read and interpreted into paths/points. These are then assigned
        as the paths/points of the under-lying Vector Entity.
        """

        with tempfile.TemporaryDirectory(prefix="pyramid") as temporary_directory:
            random_name = next(tempfile._get_candidate_names())
            temporary_file_name = path.join(temporary_directory, f"pyramid_{self.__class__.__name__}_{random_name}.svg")

            w, h = 1920, 1080
            with cairo.SVGSurface(temporary_file_name, w, h) as surface:
                self.context = cairo.Context(surface)
                # self.context.scale(2, 2)
                # self.context.translate(w/2, h/2)

                self.draw_to_temporary_context()

                surface.finish()

            # clean up and remove the temporary context
            del surface
            try:
                delattr(self, "context")
            except AttributeError:
                pass

            # svg2paths returns a list of two lists. The second one contains raw svg which is
            # not interesting, so we only save the first list of actual svgpathtools.Path objects
            svg_render = svgpathtools.svg2paths(temporary_file_name)

            temporary_points = []
            for line in svg_render[0][0]:
                if isinstance(line, svgpathtools.path.CubicBezier):
                    for coordinates in list(line):
                        temporary_points.append(coordinates)
                elif isinstance(line, svgpathtools.path.Line):
                    points = list(line)
                    temporary_points.append(points[0])
                    temporary_points.append(points[0])
                    temporary_points.append(points[1])
                    temporary_points.append(points[1])
                elif isinstance(line, svgpathtools.path.QuadraticBezier):
                    points = list(line)
                    temporary_points.append(points[0])
                    temporary_points.append(points[1])
                    temporary_points.append(points[1])
                    temporary_points.append(points[2])
                else: 
                    raise NotImplementedError(
                    f"Rendering of curves of type '{line.__class__.__name__}' has not been implemented yet.")

            self.points = temporary_points
            self.svg = svg_render[1]

    @abstractmethod
    def draw_to_temporary_context(self):
        """
        When this method is called, there is a temporary self.context present
        that any implementation of this class should draw to.
        """
        raise NotImplementedError()
