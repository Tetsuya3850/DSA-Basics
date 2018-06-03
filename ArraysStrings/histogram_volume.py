

def histogram_volume(histogram):
    left_maxes = [None] * len(histogram)
    left_max = histogram[0]
    for i in range(len(histogram)):
        left_max = max(left_max, histogram[i])
        left_maxes[i] = left_max
    sum = 0
    right_max = histogram[-1]
    for i in reversed(range(len(histogram))):
        right_max = max(right_max, histogram[i])
        second_tallest = min(right_max, left_maxes[i])
        if second_tallest > histogram[i]:
            sum += second_tallest - histogram[i]
    return sum


print(histogram_volume([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]))
