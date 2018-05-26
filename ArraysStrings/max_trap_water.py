

def max_trap_water(heights):
    # Time O(N), Space O(1), where N is the num of length.
    i = 0
    j = len(heights) - 1
    max_water = 0
    while i < j:
        width = j-i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1
        else:
            i += 1
    return max_water
