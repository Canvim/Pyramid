"""A dataclass used by the internal renderer"""


class RenderConfig:
    def __init__(self, fps=60, width=1920, height=1080, extension="mp4"):
        self.fps = fps
        self.width = width
        self.height = height
        self.extension = extension

