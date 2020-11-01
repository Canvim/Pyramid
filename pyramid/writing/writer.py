"""An abstract Writer class which all writers must implement."""

from abc import ABC, abstractmethod
from contextlib import ContextDecorator

from ..constants import HD_RENDER_CONFIG
from ..utils.utils import ProgressBar


class Writer(ABC, ContextDecorator):
    def __init__(self, render_config=HD_RENDER_CONFIG, total_frames=0):
        self.total_frames = total_frames
        self.render_config = render_config
        self.progress_bar_message = "Writing"

    def initiate_progress_bar(self):
        self.progress_bar = ProgressBar(self.progress_bar_message, max=self.total_frames)

    @abstractmethod
    def write_frame(self, frame):
        """Writes the frame using whatever means the writer has.

        Args:
            frame (np.ndarray): A numpy array of pixels.

        """
        return NotImplemented

    @abstractmethod
    def __enter__(self):
        return NotImplemented

    @abstractmethod
    def __exit__(self, *args):
        return NotImplemented