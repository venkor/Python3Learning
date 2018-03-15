
# A modern and fast solution, for Python 3.7. May also work in some interpreters of Python 3.6.
#
# TLDR
#
# To sort a dictionary by keys use:
#
# sorted_dict = {k: disordered[k] for k in sorted(disordered)}
# Almost three times faster than the accepted answer; probably more when you include imports.
#
# Comment on the accepted answer
#
# The example in the accepted answer does not use the key parameter for sorted() which (granted, looks nice and requires less typing) is slower as both elements of generated tuples (key, value) are compared. As Python dictionaries cannot have two items with the same key, using the second element of the tuple for comparison is unnecessary.
#
# How to sort by key in Python 3.7
#
# The big change in Python 3.7 is that the dictionaries are now ordered by default.
#
# You can generate sorted dict using dict comprehensions.
# Using OrderedDict might still be preferable for the compatibility sake.
# Do not use sorted(d.items()) without key.
# disordered = {10: 'b', 3: 'a', 5: 'c'}
#
# # sort keys, then get values from original - fast
# sorted_dict = {k: disordered[k] for k in sorted(disordered)}
#
# # key = itemgetter - slower
# from operator import itemgetter
# key = itemgetter(0)
# sorted_dict = {k: v for k, v in sorted(disordered.items(), key=key)}
#
# # use key = lambda - the slowest
# key = lambda item: item[0]
# sorted_dict = {k: v for k in sorted(disordered.items(), key=key)}

from timeit import repeat

setup_code = """
from operator import itemgetter
from collections import OrderedDict
import random
random.seed(0)
d = {i: chr(i) for i in [random.randint(0, 12) for repeat in range(12)]}
key_getter = itemgetter(0)
key_lambda = lambda item: item[0]
"""

cases = [
    # fast
    '{k: d[k] for k in sorted(d)}',
    '{k: v for k, v in sorted(d.items(), key=key_getter)}',
    '{k: v for k, v in sorted(d.items(), key=key_lambda)}',
    # slower
    'dict(sorted(d.items(), key=key_getter))',
    'dict(sorted(d.items(), key=key_lambda))',
    'dict(sorted(d.items()))',
    # the slowest
    'OrderedDict(sorted(d.items(), key=key_getter))',
    'OrderedDict(sorted(d.items(), key=key_lambda))',
    'OrderedDict(sorted(d.items()))',
]

for code in cases:
    times = repeat(code, setup=setup_code, repeat=3)
    print(f"Best for {code}: {min(times)}")
