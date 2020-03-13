# how to marge dict
from copy import deepcopy
import itertools


def merge_two_dict(a: dict, b: dict):
    x = a.copy()
    x.update(b)
    return x


def dict_of_str_merge(x, y):
    z = {}
    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        z[key] = [x[key], y[key]]
    for key in x.keys() - overlapping_keys:
        z[key] = deepcopy(x[key])
    for key in y.keys() - overlapping_keys:
        z[key] = deepcopy(y[key])
    return z


def dict_of_dicts_merge(x, y):
    z = {}

    if isinstance(x, str) | isinstance(y, str):
        return [x, y]

    overlapping_keys = x.keys() & y.keys()
    for key in overlapping_keys:
        z[key] = dict_of_dicts_merge(x[key], y[key])
    for key in x.keys() - overlapping_keys:
        z[key] = deepcopy(x[key])
    for key in y.keys() - overlapping_keys:
        z[key] = deepcopy(y[key])
    return z


if __name__ == "__main__":
    # the same keys aren't allowed.
    x = {'0000': 'Ryota', '0001': 'Taro'}
    y = {'1000': 'Mark', '1001': 'Zack'}
    # duplidated items will be removed without addional codes.
    duplicated_items = {'1002': 'Mark', '1001': 'Zack'}

    z = {**x, **y, **duplicated_items}

    merged = merge_two_dict(x, y)

    # Python 3.9 or greater version
    # z = x | y # means merging two dicts!!

    # dict items is like set. so union results in combining to dits.
    new_dict = dict(x.items() | y.items())

    # by using dict constructor: not recommended way to combine.
    new_dict = dict(x, **y)

    new_items = {'0000': 'Bannai', '0002': 'Stanford'}
    merged_same_keys = dict_of_str_merge(x, new_items)
    # print(merged_same_keys)

    mutiple_layered_x = {'a': {1: {}, 2: {}}, 'b': {2: {3: 'Hi'}}}
    mutiple_layered_y = {'b': {10: 'haha', 2: {3: 'Hello'}}, 'c': {11: {}}}

    merged_same_keys2 = dict_of_dicts_merge(
        mutiple_layered_x, mutiple_layered_y)
    # print(merged_same_keys2)

    # the same keys are overwritten by later defined ones
    have_the_same_keys = {'a': {1: 'Some', 2: 'thing'},
                          'a': {3: 'any', 4: 'thing'}
                          }
    # print(have_the_same_keys['a'])

    # dict comprehension: -> hahaha doesn't work
    # dict_comp = {k: v for d in mutiple_layered_y for k,
    #             v in d.items() if not isinstance(d, str)}

    # by using itertools
    x_items = mutiple_layered_x.items()
    y_items = mutiple_layered_y.items()
    new_items_with_original_orders = dict(itertools.chain(x_items, y_items))
    print(new_items_with_original_orders)
