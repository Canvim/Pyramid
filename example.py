
from pyramid import *

# with Timeline() as timeline:
#     timeline.add(Animation(duration=14*1000))

#     with CairoRenderer(timeline=timeline) as renderer:
#         with FFMPEGWriter(total_frames=renderer.total_frames) as writer:
#             renderer.render(writer)

class CoolerScene(Scene):
    def construct(self):
        self.add(Wait(duration=10*1000))

cooler_scene = CoolerScene()
# cooler_scene.render(writer=FFMPEGWriter())
# cooler_scene.render(render_config=UHD_RENDER_CONFIG)

my_render_config = TOASTER_RENDER_CONFIG

cooler_scene.render(render_config=my_render_config, writer=FFMPEGWriter())