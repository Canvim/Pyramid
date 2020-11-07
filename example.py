"""Temporary Example. Will move to examples/ once module installation works"""

import math
from pyramid import *


class CoolerScene(Scene):
    def construct(self):
        circle1 = Circle(radius=200, x=100, y=200)
        self.add_entity(circle1)

        text1 = Text(text="Hello, World! This is a longer sentence!", font_size=100, x=100, y=500)
        self.add_entity(text1)

        self.add(
            Animation(text1, font_size=200, duration=1600),
            Animation(text1, x=500, y=100, duration=2000)
        )

        self.add(Wait(1000))

        self.add(Animation(text1, x=100, y=900, duration=2000))
        self.add(Animation(text1, font_size=350, duration=1600))


class MorphScene(Scene):
    def construct(self):
        text1 = Text("This is text on the side!", x=400, y=400, font_size=200, rotation=0)
        self.add_entity(text1)

        dot = Circle(20, x=500, y=500)

        text2 = Text("I can be on this side too!", x=2000, y=400, font_size=200, rotation=math.pi)
        # self.add_entity(text)

        self.add(Wait(2000))
        self.add(Morph(text1, dot))
        self.add(Morph(text1, text2))
        self.add(Wait(2000))


scene_to_render = MorphScene() # CoolerScene()
scene_to_render.render(render_config=HD_RENDER_CONFIG, writer=FFMPEGWriter())
