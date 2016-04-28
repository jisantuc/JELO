import string
from collections import Counter
from copy import deepcopy

def json_to_bow(js):
    tmp = deepcopy(js)
    words = tmp['Abstract']
    lookup = string.maketrans(string.ascii_lowercase, string.ascii_lowercase)

    word_list = string.translate(
        words.lower(), lookup,
        deletions=string.punctuation + string.digits
    ).split(' ')
    word_counts = Counter(word_list)
    tmp['BoW'] = {k: v for k, v in word_counts.items() if v > 1}
    return tmp
