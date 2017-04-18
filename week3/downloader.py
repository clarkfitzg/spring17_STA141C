# Python 3
from urllib.request import urlretrieve

# Python 2
#from urllib import urlretrieve


# Grab the baby names for some examples
babyurl = "https://www.ssa.gov/oact/babynames/names.zip"

fname = babyurl.split("/")[-1]

# This could take a while depending on your connection speed
urlretrieve(babyurl, fname)
