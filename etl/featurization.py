import string
from collections import Counter
from copy import deepcopy
from gensim import corpora

def json_to_wl(js):
    tmp = deepcopy(js)
    words = tmp['Abstract']
    lookup = string.maketrans(string.ascii_lowercase, string.ascii_lowercase)

    word_list = (words
                 .lower()
                 .encode('ascii', errors='replace')
                 .translate(lookup, string.punctuation + string.digits)
                 .split(' '))
    word_counts = Counter(word_list)
    ## can be extended to remove more
    stopwords = ['abstract', 'and', 'the', 'of', 'a', 'in', 'to', 'that',
                 'is', 'with', 'are', 'we', 'for', 'on', 'i', 'an', 'be',
                 'this', 'as', 'by', 'from', 'when', 'which', 'model',
                 'models', 'their', 'it', 'these', 'they', 'have', 'find',
                 'more']
    # sorted for testability's sake
    tmp['word_list'] = sorted([w for w in word_list if word_counts[w] > 1 and w not in stopwords])
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

    dictionary = corpora.Dictionary(json_w_wl_to_texts(jslist))
    if output:
        dictionary.save(output)
    return dictionary

def jslist_to_corpus(json_w_wl, dictionary):
    """
    Creates a corpus of sparse vectors in (id, count) format from
    a list of json objects and an already existing gensim dictionary
    """

    return [dictionary.doc2bow(js['word_list']) for js in json_w_wl]
