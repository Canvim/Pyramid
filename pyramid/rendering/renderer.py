"""An abstract Renderer class which all rendererers must implement."""

from abc import ABC, abstractmethod
from contextlib import ContextDecorator

from ..constants import DEFAULT_RENDER_CONFIG
from ..animation.timeline import Timeline


class Renderer(ABC, ContextDecorator):
    def __init__(self, render_config=DEFAULT_RENDER_CONFIG, timeline=Timeline(), starting_frame_number=0):
        self.render_config = render_config
        self.current_frame_number = starting_frame_number
        self.timeline = timeline
        self.total_frames = round((self.timeline.duration/1000)*self.render_config.fps)

    def re_initiate(self, render_config=DEFAULT_RENDER_CONFIG, timeline=Timeline(), starting_frame_number=0):
        self.__init__(render_config=render_config, timeline=timeline, starting_frame_number=starting_frame_number)

    @abstractmethod
    def draw_frame(self, frame_number):
        """Draw's the requested frame

        Args:
            frame_number ([type]): [description]
        """
        raise NotImplementedError()

    @abstractmethod
    def get_frame(self, frame_number):
        """Returns a numpy array of pixels of the correct dimensions.

        Args:
            frame_number (int): index of the requested frame.

        Returns:
            np.ndarray: A numpy array of pixels.
        """
        raise NotImplementedError()

    def get_current_frame(self):
        """Since the renderer kan keep track of the current frame number,
        this kan be a shorthand for returning the frame of the current frame
        number.

        Returns:
            np.ndarray: A numpy array of pixels.
        """
        return self.get_frame(self.current_frame_number)

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, *args):
        raise NotImplementedError()

    def __iter__(self):
        """If renderer is used as an iterator, it yields frames

        Yields:
            np.ndarray: A numpy array of pixels.
        """
        while self.current_frame_number < self.total_frames:
            frame = self.get_current_frame()
            yield frame
            self.current_frame_number += 1
