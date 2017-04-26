from collections import Counter


from problem1 import preprocess


def overlap_score(q1, q2):
    """
    q1, q2 are preprocessed sentences (strings)

    >>> overlap_score("a b", "a")
    0.6666666666666666

    """

    c1 = Counter(q1.split())
    c2 = Counter(q2.split())
    c1c2 = c1 + c2

    both = set(c1.keys())
    both = both.intersection(c2.keys())

    bothscore = float(sum(c1c2[x] for x in both))
    mplusn = float(sum(c1c2.values()))

    score = bothscore / mplusn

    return score



if True:
    import doctest
    doctest.testmod(verbose=True)
