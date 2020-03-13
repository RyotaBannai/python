# judge how many key& value pair shared


def judge_if_same(dictA, dictB) -> bool:
    """
    return True if the two dicts are the same key value pair
    return Flase if not.
    """
    shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
    return True if len(shared_items) == len(dictA) else False


if __name__ == "__main__":
    x = {'0000': 'Ryota', '0001': 'Taro'}
    y = {'1000': 'Mark', '1001': 'Zack'}

    result = judge_if_same(x, x)
    print(result)
