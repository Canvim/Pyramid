"""The core cairo-based renderer"""

from cairo import ImageSurface, Context, FORMAT_ARGB32, MeshPattern
import numpy as np
from numpy import pi, sin
from svgpathtools import CubicBezier, QuadraticBezier, Line, Arc, Path

from .renderer import Renderer
from ..entities.entity import Entity
from ..entities.vector_entity import VectorEntity
from ..writing.ffmpeg_writer import FFMPEGWriter
from ..animation.timeline import Timeline
from ..constants import DEFAULT_RENDER_CONFIG

class CairoRenderer(Renderer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.surface = ImageSurface(FORMAT_ARGB32, self.render_config.width, self.render_config.height)
        self.context = Context(self.surface)

        self.context.translate(0, 0)
        self.context.scale(1, 1)

    def draw_frame(self, frame_number):

        time = frame_number * self.delta_time
        self.scene.seek(time)

        # TODO: Support drawing of non-vector entities, such as Scene
        # self.draw_entity(self.scene)
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
        else:
            raise NotImplementedError(f"Entity of type '{entity}' cannot currently be rendered.")

    def draw_vector_entity(self, vector_entity):
        for path in vector_entity.paths:
            self.draw_path(path)

        self.context.set_source_rgba(0.4, 0.5, 0.0, 1.0)

        self.context.set_fill_rule(1)
        # self.context.set_dash([40])
        self.context.set_line_width(1)
        self.context.stroke()
        self.context.fill()

    def draw_path(self, path: Path):
        for curve in path:
            self.draw_curve(curve)

    def draw_curve(self, curve):
        if isinstance(curve, CubicBezier):
            self.context.move_to(curve.start.real, curve.start.imag)
            self.context.curve_to(curve.control1.real, curve.control1.imag, curve.control2.real, curve.control2.imag, curve.end.real, curve.end.imag)
        elif isinstance(curve, Line):
            self.context.move_to(curve.start.real, curve.start.imag)
            self.context.line_to(curve.end.real, curve.end.imag)
        else:
            raise NotImplementedError(f"Rendering of curves of type '{curve.__class__.__name__}' has not been implemented yet.")

    def draw_frame_temporary(self, frame_number):
        t = frame_number/self.render_config.fps

        height = self.render_config.height
        width = self.render_config.width

        s = height/2
        x = width/2 + s * sin(t)
        y = height/2 - s * sin(t*2)
        r = height/(2.1 + 2*sin(t))
        ea = 2 * pi

        st = sin(t)

        self.context.arc(x, y, r, 0, ea)

        r = abs(st*st*st)
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
        pass
