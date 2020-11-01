"""An abstract Renderer class which all rendererers must implement."""

from abc import ABC, abstractmethod
from contextlib import ContextDecorator

from ..constants import HD_RENDER_CONFIG
from ..animation.timeline import Timeline


class Renderer(ABC, ContextDecorator):
    def __init__(self, render_config=HD_RENDER_CONFIG, timeline=Timeline(), starting_frame_number=0):
        self.render_config = render_config
        self.current_frame_number = starting_frame_number
        self.timeline = timeline

        self.total_frames = round((self.timeline.duration/1000)*self.render_config.fps)

    @abstractmethod
    def draw_frame(self, frame_number):
        """Draw's the requested frame

        Args:
            frame_number ([type]): [description]
        """
        return NotImplemented

    @abstractmethod
    def get_frame(self, frame_number):
        """Returns a numpy array of pixels of the correct dimensions.

        Args:
            frame_number (int): index of the requested frame.

        Returns:
            np.ndarray: A numpy array of pixels.
        """
        return NotImplemented

    def get_current_frame(self):
        """Since the renderer kan keep track of the current frame number,
        this kan be a shorthand for returning the frame of the current frame
        number.

        Returns:
            np.ndarray: A numpy array of pixels.
        """
        return self.get_frame(self.current_frame_number)

    @abstractmethod
    def render(self):
        """
        Steps through the timeline and draws every frame.
        Should also write these frames to something in some way. See CairoRenderer
        for an example.
        """
        return NotImplemented

    @abstractmethod
    def __enter__(self):
        return NotImplemented

    @abstractmethod
    def __exit__(self, *args):
        return NotImplemented

    def __iter__(self):
        """If renderer is used as an iterator, it yields frames

        Yields:
            np.ndarray: A numpy array of pixels.
        """
        while self.current_frame_number < self.total_frames:
            frame = self.get_current_frame()
            yield frame
            self.current_frame_number += 1
