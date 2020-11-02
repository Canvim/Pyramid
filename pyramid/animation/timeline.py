"""An object that keeps track of all the animations within a scene"""

from contextlib import ContextDecorator

from .animation import Animation


class Timeline(ContextDecorator):
    def __init__(self, *animations):
        self.duration = 0
        self.total_frames = 0
        self.animations = []

        for animation in [*animations]:
            self.add(animation)

    def add(self, *animations : Animation):
        """Adds animations to the timeline"""

        for animation in animations:
            self.animations.append(animation)


        self.recalculate_total_duration()

    def recalculate_total_duration(self):
        self.duration = 0

        # TODO: Big task, but must take overlapping animations into consideration

        for animation in self.animations:
            self.duration += animation.duration

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.recalculate_total_duration()
        pass
