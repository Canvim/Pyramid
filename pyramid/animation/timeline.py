"""An object that keeps track of all the animations within a scene"""


from .animation import Animation

class Timeline():
    def __init__(self, *animations):
        self.duration = 0
        self.total_frames = 0
        self.animations = []

        self.current_time = 0

        for animation in [*animations]:
            self.add_animation(animation)

    def add_animation(self, *animations : Animation):
        """Adds animations to the timeline"""

        for animation in animations:
            self.animations.append(animation)

        self.recalculate_total_duration()

    def seek(self, time):
        self.current_time = time

        for animation in self.animations:
            animation.interpolate(self.current_time)

    def recalculate_total_duration(self):
        self.duration = 0

        # TODO: Big task, but must take overlapping animations into consideration

        for animation in self.animations:
            if animation.duration >= self.duration:
                self.duration = animation.duration
