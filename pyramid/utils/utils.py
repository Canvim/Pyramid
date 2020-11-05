
import datetime

from progress.bar import IncrementalBar
from numpy import exp

# Implementation by the manim project


def sigmoid(x):
    return 1.0 / (1 + exp(-x))


class ProgressBar(IncrementalBar):
    suffix = "%(percent)d%% - [%(elapsed_td)s / %(estimated_total)s] eta: [%(eta_td)s]"

    @property
    def estimated_total(self):
        return "{}".format(datetime.timedelta(seconds=round(self.elapsed + self.eta)))
