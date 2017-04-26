import re


special_chars = re.compile(r"[?,!.()'\":]")

dashes = re.compile("-")


def preprocess( str_in ):
    """
    >>> preprocess('----Hello?,!.():"Dude')
    'hello        dude'
    >>> preprocess("'")
    ' '
    """

    # Change all the uppercase letters in “str in” to lowercase letters.
    str1_out = str_in.lower()

    # Replace all the following parameters by “ ” (white space):
    # ? , ! . ( ) ’ " :
    str1_out = special_chars.subn(" ", str1_out)[0]

    # Remove all the “-” character in “str in”.
    str1_out = dashes.subn("", str1_out)[0]

    return str1_out


if __name__ == "__main__":
    import doctest
    doctest.testmod()
