from math import pi, sin
from dataclasses import dataclass
from contextlib import ContextDecorator
import subprocess
import datetime

from cairo import ImageSurface, Context, FORMAT_ARGB32
import numpy as np
from progress.bar import IncrementalBar


class ProgressBar(IncrementalBar):
    suffix = "%(percent)d%% - [%(elapsed_td)s / %(estimated_total)s] eta: [%(eta_td)s]"

    @property
    def estimated_total(self):
        return "{}".format(datetime.timedelta(seconds=round(self.avg*self.max)))


@dataclass
class RenderConfig:
    fps: int = 60
    width: int = 1920
    height: int = 1080
    extension: str = "mp4"


HD_RENDER_CONFIG = RenderConfig(
    fps=120,
    width=1920,
    height=1080,
    extension="mp4"
)

FFMPEG_BINARY = "ffmpeg"


class FFMPEGWriter(ContextDecorator):
    def __init__(self, render_config=HD_RENDER_CONFIG, total_frames=0):
        self.total_frames = total_frames
        self.render_config = render_config

        self.file_name = f"{self.render_config.width}x{self.render_config.height}_{self.render_config.fps}fps.{self.render_config.extension}"

    def start_ffmpeg(self):
        """
        Starts ffmpeg in a subprocess with a setup that allows for
        frames to be piped to it.
        """
        command = [
            FFMPEG_BINARY, "-y",
            "-f", "rawvideo",
            "-s", f"{self.render_config.width}x{self.render_config.height}",
            "-pix_fmt", "rgba",
            "-r", str(self.render_config.fps),
            "-i", "-",
            "-an",
            "-loglevel", "error",
            "-vcodec", "libx264",
            "-pix_fmt", "yuv420p",
            self.file_name
        ]

        self.ffmpeg_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def initiate_progress_bar(self):
        self.progress_bar = ProgressBar(f"Rendering {self.file_name}", max=self.total_frames)

    def stop_ffmpeg(self):
        self.ffmpeg_process.stdin.close()
        self.ffmpeg_process.wait()

    def write_frame(self, frame):
        """ Pipes the frame to the ffmpeg subprocess' stdin

        Args:
            frame (np.ndarray): numpy array of pixels
        """

        self.ffmpeg_process.stdin.write(frame)
        self.progress_bar.next()

    def __enter__(self):
        self.start_ffmpeg()
        self.initiate_progress_bar()
        return self

    def __exit__(self, *args):
        self.stop_ffmpeg()
        pass


class Timeline:
    def __init__(self, duration=0):
        self.duration = duration

    def add(self):
        pass


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


def main():
    my_render_config = RenderConfig()
    duration = 7 * 1000

    timeline = Timeline(duration=duration)

    renderer = CairoRenderer(my_render_config, timeline)
    renderer.render()


if __name__ == "__main__":
    main()
