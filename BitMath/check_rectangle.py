
def distPoints(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def check_rectangle(A):
    center = [0, 0]
    for p in A:
        center[0] += p[0]/4.0
        center[1] += p[1]/4.0
    diagonal = 0
    for p in A:
        diagonal_next = distPoints(p, center)
        if diagonal != 0 and diagonal != diagonal_next:
            return False
        diagonal = diagonal_next
    return True


coords = [(3, 0), (7, 3), (4, 7), (0, 4)]
print(check_rectangle(coords))
