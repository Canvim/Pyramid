

from abc import abstractmethod

from .entity import Entity
from ..constants import DEFAULT_RENDER_CONFIG
from ..animation.timeline import Timeline
from ..animation.animation import Animation
from ..writing.writer import Writer
from ..writing.ffmpeg_writer import FFMPEGWriter
from ..rendering.render_config import RenderConfig
from ..rendering.renderer import Renderer
from ..rendering.cairo_renderer import CairoRenderer

class Scene(Entity):

    def __init__(self):
        super().__init__()

        self.timeline = Timeline()
        self.entities_dictionary = {}

    @abstractmethod
    def construct(self):
        raise NotImplementedError()

    def render(self, render_config : RenderConfig=DEFAULT_RENDER_CONFIG, renderer : Renderer=CairoRenderer(), writer : Writer=FFMPEGWriter()):

        renderer.re_initiate(render_config=render_config, scene=self)
        writer.re_initiate(render_config=render_config, total_frames=renderer.total_frames)

        with renderer:
            with writer:
                for frame in renderer:
                    writer.write_frame(frame)

    def seek(self, time):
        self.timeline.seek(time)

    def update(self):
        self.timeline.step()
        self.draw()

    def add(self, *animations : Animation):
        self.timeline.add(*animations)

    def add_entity(self, entity):
        self.entities_dictionary[id(entity)] = entity
