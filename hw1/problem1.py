import re


special_chars = re.compile(r"[?,!.()'\":]")


dashes = re.compile("-")


def preprocess( str_in ):
    """
    >>> preprocess("Hello?,!.(':Guy---")
    'hello       guy'
    >>> preprocess('"')
    ' '
    """
    str_out = str_in.lower()
    str_out = special_chars.subn(" ", str_out)[0]
    str_out = dashes.subn("", str_out)[0]
    return str_out


if __name__ == "__main__":
    import doctest
    doctest.testmod()
