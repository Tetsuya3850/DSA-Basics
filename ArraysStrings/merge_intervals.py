
from operator import attrgetter


class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def add_interval(intervals, new_interval):
    # Time O(N), Space O(1), where N is the num of intervals in array.
    i = 0
    result = []
    while i < len(intervals) and new_interval.left > intervals[i].right:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and new_interval.right >= intervals[i].left:
        new_interval = Interval(min(new_interval.left, intervals[i].left), max(
            new_interval.right, intervals[i].right))
        i += 1

    return result + [new_interval] + intervals[i:]


def union_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=attrgetter('right'))
    result = [intervals[0]]
    for interval in intervals:
        if interval.left < result[-1].right:
            if interval.right > result[-1].right:
                result[-1].right = interval.right
        else:
            result.append(interval)
    return result
