"""Some default animation shorthands"""

from .animation import Animation


class Wait(Animation):
    def __init__(self, duration=1000):
        super().__init__(duration=duration)
