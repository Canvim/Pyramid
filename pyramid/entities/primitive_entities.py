

from math import pi, sin

from .hacky_svg_base_entity import HackySvgBaseEntity

# Bezier curves https://www.pythoninformer.com/python-libraries/pycairo/bezier-curves/

# Circle https://spencermortensen.com/articles/bezier-circle/
# Rounded Polygon https://www.toptal.com/c-plus-plus/rounded-corners-bezier-curves-qpainter

# Shape morphing https://css-tricks.com/many-tools-shape-morphing/

# Gradients https://www.pythoninformer.com/python-libraries/pycairo/gradients/


class Arc(HackySvgBaseEntity):
    def __init__(self, start_angle=0, end_angle=pi, radius=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.radius = radius

        self.generate_paths()

    def draw_to_temporary_context(self):
        self.context.arc(0, 0, self.radius, self.start_angle, self.end_angle)
        self.context.fill()

class Text(HackySvgBaseEntity):
    def __init__(self, text="", font_size=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text
        self.font_size = font_size

        self.generate_paths()

    def draw_to_temporary_context(self):
        self.context.set_font_size(self.font_size)

        self.context.select_font_face("times")
        self.context.text_path(self.text)

        self.context.fill()

    def update(self):
        self.generate_paths()


class Circle(Arc):
    def __init__(self, radius, *args, **kwargs):
        super().__init__(start_angle=0, end_angle=2*pi, radius=radius, *args, **kwargs)
