import json

def to_json_list(lines):
    ''' treats each line in lines as a json and attempts to load '''
    return [json.loads(x.strip()) for x in lines]

def to_jel_letters(codes):
    """
    reduces JEL code specificity from Cxx to C, returning the set of
    codes. This is necessary because abstracts in EconPapers are only
    available at consistent CSS selections so far into the past, and
    it's a cheap way to reduce from like a hundred categories to about
    twenty. Code list available here:
    http://econpapers.repec.org/scripts/jelsearch.pf
    """

    if not all([x.isalnum() for x in codes]):
        bad_codes = [x for x in codes if not x.isalnum()]
        raise ValueError("Bad JEL codes: {}".format(bad_codes))
    elif not all([x[0].isalpha() for x in codes]):
        bad_codes = [x for x in codes if not x[0].isalpha()]
        raise ValueError("Bad JEL codes: {}".format(bad_codes))

    return set(x[0] for x in codes)
