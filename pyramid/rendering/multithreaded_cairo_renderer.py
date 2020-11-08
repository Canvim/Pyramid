
import queue
from concurrent.futures import ThreadPoolExecutor

import numpy as np

from .cairo_renderer import CairoRenderer

class MultithreadedCairoRenderer(CairoRenderer):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.rendered_frames = []

   def __enter__(self):
      self.render_all_frames()

   def render_all_frames(self):
      self.rendered_frames = [None] * self.total_frames

      with ThreadPoolExecutor(max_workers=8) as executor:
         executor.map(self.worker, range(self.total_frames))

   def worker(self, frame_number):
      self.draw_frame(frame_number)
      buf = self.surface.get_data()
      frame = np.ndarray(shape=(self.render_config.width, self.render_config.height), dtype=np.uint32, buffer=buf)

      self.rendered_frames[frame_number] = frame
      print(f"Done with frame #{frame_number}")

   def get_frame(self, frame_number):
      return self.rendered_frames[frame_number-1]

