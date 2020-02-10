import argparse
import os


parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')

#nargs は最低でも一つ以上のファイルがpass されないとエラー
#*なら0個でもnonerror
parser.add_argument('filenames', nargs='+')  #ファイル名リストなどの位置引数
parser.add_argument('-l', '--lines', type=int, default=10) #flag list オプション引数

args = parser.parse_args() #コマンドライン から渡されたデータをパース.
                           #以下のようにどのように実行されるか実際のコマンドを渡して, テストも可能.
# parser.parse_args('--foo 1 --foo 2'.split())


print(args)
for data in enumerate(args.filenames):
  print('No.'+str(data[0])+' file '+('-'*40))
  os.system('cat -n {fileName} | head -n5'.format(fileName=data[1]))
