# Python_project
The record of my own learning history of Python.

#Memo
For Python Tutorial online resource.
##Chapter1
- 可変長配列や辞書などの高級な型を組込みで持つ 超高級言語(very-high-level language) 
- 標準モジュールには、ファイル I/O、システムコール、ソケットといった機能や、Tk のようなグラフィカルユーザインタフェースツールキットを使うためのインターフェイスなども提供
- 実行文のグループ化は、グループの開始や終了の括弧ではなくインデント
- 変数や引数の宣言が不要
- 拡張性: C 言語でプログラムを書く方法を知っているなら、簡単に新たな「組み込み関数やモジュール」を、簡単にインタプリタに追加可能. これによって、いちばん時間のかかる処理を高速化したり、ベンダ特有のグラフィクスライブラリなどの、 バイナリ形式でしか手に入らないライブラリを Python にリンクしたりできる

##Chapter2
- python3 < filename のように標準入力ファイルとして指定すると、インタプリタはファイルから スクリプト を読み込んで実行
- [コマンドラインと環境](https://docs.python.org/ja/3/using/cmdline.html#using-on-general)
- [対話モード(interactive mode)](https://docs.python.org/ja/3/tutorial/appendix.html#tut-interac) ：インタプリタが命令を端末 (tty) やコマンドプロンプトから読み取っている場合, インタプリタは 対話モード で動作している. このモードでは, インタプリタは 「一次プロンプト (primary prompt)（三つの「大なり記号」 (>>>) ） 」を表示して, ユーザにコマンドを入力するよう促す. 継続行では, インタプリタは 「二次プロンプト (secondary prompt)（デフォルトでは三つのドット (...) -> 関数宣言時など, 行が複数に跨がる場合には二次プロンプト） 」を表示.
- デフォルトエンコーディング以外のエンコーディングを使用するには, ファイルの 先頭 の行に特別なコメントを追加しなければならない. 例えば、Windows-1252 エンコーディングを使用するには, ソースコードの先頭に, # -*- coding: cp1252 -*- を追加.

##Chapter3
###3.1.1. Number
- // 演算子は 整数除算 を行い、(小数部を切り捨てた) 整数値
- 対話モードでは、最後に表示された結果は変数 _ に代入される
- [Decimalを使用することで、浮動小数点数の計算, 例えば、1.1+2.2==3.3のような計算を正確に実行できる.](https://docs.python.org/ja/3/library/decimal.html#decimal.Decimal)
- 有理数計算はFractions (Decimalを使った場合, Decimal('-3.14').as_integer_ratio()とかでもでけきそう.)
###3.1.2. String
- 特殊文字を使用を表示するときは, print()で実行. 'C:\user\name'のように特殊文字を評価したくないときは, 引用符の前にrをつけたraw string を使う. print(r'C:\user\name')
- 複数行に跨がるときは, """\...\...\..."""（三重引用符）のようにする. 
- 文字列の連結は + または、間に空白のみを含む文字列リテラル. 'Py' 'thon' => 'Python', text = 'Py' \ 'thon' is the same. これは文字列リテラルのみで可能. => 「リテラルと変数は連結できない」.　この場合 + を使用.
- 文字列のスライス: s[:i] + s[i:] == s はtrue. (s,i ='test test', 2)
- s='test', s[10] >>> error, but s[3:10] is not an error. even s[4:10] is not an error.
- pythonの文字列はimmutable. "Oh i'd like to pluralize it." then,  s[4:5] = 's' >>> an error. => 新しく文字列を作成すること. s[:4] + 's' => 'tests', または, ''.join((s[:4],'s')), by using tuple
- 文字列の長さを知りたいときは, 組み込み関数len()を使用.
###3.1.3. List
- list は「角かっこ[]」 でコンマ区切りしたデータ型.
- listの全てのスライス[:]で、シャローコピーを実現.
- listは連結可. [0,1,2] + [3,4,5] >>> [0,1,2,3,4,5] 
- listはstringとは違って, muttable だから要素の入れ替え可. test=[0,1,2], test[1:]=[] >>> test is [0]
- listにはappend()で要素を追加.
- listの入れ子はlistにlistを挿入するだけ. b=[0,], b[0]=[] >>> b = [[]] case closed.