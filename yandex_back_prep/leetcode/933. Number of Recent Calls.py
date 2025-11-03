class RecentCounter:
    def __init__(self):
        self.track = []

    def ping(self, t: int) -> int:
        self.track.append(t)

        while t - self.track[0] > 3000:
            self.track.pop(0)

        return len(self.track)
