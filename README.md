# Python_project
The record of my own learning history of Python.

# Memo
For Python Tutorial online resource.

## Chapter1
- 可変長配列や辞書などの高級な型を組込みで持つ 超高級言語(very-high-level language) 
- 標準モジュールには、ファイル I/O、システムコール、ソケットといった機能や、Tk のようなグラフィカルユーザインタフェースツールキットを使うためのインターフェイスなども提供
- 実行文のグループ化は、グループの開始や終了の括弧ではなくインデント
- 変数や引数の宣言が不要
- 拡張性: C 言語でプログラムを書く方法を知っているなら、簡単に新たな「組み込み関数やモジュール」を、簡単にインタプリタに追加可能. これによって、いちばん時間のかかる処理を高速化したり、ベンダ特有のグラフィクスライブラリなどの、 バイナリ形式でしか手に入らないライブラリを Python にリンクしたりできる

## Chapter2
- python3 < filename のように標準入力ファイルとして指定すると、インタプリタはファイルから スクリプト を読み込んで実行
- [コマンドラインと環境](https://docs.python.org/ja/3/using/cmdline.html#using-on-general)
- [対話モード(interactive mode)](https://docs.python.org/ja/3/tutorial/appendix.html#tut-interac) ：インタプリタが命令を端末 (tty) やコマンドプロンプトから読み取っている場合, インタプリタは 対話モード で動作している. このモードでは, インタプリタは 「一次プロンプト (primary prompt)（三つの「大なり記号」 (>>>) ） 」を表示して, ユーザにコマンドを入力するよう促す. 継続行では, インタプリタは 「二次プロンプト (secondary prompt)（デフォルトでは三つのドット (...) -> 関数宣言時など, 行が複数に跨がる場合には二次プロンプト） 」を表示.
- デフォルトエンコーディング以外のエンコーディングを使用するには, ファイルの 先頭 の行に特別なコメントを追加しなければならない. 例えば, Windows-1252 エンコーディングを使用するには, ソースコードの先頭に, # -*- coding: cp1252 -*- を追加.

## Chapter3
### 3.1.1. Number
- // 演算子は 整数除算 を行う
- 対話モードでは, 最後に表示された結果は変数 _ に代入される
- [Decimalを使用することで、浮動小数点数の計算, 例えば、1.1+2.2==3.3のような計算を正確に実行できる.](https://docs.python.org/ja/3/library/decimal.html#decimal.Decimal)
- 有理数計算はFractions (Decimalを使った場合, Decimal('-3.14').as_integer_ratio()とかでもでけきそう.)
### 3.1.2. String
- 特殊文字を使用を表示するときは, print()で実行. 'C:\user\name'のように特殊文字を評価したくないときは, 引用符の前にrをつけたraw string を使う. print(r'C:\user\name')
- 複数行に跨がるときは, `"""\...\...\..."""`（三重引用符）のようにする. 
- 文字列の連結は + または、間に空白のみを含む文字列リテラル. `'Py' 'thon' => 'Python', text = 'Py' \ 'thon'` is the same. これは文字列リテラルのみで可能. => 「リテラルと変数は連結できない」.　この場合 + を使用.
- 文字列のスライス: `s[:i] + s[i:] == s` はtrue. (`s,i ='test test', 2`)
- `s='test', s[10] >>> an error`, but s[3:10] is not an error. even s[4:10] is not an error.
- pythonの文字列はimmutable. "Oh i'd like to pluralize it." then,  `s[4:5] = 's' >>> an error`. => 新しく文字列を作成すること. `s[:4] + 's' => 'tests'`, または, `''.join((s[:4],'s'))`, by using tuple
- 文字列の長さを知りたいときは, 組み込み関数len()を使用.
### 3.1.3. List
- list は「角かっこ[]」 でコンマ区切りしたデータ型.
- listの全てのスライス[:]で、シャローコピーを実現.
- listは連結可. `[0,1,2] + [3,4,5] >>> [0,1,2,3,4,5]`
- listはstringとは違って, muttable だから要素の入れ替え可. `test=[0,1,2], test[1:]=[] >>> test is [0]`
- listにはappend()で要素を追加.
- listの入れ子はlistにlistを挿入するだけ. `b=[0,], b[0]=[] >>> b = [[]]` case closed.
### 3.2 The first step of programming
- print() にend を使うと改行なしで表示. `print(a, end=', ') >>> 0, 1, 1, 2, 3, 5`
## Chapter4 
### 4.1 
- Python の制御構文は if 条件1: elif 条件2: else: >>> elif!
- pythonで, phpのforeach($books as $id) を表現するには for id in books, もし辞書なら（phpなら連想配列） `for id in books.keys()` または `for value in books.values()` 同時にどちらも取り出すならば, `for id, value in books.items()` を使う.
- collectionなどの要素を消去したいときは, del. `users = {'user1': 'active', 'user2': 'inactive'}, del users['user1'] >>> users == {'user2': 'inactive'}`
### 4.3 
- range + len よりもenumerateの方がクリーン. `for data in list(enumerate(a, start=0))` enumerateはenumerateオブジェクトを作成する. enumerateの中ではyieldでつどtupleを返す. yield n, elem
- イテレータ: 反復して要素を取り出すことが出来る型のこと. Pythonのリストやセット、辞書型はイテレーションすることが出来るため, これらのオブジェクトはイテレータ.
- ジェネレータ: イテレータの一種. 要素を取り出すごとに処理を実行して、要素を生成することが出来る. yieldを使う. (return文は一度に大きなlistを返してしまい, 一度のたくさんのメモリを消費する恐れがある一方で, yieldは関数の実行を一時的に中断し, つどデータを返すため一度にたくさんのメモリを使わない.)
- generatorを作成したら, genetator.\_\_next\_\_()で一つずつyieldを呼び出せる. \_\_next\_\_()は特殊メゾット. そのほかには, \_\_reversed\_\_() \_\_contains\_\_() など. 組み込み関数である, next(generator)は\_\_next\_\_()を呼び出し, 一つ一つ取り出す. `@yield.py`
- もし複数のgeneratorを同じ関数で使いたいときは, yield from を使う. `@yield_from.py`
- range() が返すオブジェクトは, いろいろな点でリストであるかのように振る舞いますが, 本当はリストではない. これは, イテレートした時に望んだ数列の連続した要素を返す「オブジェクト」です. しかし実際にリストを作るわけではないので, 「スペースの節約」になる. この性質を, iterableを呼ぶ.
### 4.5 path statement 
- passの用途は, 1. 最小限のclassを定義するとき, 2. 抽象度の高い開発をしたいときで, 後から実装するとき.
### 4.6 define function 
- [関数にはdocstring をいれる癖を付ける. """..."""](https://docs.python.org/ja/3/tutorial/controlflow.html#tut-docstrings)
- 関数内で global, nonlocal変数の参照はできるが, 代入はできない.
- 関数に渡す引数や関数は, 元の関数が呼ばれる時に, 「ローカルな」シンボルテーブル内に取り込まれまれ, 値渡しでその関数に渡される.
- 関数を定義すると, 関数名の値は, インタプリタからはユーザ定義関数 (user-defined function) として認識される型を持つ.
- returnを持たないfunction はprocedure だが, pythonの場合returnが無ければ必ずnoneを返すので常に関数である.
#### 4.7.1 default parameters 
- 関数は評価された時点での変数を読み込むため, 評価後の変数の変更はその関数に影響しない. `@function/scope.py`
- 関数のデフォルト値は全体を通して一度しか呼ばれない->値に変更があった場合, 何度も同じ関数を呼び出すと, 「値が更新されたり追加される.」 `@function/default.py`
- is : オブジェクトが同一かどうか調べる => オブジェクト固有のIDを比較. (処理が早く済むことや、Noneが「シングルトンオブジェクト」（そのクラスのオブジェクトは1つのみ、複数のインスタンスの作成が不可能であること）である)
- == : 同じ値を持っているか調べる. 
#### 4.7.2 keyword parameters 
- 仮引数に, keywordとして引数を渡すことも可.
- 仮引数の最後に `**name` の形式のものがあると, それまでの仮引数に対応したものを「除くすべてのキーワード引数」が入った辞書を受け取る. `**name` は `*name` の形式をとる, 仮引数のリストを超えた「位置引数」の入った タプル を受け取る引数と組み合わせられる. (`*name` は  `**name` より前になければならない.)　=> つまり, 位置引数で溢れた引数は\*nameで掬えて, キーワード引数で溢れた引数は\*\*で掬える. この場合, キーワード付きで仮引数を指定していなくても, \*\*で掬えるため, errorにはならない.`@function/argmap.py`
#### 4.7.3 Special parameters 
- \* や/(positional-onlyは, Python3.8 から)を使用することでpositional-only(仮引数の最後に`/`)かkeyword-only(仮引数の最初に`*`)または, positional-only or keyword-only(キーワードで指定した仮引数を前後`\, standard, *`とする)の指定ができる. `@function/specialparam.py`
- positionalで指定したつもりの変数が, keywordパラメータの展開によって, 変数名が衝突してしまう場合がある. 例えば, `def f(name, **args)` を `f(1, **{'name':2})` のように呼び出すと, name仮引数が二つになり, エラーを投げる(`TypeError: f() got multiple values for argument 'name'`). これの対処法として, 意図的に初めのname仮引数はpositionalであると伝えれば良い. `def f(name, /, **args)` `@function/specialparam.py`

#### 4.7.4 optional parameter list 
- \*args を初めに指定することもでき, この場合その後に続く仮引数はキーワード引数によって区別することができる. `def f(*args, separater=','), f('I', 'am', 'hungry.', separater=' ')`
#### 4.7.5 unpack parameter list
- 引数にリストや辞書を渡したい場合は, unpackして渡す. listやtupleならば\*, 辞書なら\*\*を先頭に付与
#### 4.7.6 ラムダ式
- return は : の右側の式.
- ラムダの中の式ではlocalやfile変数も任意に取り込むことができる.
- sort組み込み関数などのkeyにはrambdaを使うと, 任意のデータを基準に実行することができる.
#### 4.7.7 documentation string 
- function.\_\_doc\_\_ で確認. 
#### 4.7.8 関数のアノテーション
- ユーザ定義関数で使用される型についての完全にオプションなメタデータ情報
- `def f(ham: str, eggs: str='eggs') -> str:`戻り値のアノテーションは `->`で定義. `@function/annotate.py`
#### 4.8. 間奏曲: コーディングスタイル 
- 演算子の前後とコンマの後には空白を入れ, 括弧類のすぐ内側には空白を入れないこと: `a = f(1, 2) + g(3, 4)`
- クラスや関数に一貫性のある名前を付けること. 慣習では UpperCamelCase をクラス名に使い、 lowercase_with_underscores を関数名やメソッド名に使う.