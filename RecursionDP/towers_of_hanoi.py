
def towers_of_hanoi(n):
    # Time O(2^N), Space O(N), where N is the height of the tower.
    def towers_of_hanoi_helper(n, fro, to, buf):
        if n <= 0:
            return
        elif n == 1:
            return to.append(fro.pop())
        towers_of_hanoi_helper(n-1, fro, buf, to)
        towers_of_hanoi_helper(1, fro, to, buf)
        towers_of_hanoi_helper(n-1, buf, to, fro)

    towers = [[] for _ in range(3)]
    for i in reversed(range(1, n+1)):
        towers[0].append(i)
    towers_of_hanoi_helper(n, towers[0], towers[2], towers[1])
    return towers


print(towers_of_hanoi(3))
