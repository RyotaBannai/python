def try_error_like_if_else():
    """
    else はif文に引っかからなかったときに, for文に属させることで,
    try and error のような構文にすることができる.
    """
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print('if:...', n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print('else:...', n, 'is a prime number')


# continueはあとの処理を飛ばす.
def skip_by_continue():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)


if __name__ == "__main__":
    try_error_like_if_else()
