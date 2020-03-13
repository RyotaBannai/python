# judge how many key& value pair shared
import deepdiff
import json
import numpy as np


def judge_if_same(dictA, dictB) -> bool:
    """
    return True if the two dicts are the same key value pair
    return Flase if not.
    """
    shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
    return True if len(shared_items) == len(dictA) else False


def compare_dict(a, b):
    """
    This is the super useful when you wanna know which values are different.
    Compares two dictionaries..
    Posts things that are not equal..
    """
    res_compare = []
    for k in set(list(a.keys()) + list(b.keys())):
        if isinstance(a[k], dict):
            z0 = compare_dict(a[k], b[k])
        else:
            z0 = a[k] == b[k]

        z0_bool = np.all(z0)
        res_compare.append(z0_bool)
        if not z0_bool:
            print(k, a[k], b[k])
    return np.all(res_compare)


if __name__ == "__main__":
    x = {'0000': 'Ryota', '0001': 'Taro'}
    y = {'1000': 'Mark', '1001': 'Zack'}
    z = {'0000': 'Ryota', '0001': 'Taro'}

    result = judge_if_same(x, x)

    # wait... this works...
    is_the_same = x == z
    # print(is_the_same)

    # id there is a guarantee all keys are the same then, deepdiff is very useful.
    dict_1 = {
        "a": 1,
        "nested": {
            "b": 1,
            "c": 2
        }
    }
    dict_2 = {
        "a": 2,
        "nested": {
            "b": 1,
            "c": 2
        }
    }
    diff = deepdiff.DeepDiff(dict_1, dict_2)
    # print(json.dumps(diff, indent=4))

    compare_dict(dict_1, dict_2)
