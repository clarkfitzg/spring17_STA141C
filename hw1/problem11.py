import re

special_chars = re.compile(r"[?,!.()'\":]")
dashes = re.compile("-")

charlist = "? , ! . ( ) ' \" :".split()

# This is marginally slower on my laptop. But definitely easier to read!
def otherway(str_in):
    # Without regex
    str_out = str_in
    for char in charlist:
        str_out = str_out.replace(char, " ")
    return  str_out
    


def preprocess( str_in ):
    """
    >>> preprocess("Hey?,!.()':Dude-----")
    'hey        dude'
    >>> preprocess('"')
    ' '
    """
    # 1. Change all the uppercase letters in “str in” to lowercase letters.
    str_out = str_in.lower()

    # 2. Replace all the following parameters by “ ” (white space):
    # ? , ! . ( ) ’ " :
    str_out = special_chars.subn(" ", str_out)[0]

    # 3. Remove all the “-” character in “str in”.
    str_out = dashes.subn("", str_out)[0]

    return str_out


if __name__ == "__main__":

    import doctest
    doctest.testmod(verbose=True)
