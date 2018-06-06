
from collections import Counter


def ransom_note(note, magazine):
    # Time O(M + N), Space O(L), where M and N is the legth of the note and magazine and L is the num of distinct characters.
    char_freq_note = Counter(note)
    for c in magazine:
        if c in char_freq_note:
            char_freq_note[c] -= 1
            if char_freq_note[c] == 0:
                del char_freq_note[c]
            if not char_freq_note:
                return True
    return not char_freq_note
