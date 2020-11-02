
from .entity import Entity

# Bezier curves https://www.pythoninformer.com/python-libraries/pycairo/bezier-curves/

# Circle https://spencermortensen.com/articles/bezier-circle/
# Rounded Polygon https://www.toptal.com/c-plus-plus/rounded-corners-bezier-curves-qpainter

# Shape morphing https://css-tricks.com/many-tools-shape-morphing/

# Gradients https://www.pythoninformer.com/python-libraries/pycairo/gradients/

class Rectangle(Entity):
    def __init__(self, width=200, height=100, **kwargs):
        super().__init__(**kwargs)

    def update(self):
        pass

    def draw(self):
        pass

