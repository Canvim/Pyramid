
from pyramid import *


# This is what we have
# (temporary)

with Timeline() as timeline:
    timeline.add(Animation(duration=7*1000))

    my_render_config = RenderConfig(fps=60, width=720, height=480)

    with CairoRenderer(timeline=timeline, render_config=my_render_config) as renderer:
        with FFMPEGWriter(total_frames=renderer.total_frames, render_config=my_render_config) as writer:
            renderer.render(writer)


# This is what we want:

class CoolestScene(Scene):
    def construct(self, timeline):
        rectangle = Rectangle()
        timeline.add(Animation(rectangle))
        # or timeline.add_animation(rectangle, ...)

        # scene.render, renderer.render will then be called by the
        # package itself and configured by the cli / config file


# ... maybe even this, where Scene actually implements both Entity and Timeline:

class CoolestScene(Scene):
    def construct(self):
        rectangle = Rectangle()
        self.add(Animation(rectangle))