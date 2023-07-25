from time import perf_counter

class etawatch:
    def __init__(self, total_laps, max_laps_to_avg=None):
        if total_laps < 1:
            raise ValueError("Total laps must be greater than 0")
        if max_laps_to_avg is not None and max_laps_to_avg < 1:
            raise ValueError("Max laps to average must be greater than 0")
        self.times = []
        self.total_laps = total_laps
        self.max_laps_to_avg = max_laps_to_avg
        if self.max_laps_to_avg is None:
            self.max_laps_to_avg = total_laps
        self.i = 0
        self.last = perf_counter()

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.total_laps:
            raise StopIteration
        current = perf_counter()
        lap = current - self.last
        self.last = current
        self.times.append(lap)
        if len(self.times) > self.max_laps_to_avg:
            self.times.pop(0)
        self.i += 1
        average = sum(self.times) / len(self.times)
        eta = average * max(0, self.total_laps - self.i) / 60
        return eta, lap

    __call__ = __next__
