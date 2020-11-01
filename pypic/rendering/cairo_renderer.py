"""The core cairo-based renderer"""

from math import pi, sin

from cairo import ImageSurface, Context, FORMAT_ARGB32
import numpy as np

from pypic.rendering.ffmpeg_writer import FFMPEGWriter
from pypic.animation import Timeline

from pypic.constants import HD_RENDER_CONFIG


class CairoRenderer:
    def __init__(self, render_config=HD_RENDER_CONFIG, timeline=Timeline(), starting_frame_number=0):
        self.render_config = render_config
        self.current_frame_number = starting_frame_number
        self.timeline = timeline

        self.total_frames = round((self.timeline.duration/1000)*self.render_config.fps)

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
        self.context.set_source_rgba(abs(st*st*st), abs(st), 1.0 - abs(st), abs(st*st))
        self.context.fill()

    def get_frame(self, frame_number):
        self.draw_frame(frame_number)
        buf = self.surface.get_data()
        frame = np.ndarray(shape=(self.render_config.width, self.render_config.height), dtype=np.uint32, buffer=buf)

        return frame

    def get_current_frame(self):
        return self.get_frame(self.current_frame_number)

    def render(self):
        """
        Steps through the timeline and draws every frame to a cairo surface. That
        surface is then converted into pixel arrays which are then written to an
        ffmpeg process living inside the FFMPEGWriter.
        """
        with FFMPEGWriter(render_config=self.render_config, total_frames=self.total_frames) as ffmpeg_writer:
            while self.current_frame_number < self.total_frames:
                frame = self.get_current_frame()
                ffmpeg_writer.write_frame(frame)
                self.current_frame_number += 1