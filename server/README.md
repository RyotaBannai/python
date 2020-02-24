# Useful tips
## ヒアドキュメントを使うときの空白文字を消したい
- `str.strip()`で前後の空白文字を消去.
- \ backslashで改行文字を読み込ませない.

    >>> txt = '''\
    >>> got a whiff of something special.
    >>> that\'s good \'cause you about to eat it.\
    >>> '''

- python scrpting を使う. `str[1:-1]` -> 前後の文字以外を取り出す.
- python のインデントを消去する. `textwrap.dedent(str)`

## textwrap is fun
- 各行の前に何か付け加えたいとき `indent` predicate に条件をつけることができる. 
    >>> s = "\nthis is a pen\nI'm from Tokyo.\n"
    >>> m = textwrap.indent(text=s.strip(), prefix= '+ ', predicate=lambda line: 'Tokyo' in line)
    >>> this is a pen
    >>> + I'm from Tokyo.
- `textwrap.TextWrapper(width=50).fill(text=somelongtexts);` で一列の文字数を50以下に整形することができる.
- `textwrap.shorten(text=hugetext, width=100)`で100文字だけにすることができる. `placeholder="..."` みたに隠させた部分の表示方法も変えられる.
- `textwrap.TextWrapper(width=50).wrap(text=somelongtexts);` -> `wrap` メソッドはラップされた文字グループをリストにして返す. ex, `['This function returns the answer as STRING and not', 'LIST.']`