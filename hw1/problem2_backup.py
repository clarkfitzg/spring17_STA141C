"""
0.961538461538
0.52380952381
0.0
0.4
0.676470588235
0.5
0.75
0.444444444444
0.107142857143
0.588235294118
"""

from collections import Counter
import csv

from problem1 import preprocess


def overlap_score(q1, q2):
    """
    >>> overlap_score("fun", "real fun")
    0.6666666666666666
    >>> overlap_score("  ", "   ")
    0
    """

    q1count = Counter(q1.split())
    q2count = Counter(q2.split())

    both = set(q1count.keys())
    both = both.intersection(q2count.keys())
    combined = q1count + q2count

    mplusn = float(sum(combined.values()))
    overlap = float(sum(combined[x] for x in both))

    try:
        return overlap / mplusn
    except ZeroDivisionError:
        return 0


def overlap_scores(fname):
    """
    Generator over scores
    """
    with open(fname) as f:
        reader = csv.reader(f)
        for line in reader:
            q1 = preprocess(line[3])
            q2 = preprocess(line[4])
            yield overlap_score(q1, q2)
            

if True:
    import doctest
    doctest.testmod()


def main(fname):
    for score in overlap_scores(fname):
        print(score)


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
