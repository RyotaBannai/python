# encoding = utf-8
import traceback
import sys
from pprint import pprint


def another_function():
    lumberjack()


def lumberjack():
    try:
        tuple()[0]
    except IndexError:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        #traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
        # print(traceback.extract_tb(exc_traceback))
        # traceback.print_exc(file=sys.stdout)
        # traceback.print_list(extracted_list=traceback.extract_stack())

        formatted_lines = traceback.format_exc().splitlines()
        # print(formatted_lines)

        print(repr(traceback.format_tb(exc_traceback)))


def lumberstack():
    traceback.print_stack()  # 普通の形式
    pprint(repr(traceback.extract_stack()))
    pprint(repr(traceback.format_stack()))


def mytraceback():
    tb_list = traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'),
                                     ('eggs.py', 42, 'eggs', 'return "bacon"')])
    an_error = IndexError('tuple index out of range')
    err = traceback.format_exception_only(type(an_error), an_error)

    pprint(tb_list)
    print('\n', err)


if __name__ == "__main__":
    # another_function()
    mytraceback()
