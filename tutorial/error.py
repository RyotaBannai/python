def bool_return():
    """
      もしfinally節もreturn, break, or continueを持っていれば,
      tryではなくfinallyの物が優先される.
    """
    try:
        print('haha')
        return True
    finally:
        return False

# print(bool_return())


def justbefore():
    """
      If the try statement reaches a return, break, or continue statement,
      the finally clause will execute '''just prior''' to the  return, break, or continue statement's execution.
    """
    try:
        return True
    finally:
        print('Finally!')

    print('After try and except')


def divide_else(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('you cant divde number by zero')
    else:
        # 正常終了時にだけ実行
        print('awesome!')


if __name__ == "__main__":
    """
    前者のように処理の前に明示的に条件判定を行うスタイルは「LBYL: Look Before You Leap（転ばぬ先の杖）」、
    後者のように例外処理を用いるスタイルは「EAFP: Easier to Ask for Forgiveness than Permission（認可をとるより許しを請う方が容易）」と呼ばれる。
    """

    # custom exception
    # ref : https://www.programiz.com/python-programming/user-defined-exception

    # justbefore()
    # bool_return()
    divide_else(1, 0)
