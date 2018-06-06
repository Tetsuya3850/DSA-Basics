
def intersect_rectangle(R1, R2):
    def is_intersect(R1, R2):
        return (R1.x <= R2.x + R2.width) and (R1.x + R1.width >= R2.x) and (R1.y <= R2.y + R2.height) and (R1.y + R1.height >= R2.y)

    if is_intersect(R1, R2):
        return (max(R1.x, R2.x), max(R1.y, R2.y), min(R1.x + R1.height, R2.x + R2.width) - max(R1.x, R2.x), min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))
    else:
        False
