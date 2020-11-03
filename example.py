"""Temporary Example. Will move to examples/ once module installation works"""

from pyramid import *


class CoolerScene(Scene):
    def construct(self):
        circle1 = Circle(radius=100, x=200, y=200)
        self.add_entity(circle1)

        self.add(Wait(duration=1000))
        self.add(Animation(circle1, x=100, y=100))


cooler_scene = CoolerScene()
cooler_scene.render(render_config=FULL_HD_RENDER_CONFIG, writer=FFMPEGWriter())
