"""An object that keeps track of all the animations within a scene"""

from operator import attrgetter

from .animation import Animation


class Timeline():
    def __init__(self, *animations):
        self.duration = 0
        self.total_frames = 0
        self.animations = []

        self.current_time = 0
        self._add_time = 0

        for animation in [*animations]:
            self.add_animation(animation)

    def add_animation(self, *animations: Animation):
        """Adds animations to the timeline"""

        longest_duration = -1

        for animation in animations:
            if animation.duration >= longest_duration:
                longest_duration = animation.duration

            animation.start_time = self._add_time
            self.animations.append(animation)

        self._add_time += longest_duration

        self.recalculate_total_duration()

    def seek(self, time):
        self.current_time = time

        for animation in self.animations:
            animation.interpolate(self.current_time)

    def recalculate_total_duration(self):
        self.duration = 0

        # TODO: Big task, but must take overlapping animations into consideration

        self.animations.sort(key=attrgetter("start_time"))
        last_animation = self.animations[-1:][0]
        self.duration = last_animation.start_time + last_animation.duration
