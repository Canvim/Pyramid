
from abc import abstractmethod
from os import path, mkdir

from cairo import ImageSurface, FORMAT_ARGB32
from numpy import swapaxes

from .writer import Writer

class ImageWriter(Writer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.images_path = path.join("images")

    def __enter__(self):
        self.make_directory()
        self.initiate_progress_bar()

    def make_directory(self):
        if not path.isdir(self.images_path):
            mkdir(self.images_path)

    def __exit__(self, *args):
        pass


class PNGWriter(ImageWriter):
    def write_frame(self, frame):
        if self.progress_bar.index % self.render_config.only_write_every == 0:
            file_name = f"{self.progress_bar.index}.png"

            self.progress_bar.message = f"Writing {file_name}"

            width, height = frame.shape
            surface = ImageSurface.create_for_data(frame, FORMAT_ARGB32, width, height)
            surface.write_to_png(path.join(self.images_path, file_name))

        self.progress_bar.next()


class JPEGWriter(ImageWriter):
    def write_frame(self, frame):
        return NotImplemented

        if self.progress_bar.index % self.render_config.only_write_every == 0:
            width, height = frame.shape
            surface = ImageSurface.create_for_data(frame, FORMAT_ARGB32, width, height)
        self.progress_bar.next()
