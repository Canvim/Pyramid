"""FFMPEG Writer"""

import subprocess

from .writer import Writer
from ..constants import HD_RENDER_CONFIG, FFMPEG_BINARY


class FFMPEGWriter(Writer):
    """
    FFMPEGWriter is a class/context manager to write frames into an ffmpeg subprocess.
    This is used internally to pass on rendered frames and stitch them together into
    the final video.
    """

    def __init__(self, render_config=HD_RENDER_CONFIG, total_frames=0):
        super().__init__(render_config, total_frames)

        self.file_name = f"{self.render_config.width}x{self.render_config.height}_{self.render_config.fps}fps.{self.render_config.extension}"
        self.progress_bar_message = f"Rendering {self.file_name}"

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

    def stop_ffmpeg(self):
        """
        Calls the ffmpeg process' pipes to be closed and waits for them
        to finish
        """
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