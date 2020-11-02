
from functools import total_ordering
from pyramid.constants import DEFAULT_RENDER_CONFIG
from .entity import Entity
from ..animation.timeline import Timeline
from ..animation.animation import Animation
from ..writing.writer import Writer
from ..writing.ffmpeg_writer import FFMPEGWriter
from ..rendering.render_config import RenderConfig
from ..rendering.renderer import Renderer
from ..rendering.cairo_renderer import CairoRenderer

class Scene(Entity):

    def __init__(self, ):
        super().__init__()

        self.timeline = Timeline()
        self.construct()

    def construct(self):
        pass

    def render(self, render_config : RenderConfig=DEFAULT_RENDER_CONFIG, renderer : Renderer=None, writer : Writer=None):
        if not renderer:
            renderer = CairoRenderer(render_config=render_config, timeline=self.timeline)

        with renderer:
            if not writer:
                writer = FFMPEGWriter(render_config=render_config, total_frames=renderer.total_frames)

            with writer:
                renderer.render(writer)


    def update(self):
        return

    def draw(self):
        pass

    def add(self, *animations : Animation):
        self.timeline.add(*animations)
