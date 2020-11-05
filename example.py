"""Temporary Example. Will move to examples/ once module installation works"""

from pyramid import *


class CoolerScene(Scene):
    def construct(self):
        circle1 = Circle(radius=100, x=100, y=200)
        self.add_entity(circle1)

        text1 = Text(text="Hello, World!", font_size=100, x=100, y=500)
        self.add_entity(text1)

        self.add(Animation(text1, font_size=200, duration=2000))
        self.add(Animation(text1, x=500, y=100, duration=2000))


cooler_scene = CoolerScene()
cooler_scene.render(render_config=FULL_HD_RENDER_CONFIG, writer=FFMPEGWriter())
