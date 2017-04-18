import csv
from zipfile import ZipFile
from collections import deque


zf = ZipFile("names.zip")

# Inspect this object

zf.namelist()

# Extract file to current directory
zf.extract("yob2015.txt")

fields = ("name", "gender", "count")

# A file pointer
with open("yob2015.txt") as f:
    reader = csv.DictReader(f, fieldnames=fields)
    names_hash = {row["name"]: int(row["count"]) for row in reader}


names_list = list(names_hash.keys())


# Run in Ipython

%timeit "Jackie" in names_hash

# This is 8000 times slower!!
%timeit "Jackie" in names_list


def make_names_deque():
    names_deque = deque()
    with open("yob2015.txt") as f:
        reader = csv.DictReader(f, fieldnames=fields)
        for row in reader:
            names_deque.appendleft(row["name"])
    return names_deque


# 101 ms
%timeit make_names_deque()


# How people actually use deques:
orders = deque()

orders.appendleft("hot dog")
orders.appendleft("hamburger")
orders.appendleft("beer")


def crazy_make_names_list():
    """
    DON'T do this :)
    """
    names_list = list()
    with open("yob2015.txt") as f:
        reader = csv.DictReader(f, fieldnames=fields)
        for row in reader:
            names_list.insert(0, row["name"])
    return names_list


%timeit crazy_make_names_list()
