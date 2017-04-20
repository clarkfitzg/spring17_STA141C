# Python 3
from urllib.request import urlretrieve


print("hey!!!")
# Python 2
#from urllib import urlretrieve


# Grab the baby names for some examples
babyurl = "https://www.ssa.gov/oact/babynames/names.zip"

# Last 
babyurl.split("/")

babyurl.split("/")[-1]

fname = babyurl.split("/")[-1]

if __name__ == "__main__":
    # This could take a while depending on your connection speed
    urlretrieve(babyurl, fname)
