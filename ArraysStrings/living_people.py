class Person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death


def most_alive(people):
    # Given a list of people with their birth and death years, implement a method to compute the year with the most number of people alive. You may assume that all people were born between 1900 and 2000. If a person was alive during any portion of that year, they should be included in that year's count.
    # Time O(R+P), Space O(R), where R is the range of the table and P is the num of people.

    alive_table = [0] * 250
    for person in people:
        alive_table[person.birth - 1900] += 1
        alive_table[person.death - 1900 + 1] -= 1
    max_total = 0
    current_total = 0
    for year in alive_table:
        current_total += year
        max_total = max(max_total, current_total)
    return max_total


people = []
people.append(Person(1901, 1999))
people.append(Person(1924, 1990))
people.append(Person(1903, 1940))
people.append(Person(1914, 1950))
people.append(Person(1932, 1960))
people.append(Person(1943, 1943))
print(most_alive(people))
