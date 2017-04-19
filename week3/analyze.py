import csv

f = open("yob2015.txt")

fields = ("name", "gender", "count")
reader = csv.DictReader(f, fieldnames = fields)

names = {x["name"]: int(x["count"]) for x in reader}

names_list = list(names.keys())


# THE RIGHT WAY :)
# O(1) operation
%timeit "Julia" in names

# WRONG WAY :(
# O(n) operation with n ~ 32K
%timeit "Julia" in names_list
