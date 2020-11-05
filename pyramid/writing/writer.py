"""An abstract Writer class which all writers must implement."""

from abc import ABC, abstractmethod
from contextlib import ContextDecorator

from ..constants import DEFAULT_RENDER_CONFIG
from ..utils.utils import ProgressBar


class Writer(ABC, ContextDecorator):
    def __init__(self, render_config=DEFAULT_RENDER_CONFIG, total_frames=0):
        self.total_frames = total_frames
        self.render_config = render_config
        self.progress_bar_message = "Writing"

    def re_initiate(self, render_config=DEFAULT_RENDER_CONFIG, total_frames=0):
        self.__init__(render_config=render_config, total_frames=total_frames)

    def initiate_progress_bar(self):
        self.progress_bar = ProgressBar(self.progress_bar_message, max=self.total_frames)

    @abstractmethod
    def write_frame(self, frame):
        """Writes the frame using whatever means the writer has.

        Args:
            frame (np.ndarray): A numpy array of pixels.

        """
        raise NotImplementedError()

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, *args):
        raise NotImplementedError()
