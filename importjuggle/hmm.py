# coding: utf-8

# Refs: 
# https://note.nkmk.me/python-relative-import/
# https://note.nkmk.me/python-import-module-search-path/

import sys, os, pathlib
import pprint

# A
# ├── B ── C ── D.py <- entrypoint
# └── E ── F ── G.py <- some reusable module
#
#

# sys.path.append(pathlib.Path(os.path.dirname(__file__)).parents)[1]) 
# A をmodule読み込みdirにすることで、どこのmoduleへも降っていける. 
# パッケージトップから出なくでも実行可.
# from E.F import G

# パッケージトップレベルから実行. # もし階層が１層のみなら, from ..H import I
# from ...E.F import G

# 試行錯誤が必要
# from D.F import G

if __name__ == "__main__":
	#pprint.pprint(sys.path)
	pass