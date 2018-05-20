from operator import attrgetter


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=attrgetter('end'))
    end = intervals[0].end
    count = 1
    for i in range(1, len(intervals)):
        if end <= intervals[i].start:
            count += 1
            end = intervals[i].end
    return len(intervals) - count
