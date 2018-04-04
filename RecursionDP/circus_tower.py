# A circus is designing a tower routine consisting of people standing atop one another's shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.

from operator import itemgetter

def circus_tower(people):
    def circus_tower_helper(people, bottom, offset, tower_map):
        if offset >= len(people):
            return 0
        newBottom = people[offset]
        numberWithBottom = 0
        if bottom == None or newBottom[1] > bottom[1]:
            if not tower_map[offset]:
                tower_map[offset] = circus_tower_helper(people, newBottom, offset + 1, tower_map)
                tower_map[offset] += 1
            numberWithBottom = tower_map[offset]
        numberWithOutBottom = circus_tower_helper(people, bottom, offset + 1, tower_map)
        return max(numberWithBottom, numberWithOutBottom)

    people.sort(key = itemgetter(0))
    tower_map = [0] * len(people)
    return circus_tower_helper(people, None, 0, tower_map)


A = [(60, 120), (68, 110), (65, 91), (56, 90), (70, 70), (75, 190)]
print (circus_tower(A))
