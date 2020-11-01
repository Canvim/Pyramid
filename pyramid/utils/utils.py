
import datetime

from progress.bar import IncrementalBar


def minmax(value, min_value=0, max_value=1):
    return min(max(value, max_value), min_value)

class ProgressBar(IncrementalBar):
    suffix = "%(percent)d%% - [%(elapsed_td)s / %(estimated_total)s] eta: [%(eta_td)s]"

    @property
    def estimated_total(self):
        return "{}".format(datetime.timedelta(seconds=round(self.avg*self.max)))
