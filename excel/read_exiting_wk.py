from openpyxl import load_workbook
import myOpenpyxl as fn


def print_xl_file(sheet: list) -> None:
    """
    ワークシートをもらって、
    その中の全部のセルをそのまま表示.
    """
    for line in sheet:
        # line はTuple
        for v in line:
            print(v.value, end=',')
        print('\n')


if __name__ == "__main__":
    opdir = fn.read_output_dir()
    wb = load_workbook(filename=str(opdir/'test2.xlsx'))
    sheet = wb['test excel file name']
    print_xl_file(sheet)
