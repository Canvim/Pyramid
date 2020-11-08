"""The core cairo-based renderer"""

from cairo import ImageSurface, Context, FORMAT_ARGB32
import numpy as np
from numpy import pi, sin
from svgpathtools import CubicBezier, QuadraticBezier, Line, Arc, Path

from .renderer import Renderer
from ..entities.entity import Entity
from ..entities.vector_entity import VectorEntity


class CairoRenderer(Renderer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.surface = ImageSurface(FORMAT_ARGB32, self.render_config.width, self.render_config.height)
        self.context = Context(self.surface)

        self.context.translate(0, 0)
        self.context.scale(0.4, 0.4)

    def draw_frame(self, frame_number):
        time = frame_number * self.delta_time
        self.scene.seek(time)

        # TODO: Support drawing of non-vector entities, such as Scene
        self.draw_entity(self.scene)
        for entity in self.scene.entities_dictionary.values():
            entity.update()
            self.context.save()
            self.context.translate(entity.x, entity.y)
            self.context.scale(entity.scale, entity.scale)
            self.context.rotate(entity.rotation)
            self.draw_entity(entity)
            self.context.restore()

    def draw_entity(self, entity):
        if issubclass(type(entity), VectorEntity):
            self.draw_vector_entity(entity)
        elif issubclass(type(entity), Entity): # Temporary just to clear screen
            self.context.set_source_rgb(0.0, 0.0, 0.0)
            self.context.rectangle(0, 0, self.render_config.width*10, self.render_config.height*10)
            self.context.fill()
        else:
            raise NotImplementedError(f"Entity of type '{entity.__class__.__name__}' cannot currently be rendered.")

    def draw_vector_entity(self, vector_entity):
        self.draw_curves(vector_entity.points)

        self.context.set_source_rgba(100/255, 100/255, 124/255, 1.0)
        # self.context.set_dash([40])
        self.context.set_line_width(1)
        self.context.stroke_preserve()
        self.context.fill()

    def draw_curves(self, points):
        previous_end = complex()

        for i in range(len(points)//4):
            index = i*4
            curve = points[index:index+4]
            start, control1, control2, end = curve

            if start != previous_end:
                self.context.move_to(start.real, start.imag)
            self.context.curve_to(control1.real, control1.imag, control2.real, control2.imag, end.real, end.imag)
            previous_end = end



    def draw_frame_temporary(self, frame_number):
        """This was an old drawing-test generating some cool blue-white balls"""
        t = frame_number / self.render_config.fps

        height = self.render_config.height
        width = self.render_config.width

        s = height / 2
        x = width / 2 + s * sin(t)
        y = height / 2 - s * sin(t * 2)
        r = height / (2.1 + 2 * sin(t))
        ea = 2 * pi

        st = sin(t)

        self.context.arc(x, y, r, 0, ea)

        r = abs(st * st * st)
        g = abs(st) - 0.1
        b = abs(st)
        a = 1

        self.context.set_source_rgba(r, g, b, a)
        self.context.fill()

    def get_frame(self, frame_number):
        self.draw_frame(frame_number)
        buf = self.surface.get_data()
        frame = np.ndarray(shape=(self.render_config.width, self.render_config.height), dtype=np.uint32, buffer=buf)

        return frame

    def __enter__(self):
        return self

    def __exit__(self, *args):
        del self.context
        del self.surface
