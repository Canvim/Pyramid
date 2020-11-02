
from pyramid import *

# with Timeline() as timeline:
#     timeline.add(Animation(duration=14*1000))

#     with CairoRenderer(timeline=timeline) as renderer:
#         with FFMPEGWriter(total_frames=renderer.total_frames) as writer:
#             renderer.render(writer)

class CoolerScene(Scene):
    def construct(self):
        rectangle = Rectangle()
        self.add(Animation(rectangle, duration=7*1000))

cooler_scene = CoolerScene()
cooler_scene.render()