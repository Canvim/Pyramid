"""The core cairo-based renderer"""

from cairo import ImageSurface, Context, FORMAT_ARGB32
import numpy as np
from numpy import pi, sin

from .renderer import Renderer
from ..writing.ffmpeg_writer import FFMPEGWriter
from ..animation.timeline import Timeline
from ..constants import DEFAULT_RENDER_CONFIG

class CairoRenderer(Renderer):
    def __init__(self, render_config=DEFAULT_RENDER_CONFIG, timeline=Timeline(), starting_frame_number=0):
        super().__init__(render_config, timeline, starting_frame_number)

        self.surface = ImageSurface(FORMAT_ARGB32, self.render_config.width, self.render_config.height)
        self.context = Context(self.surface)

    def draw_frame(self, frame_number):
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

    def get_current_frame(self):
        return self.get_frame(self.current_frame_number)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def render(self, writer):
        """
        Steps through the timeline and draws every frame to a cairo surface. That
        surface is then converted into pixel arrays which are then written to using
        the provided writer. Usually an ffmpeg process.
        """
        for frame in self:
            writer.write_frame(frame)
