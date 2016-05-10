from gensim.models import ldamodel

def train_lda_model(features, dictionary, num_topics):
    """
    Comically thin wrapper around gensim's ldamodel, taking
    features as a bag-of-words, dictionary as a gensim dictionary,
    and num_topics as an int and returning the trained model
    """

    # many passes because small dataset
    return ldamodel.LdaModel(corpus=features,
                             id2word=dictionary,
                             num_topics=num_topics,
                             update_every=1,
                             passes=20)
