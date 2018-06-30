
def water_in_histogram(histogram):
    # Time O(N), Space O(N), where N is the length of the histogram.
    left_maxes = [None] * len(histogram)
    left_max = histogram[0]
    for i in range(len(histogram)):
        left_max = max(left_max, histogram[i])
        left_maxes[i] = left_max
    volume = 0
    right_max = histogram[-1]
    for i in reversed(range(len(histogram))):
        right_max = max(right_max, histogram[i])
        second_tallest = min(right_max, left_maxes[i])
        if second_tallest > histogram[i]:
            volume += second_tallest - histogram[i]
    return volume


print(water_in_histogram([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]))
