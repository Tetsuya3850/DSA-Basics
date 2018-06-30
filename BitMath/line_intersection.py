
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        deltaY = end.y - start.y
        deltaX = end.x - start.x
        self.slope = deltaY / deltaX
        self.yintercept = end.y - self.slope * end.x


def is_between(start, middle, end):
    return start.x <= middle.x <= end.x and start.y <= middle.y <= end.y


def intersection(start1, end1, start2, end2):
    if start1.x > start2.x:
        start1, start2 = start2, start1
        end1, end2 = end2, end1
    line1 = Line(start1, end1)
    line2 = Line(start2, end2)
    if line1.slope == line2.slope:
        if line1.yintercept == line2.yintercept and is_between(start1, start2, end1):
            return start2
        return None
    x = (line2.yintercept - line1.yintercept) / (line1.slope - line2.slope)
    y = x * line1.slope + line1.yintercept
    intersection = Point(x, y)
    if is_between(start1, intersection, end1) and is_between(start2, intersection, end2):
        return intersection
    return None
