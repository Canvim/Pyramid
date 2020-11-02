"""A dataclass used by the internal renderer"""


class RenderConfig:
    def __init__(self, fps=60, width=1920, height=1080, only_write_every=1):
        self.fps = fps
        self.width = width
        self.height = height
        self.only_write_every = only_write_every
