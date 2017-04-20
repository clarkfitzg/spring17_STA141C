import csv
from zipfile import ZipFile
from collections import deque


zf = ZipFile("names.zip")

# Inspect this object

zf.namelist()

# Extract file to current directory
zf.extract("yob2015.txt")






















import pandas as pd

pd


fields = ("name", "gender", "count")

# A file pointer

with open("yob2015.txt") as f:
    reader = csv.DictReader(f, fieldnames=fields)
    names_hash = {row["name"]: int(row["count"]) for row in reader}



names_list = list(names_hash.keys())


# Run in Ipython



# This is O(1)
# AWESOME!
%timeit "Zhuoer" in names_hash 

# This is O(n)
# TERRIBLE!! :(
%timeit "Zhuoer" in names_list


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













# The right way to find an intersection:
n1, n2 = names_list[:15000], names_list[14000:]

# THE RIGHT WAY
%timeit middle = set(n1).intersection(n2)


def crazy_intersect(a, b):
    """
    DON'T do this :)
    It's O(n^2) !!!! BAD!!
    """
    both = []
    for x in a:
        if x in b:
            both.append(x)


%timeit middle = crazy_intersect(n1, n2)
