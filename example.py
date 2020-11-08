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
        text1 = Text("I used to be a dot!", x=400, y=400, font_size=200)
        text2 = Text("Testing to morph into different text", x=400, y=400, font_size=200)
        dot = Circle(200, x=500, y=500)
        dot2 = Circle(200, x=500, y=500)

        self.add_entity(dot)

        self.add(Wait(1000))
        self.add(Morph(dot, text1, duration=900), Animation(dot, y=900, rotation=-math.pi/4))
        self.add(Wait(500))
        self.add(Animation(dot, scale=3))
        self.add(Wait(500))
        self.add(Morph(dot, text2, duration=900), Animation(dot, y=200, rotation=math.pi/4))
        self.add(Wait(500))
        self.add(Morph(dot, dot2, duration=900))
        self.add(Wait(1000))


class SVGScene(Scene):
    def construct(self):
        svg_koala = SVG("assets/koala.svg", scale=2)
        text = Text("I like PyPen!", font_size=200, x=400, y=500)

        self.add_entity(svg_koala)

        self.add(Wait(3000))
        self.add(Morph(svg_koala, text))
        self.add(Wait(3000))

scene_to_render = SVGScene() # CoolerScene()
scene_to_render.render(render_config=HD_RENDER_CONFIG, writer=FFMPEGWriter())
