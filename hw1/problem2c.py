from collections import Counter


def overlap_score(q1, q2):
    """
    >>> overlap_score("a b c", "a b")
    0.8

    >>> overlap_score("   ", " ")
    0
    """

    c1 = Counter(q1.split())
    c2 = Counter(q2.split())

    numerator = 0
    for word in c1:
        if word in c2:
            numerator += c1[word]
    for word in c2:
        if word in c1:
            numerator += c2[word]

    m = sum(c1.values())
    n = sum(c2.values())

    try:
        score = numerator / (m + n)
    except ZeroDivisionError:
        score = 0
    return score


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
