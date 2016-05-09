import string
from collections import Counter
from copy import deepcopy
from gensim import corpora

def json_to_wl(js):
    tmp = deepcopy(js)
    words = tmp['Abstract']
    lookup = string.maketrans(string.ascii_lowercase, string.ascii_lowercase)

    word_list = string.translate(
        words.lower(), lookup,
        deletions=string.punctuation + string.digits
    ).split(' ')
    word_counts = Counter(word_list)
    filter_list = ['abstract'] # can be extended to remove more
    # sorted for testability's sake
    tmp['word_list'] = sorted([w for w in word_list if word_counts[w] > 1 and w not in filter_list])
    return tmp

def json_w_wl_to_texts(jslist):
    """
    Converts list of json objects with word lists into lists of just
    each objects word lists.
    """

    return [js['word_list'] for js in jslist]

def json_w_wl_to_dictionary(jslist, output=None):
    """
    Converts list of json objects with word lists into a dictionary
    a la gensim
    """

    dictionary = copora.Dictionary(json_w_wl_to_texts(jslist))
    if output:
        dictionary.save(output)
    return dictionary

def jslist_to_corpus(jslist, dictionary):
    """
    Creates a corpus of sparse vectors in (id, count) format from
    a list of json objects and an already existing gensim dictionary
    """

    json_w_wl = json_to_wl(jslist)
    return [dictionary.doc2bow(js['word_list']) for js in json_w_wl]
