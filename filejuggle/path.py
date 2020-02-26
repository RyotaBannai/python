# coding= utf-8
import os
import pathlib
import imported 

if __name__ == "__main__":
  # __file__　はファイルを実行した時しか定義されないので,
  # python cliを立ち上げたときに呼び出される .pythonstartup fileで呼び出すと怒られる.
  print(os.getcwd())
  print(imported.imhere())

  print('file abs path', os.path.abspath(__file__))
  print('file\'s abs dir ', os.path.dirname(os.path.abspath(__file__)))

  filename = 'keyword.txt'
  filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
  print('filepath: ', filepath)

  ifexist = os.path.exists(filename)
  print(ifexist)
  if ifexist:
    flags = os.O_RDWR
    #print(os.open(filepath, flags)) os.open method returns file descripter 
    with open(filename, mode='r') as f:
      print(f.read()) #ファイル全部を文字列として読み込みたい場合はread
                      #行ごとにリストで読み込みたい場合は, readlines
    
    #pathlib.Pathは高性能
    # home, parent, parents , open, glob, is_**, rename, resolve, replace
    # root, anchor, suffix (.py, ,rb), stem (/foo/bar/baz.py -> baz.py)
    # with_suffix, expanduser('~') -> /$HOME/[Username]/
    # touch
    # mkdir(parents=True, exist_ok=True) touch()の場合は, 中間dirがないと怒られるので, parentも一緒に作成するよう Trueとし、もしすでに同名のfileがあってもいいなら exist_ok=Trueにする.

    pathlib.Path('/image/test.txt'.replace('.txt','_proc.txt')).replace
    #Path.replace ->filesystem上のファイルを上書きするため注意.
    #Path.unlink() ->filesystem上からファイルを消去. iterdir()から再起的にunlink()は危ない.
    kywd = ''
    with pathlib.Path(filename).open(mode='r') as f:
      kywd = f.read()
    kywd = kywd.split()
    print(kywd)
    #もしカンマ+空白文字があったりする汚れたデータなんかは, + split(',') + strip()でやっつける.
    s = 'some, really , weirdies. , who should,, i blame, on this,? '
    clean = [x.strip() for x in s.split(',') if not x.strip() == '']
    print(clean)
    print(' '.join(clean))