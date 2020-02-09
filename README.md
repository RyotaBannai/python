# Python_project
The record of my own learning history of Python.

# Memo
For Python Tutorial online resource.<br>
[用語集](https://docs.python.org/ja/3/glossary.html)<br>
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
#### 3.1.1. Number
- // 演算子は 整数除算 を行う
- 対話モードでは, 最後に表示された結果は変数 _ に代入される
- [Decimalを使用することで、浮動小数点数の計算, 例えば、1.1+2.2==3.3のような計算を正確に実行できる.](https://docs.python.org/ja/3/library/decimal.html#decimal.Decimal)
- 有理数計算はFractions (Decimalを使った場合, `Decimal('-3.14').as_integer_ratio()`とかでもでけきそう.)
#### 3.1.2. String
- 特殊文字を使用を表示するときは, print()で実行. `'C:\user\name'` のように特殊文字を評価したくないときは, 引用符の前にrをつけたraw string を使う. `print(r'C:\user\name')`
- 複数行に跨がるときは, `"""\...\...\..."""`（三重引用符）のようにする. 
- 文字列の連結は + または、間に空白のみを含む文字列リテラル. `'Py' 'thon' => 'Python', text = 'Py' \ 'thon'` is the same. これは文字列リテラルのみで可能. => 「リテラルと変数は連結できない」.　この場合 + を使用.
- 文字列のスライス: `s[:i] + s[i:] == s` はtrue. (`s,i ='test test', 2`)
- `s='test', s[10] >>> an error`, but s[3:10] is not an error. even s[4:10] is not an error.
- pythonの文字列はimmutable. "Oh i'd like to pluralize it." then,  `s[4:5] = 's' >>> an error`. => 新しく文字列を作成すること. `s[:4] + 's' => 'tests'`, または, `''.join((s[:4],'s'))`, by using tuple
- 文字列の長さを知りたいときは, 組み込み関数len()を使用.
#### 3.1.3. List
- list は「角かっこ[]」 でコンマ区切りしたデータ型.
- listの全てのスライス[:]で、シャローコピー.
- listは連結可. `[0,1,2] + [3,4,5] >>> [0,1,2,3,4,5]`
- listはstringとは違って, muttable だから要素の入れ替え可. `test=[0,1,2], test[1:]=[] >>> test is [0]`
- listにはappend()で要素を追加.
- listの入れ子はlistにlistを挿入するだけ. `b=[0,], b[0]=[] >>> b = [[]]` case closed.
### 3.2 The first step of programming
- print() にend を使うと改行なしで表示. `print(a, end=', ') >>> 0, 1, 1, 2, 3, 5`
## Chapter4 
### 4.1 
- Python の制御構文は if 条件1: elif 条件2: else: >>> elif!
- pythonで, phpのforeach($books as $id) を表現するには for id in books, もし辞書なら（phpなら連想配列） `for id in books.keys()` または `for value in books.values()` 同時にどちらも取り出すならば, `for id, value in books.items()` を使う. これらのメソッドで返されたオブジェクトをDictionary view (辞書ビュー)という.
- collectionなどの要素を消去したいときは, del. `users = {'user1': 'active', 'user2': 'inactive'}, del users['user1'] >>> users == {'user2': 'inactive'}`
### 4.3 
- range + len よりもenumerateの方がクリーン. `for data in list(enumerate(a, start=0))` enumerateはenumerateオブジェクトを作成する. enumerateの中ではyieldでつどtupleを返す. yield n, elem
- イテレータ: 反復して要素を取り出すことが出来る型のこと. Pythonのリストやセット、辞書型はイテレーションすることが出来るため, これらのオブジェクトはイテレータ.
- ジェネレータ: イテレータの一種. 要素を取り出すごとに処理を実行して、要素を生成することが出来る. yieldを使う. (return文は一度に大きなlistを返してしまい, 一度のたくさんのメモリを消費する恐れがある一方で, yieldは関数の実行を一時的に中断し, つどデータを返すため一度にたくさんのメモリを使わない.)
- generatorを作成したら, genetator.\_\_next\_\_()で一つずつyieldを呼び出せる. \_\_next\_\_()は特殊メゾット. そのほかには, \_\_reversed\_\_() \_\_contains\_\_() など. 組み込み関数である, next(generator)は\_\_next\_\_()を呼び出し, 一つ一つ取り出す. [`@yield.py`](https://github.com/RyotaBannai/Python_project/blob/master/yield.py)
- もし複数のgeneratorを同じ関数で使いたいときは, yield from を使う. `@yield_from.py`
- range() が返すオブジェクトは, いろいろな点でリストであるかのように振る舞いますが, 本当はリストではない. これは, イテレートした時に望んだ数列の連続した要素を返す「オブジェクト」です. しかし実際にリストを作るわけではないので, 「スペースの節約」になる. この性質を, iterableを呼ぶ.
### 4.5 path statement 
- passの用途は, 1. 最小限のclassを定義するとき, 2. 抽象度の高い開発をしたいときで, 後から実装するとき.
### 4.6 define function 
- [関数にはdocstring をいれる癖を付ける. """..."""](https://docs.python.org/ja/3/tutorial/controlflow.html#tut-docstrings)
- 関数内で global, nonlocal変数の参照はできるが, 代入はできない.
- 関数に渡す引数や関数は, 元の関数が呼ばれる時に, 「ローカルな」シンボルテーブル内に取り込まれまれ, 値渡しでその関数に渡される.
- 関数を定義すると, 関数名の値は, インタプリタからはユーザ定義関数 (user-defined function) として認識される型を持つ.
- returnを持たないfunction はprocedure だが, pythonの場合returnが無ければ必ずNoneを返すので常に関数である.
#### 4.7.1 default parameters 
- 関数は評価された時点での変数を読み込むため, 評価後の変数の変更はその関数に影響しない. `@function/scope.py`
- 関数のデフォルト値は全体を通して一度しか呼ばれない->値に変更があった場合, 何度も同じ関数を呼び出すと, 「値が更新されたり追加される.」 `@function/default.py`
- is : オブジェクトが同一かどうか調べる => オブジェクト固有のIDを比較. (処理が早く済むことや、Noneが「[シングルトンオブジェクト](https://docs.python.org/ja/3/tutorial/datastructures.html#more-on-conditions)」（そのクラスのオブジェクトは1つのみ、複数のインスタンスの作成が不可能であること, (変更可能なオブジェクト)）である)
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
### 4.8 間奏曲: コーディングスタイル 
- 演算子の前後とコンマの後には空白を入れ, 括弧類のすぐ内側には空白を入れないこと: `a = f(1, 2) + g(3, 4)`
- クラスや関数に一貫性のある名前を付けること. 慣習では UpperCamelCase をクラス名に使い、 lowercase_with_underscores を関数名やメソッド名に使う.
### 5.1 Data structure
- `a[len(a):] = [x]` と `a.append(x)`は等価.　_角カッコをつけるべきかどうかに注意を払う_. 初めの式では iterable objectのみ代入できるのに対し, 後者では, list などのiterable object を代入すると, 多次元配列になるため, intなどのnon iterableを使う. この場合は, extend([])を使用して, iterable objectを挿入することで, _次元数を変えずに_ 挿入できる.
- `a.insert(len(a), x)` と `a.append(x)`は等価.
- `a.clear` と `del a[:]` は等価.
- copy()はshallow で `a[:]`と等価.
- insert, remove, sort などのリストを操作するメソッドの戻り値はなく(変更可能なオブジェクトは返されず), d->insert("a")->remove("b")->sort(); のようなメソッドチェインはできない.
#### 5.1.1
- listを _スタック_ として使う. _last in first out_.
#### 5.1.2
- listを _キュート_ して使う. _first in first out_.
- キューの実装には, `collections.deque`を使うと良い. first in をpopleft()など使える.
#### 5.1.3 リストの内包表記
- `list(map(lambda x: x**2, range(10)))` や `[x**2 for x in range(10)]`は余分な変数を生成しなくてかつクリーンなコード. 変数xすら生成しない.
- for loop のネストも可. `[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]` これは右角かっこに向かうにつれてネストの内側表現している. 
#### 5.1.4. ネストしたリストの内包表記
- 2x3の多次元配列を 3x2にトランスポーズするコードを簡単実装. `[[row(i) for row in marray] for i in range(3)]` 外側の[]から評価が始まるため, i=0で固定され, 内側の[]に入る. この中では, 行それぞれの0番目の値を引き抜いて, 一つの行にする. それを列の数分繰り返す. ちなみにこの操作は, `list(zip(*matrix))`と等価. zipは複数のイテレータを同じ要素番目の要素を組み合わせ, tupleで返す. `a, b=[0,1], [10, 20] zip(a, b) >>> [(0, 10), (1, 20)]` もしこのa, bが同じ変数の要素である場合, c=[[0,1],[10, 20]]ならば\*(unpack)で展開する. `zip(*c)`. もし, aとbの要素数が異なっている場合は, [`itertools.zip_longest() `](https://docs.python.org/ja/3/library/itertools.html#itertools.zip_longest)で, 足りない分は `fillvalue=None`などで, 大きい方に合わせることもできる.
### 5.2. del 文
- del a[:] でカラ.
- del a で変数自体消去.
### 5.3. タプルとシーケンス
- listとは違って, tumpleは _immutable_. しかし, tumbleの中のlistはmutable.
- シーケンス (sequence) データ型 (シーケンス型 --- list, tuple, range )
- tupleは宣言はコンマで区切って複数並べる. 丸括弧で囲ってもいい. `t = 12, 23, 34` (_タプルパッキング_)
- `a, b, c = t`  _タブルアンパッキング_
- 1 個の項目からなるタプルの構築は最後に コンマを置く. `a = 'text', `
### 5.4. 集合型(set) 
- 集合: 重複する要素をもたない、順序づけられていない要素の集まり. `set = {0,1,2,3,4,5,6}` =>重複された値がある場合, 最初の物以外自動的に消去される.
- 空集合を作成するときは, `set()` `{}`(波括弧 (brace)のペア)はカラの辞書を作成.
### 5.5. 辞書
- タプルは, 文字列, 数値, その他のタプルのみを含む場合はキーにすることができる. 直接, あるいは間接的に変更可能なオブジェクトを含むタプルはキーにできない. また, リストをキーとして使うことはできない.
- `dict([('sape', 0000), ('guido', 1111)]) >>> {sape': 0000, 'guido': 1111}` `dict(sape=0000, guido=1111)`は等価.
- 辞書内包表現を使って、任意のキーと値のペアから辞書を作成. `{x: x*2 for x in range(3)} >>> {0: 0, 1: 2, 2: 4}`
### 5.7. 条件についてもう少し
- Note that in Python, unlike C, assignment inside expressions must be _done explicitly _with the _walrus operator(セイウチ演算子) or Assignment Expressions_ `:=`. This avoids a common class of problems encountered in C programs: typing = in an expression when == was intended. Python 3.8 以降で利用可.
### 6.1. モジュールについてもうすこし
- モジュールレベルの関数定義を実行すると, 関数名はモジュールのグローバルなシンボルテーブルに入る.
- import されたモジュール名は _import を行っているモジュールの_ グローバルなシンボルテーブルに置かれる.
- `import importlib; importlib.reload(modulename)` のように importlib.reload() を使用し, 修正後のモジュールをリロードする.
#### 6.1.1 モジュールをスクリプトとして実行する
- コマンドライン からPython ファイルを実行すると, \_\_name\_\_ に \_\_main\_\_が設定される, ため, import できると同時にスクリプトとしても実行することができる. [`@tutorial/main.py`](https://github.com/RyotaBannai/Python_project/blob/master/tutorial/main.py)
- この方法はモジュールに便利なユーザインターフェースを提供したり, テストのために (スクリプトをモジュールとして起動しテストスイートを実行して) 使わる.
#### 6.1.2. モジュール検索パス
- モジュールをインポートするとき, 1. インタープリターはまずその名前のビルトインモジュールを探す. 2. 見つからなかった場合, ファイルを sys.path にあるディレクトリのリストから探す. sys.path は次の場所に初期化される. 2.1 入力されたスクリプトのあるディレクトリ(あるいはカレントディレクトリ) 2.2 PYTHONPATH (ディレクトリ名のリスト. シェル変数の PATH と同じ構文) 2.3 インストールごとのデフォルト.  Python プログラムは 初期化された後、sys.path を修正するので, 2.1に標準ライブラリと同名のスクリプトがあると, 予期せぬエラーなることがある. [buildin とinstall先の場所について](https://docs.python.org/ja/3.6/install/index.html). install先の場所は, `/usr/local/lib/pythonX.Y/site-packages(など)` [`環境変数`を参照](https://docs.python.org/ja/3/using/cmdline.html#environment-variables) 
- シンボリックリンクをサポートするファイルシステム上では, 入力されたスクリプトのあるディレクトリはシンボリックリンクをたどった後に計算される. 言い換えるとシンボリックリンクを含むディレクトリは _モジュール検索パスに追加_ されない.

#### 6.1.3. "コンパイル" された Python ファイル
- Pythonはスクリプトを実行するたびに.pycのコンパイル済みのファイルを\_\_pycache\_\_/に作成し, 別のスクリプトや, インタープリターでそのモジュールを読み込む際に, 参照し, 高速化している.
- ソースモジュールのないコンパイル済みモジュールを配布したいときは、同ディレクトリなくてならず, このときソースモジュール(.py)があってはいけない.

### 6.2. 標準モジュール
- 任意のディレクトリをPYTHONPATHに追加したいときは, `sys.path.append('/ufs/guido/lib/python')`
### 6.3. dir()
- 組込み関数 `dir()` は、あるモジュールがどんな名前を定義しているか調べるために使える.
- 引数がなければ、 dir() は現在定義している名前( _変数、モジュール、関数、その他の、すべての種類の名前_ )を列挙する.
- dir() は, _組込みの関数や変数の名前_ はリストしない. これらの名前からなるリストが必要なら, 標準モジュール _builtins_ で定義されている.
### 6.4.
- パッケージ (package) は, Python のモジュール名前空間を "ドット付きモジュール名" を使って構造化する手段. 例えば, モジュール名 A.B は、 A というパッケージのサブモジュール B を表す. ちょうど、モジュールを利用すると、別々のモジュールの著者が互いのグローバル変数名について心配しなくても済むようになるのと同じように, ドット付きモジュール名を利用すると,  NumPy や Pillow のように複数モジュールからなるパッケージの著者が, 互いのモジュール名について心配しなくても済むようになる. 
### 7.1. 出力を見やすくフォーマットする
- フォーマット済み文字列リテラル を使うには、開き引用符や三重の開き引用符の前に f あるいは F を付けて文字列を始める. `year=2020; event='olympic'; f'results of the {year} {event}'` この先頭にfやFがついたも文字列リテラルのことを _f-string_ という.
- パーセンテージや浮動小数点数の桁数などを指定したいときは, [format()関数](https://docs.python.org/ja/3/library/string.html#formatspec)を使う. `'{:-9}, YES votes {:2.2%}'.format(yes_votes, percentage)` `'{2}, {1}, {0}'.format(*'123')` unpackも使える.
- `coord = (3, 5); 'X: {0[0]};  Y: {0[1]}'.format(coord)` {}で引数の要素へのアクセスも可能.
- `"repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')`
- `yes_votes = 42_572_654 >>> 42572654 ` separating numbers with underscore (_comma is used for defining tuple_)results in just numbers.
- 凝った出力である必要は無いけれど, デバッグ目的で変数をすばやく表示したいときは, repr() 関数か str() 関数で _どんな値も文字列_ に変換できる. repr()はquotesで囲まれた文字列をさらにdouble quotesで囲んだり, backslashをエスケープしたりと, インタープリターが読みやすい形式で表示するのに対し, str()はそのまま表示する. 辞書はjson.dumps()のように表示される.
#### 7.1.1. フォーマット済み文字列リテラル
- オプションの _フォーマット指定子_ を式の後ろに付けられる. このフォーマット指定子によって値のフォーマット方式を制御できる. `print(f'The value of pi is approximately {math.pi:.3f}.')` .3で浮動小数点を3桁まで表示. `:10` することにより, 最小の幅数を設定することで, 出力が整理されるためデータの可読性が向上する.
#### 7.1.2. 文字列の format() メソッド
- vars()はクラスや辞書の全てのローカルな変数を返すので, これをformat()と使えば,どんな変数が入っているか簡単に確認できる.
- `str.rjust(), str.ljust(), str.center()`で左右中央寄せができる. `format()のalignキーワードに <>^`を指定して行うことも可.　
- zfill() で前に0をfill.
### 7.2. ファイルを読み書きする
- ファイルオブジェクトを扱うときに with キーワードを使うのは良い習慣. その利点, 処理中に例外が発生しても必ず最後にファイルをちゃんと閉じること. with を使うと, 同じことを try-finally ブロックを使って書くよりずっと簡潔に書ける.
- with キーワードを使わない場合は, f.close() を呼び出してファイルを閉じ, そのファイルが使っていたシステムリソースをすぐに解放する必要がある. 明示的にファイルを閉じなかった場合は, いつかは Python のガベージコレクタがそのファイルオブジェクトを破棄し開かれいていたファイルを閉じるが, しばらくはファイルが開かれたままでいる可能性がある.
#### 7.2.1. ファイルオブジェクト(file object, or file-like object) のメソッド
- `with open('test.txt') as f`　で読み込んだファイルを, `list(f)`で一行ごとにリストにできる.
#### 7.2.2 json による構造化されたデータの保存
- 標準モジュール json は, Python のデータ 階層を取り, 文字列表現に変換する.（ _シリアライズ (serializing)_ ）文字列表現からデータを再構築することは、_デシリアライズ (deserializing)_.
- json.dumpsはシリアライズ, json.loadはでシリアライズ. json.dumps(x, f)でfで指定するファイルに書き込み. 一方読み込みは, そのままjson.load(f).
### 8.2. 例外
- ZeroDivisionError, NameError, TypeError などの例外型として出力される文字列は、発生した例外の組み込み名.
- try...except文 でエラーをキャッチできなかった場合, an unhundled error となり, システムのエラーが発動される. tryの結果を受けて処理をする _else_ を書いておくこともできる. else を指定した場合でも, an unhundled errorであることには変わりないため, どのエラーハンドラーでもエラーをキャッチできない場合は, システムのエラーが発動される.
### 8.3. [例外を処理する](https://docs.python.org/ja/3/tutorial/errors.html#handling-exceptions)
- exceptには複数のエラータイプを指定できる. `except (RuntimeError, TypeError, NameError):` 
- except 節のクラスは、例外と _同じクラスか 基底クラス_ のときに互換 (compatible)となる. つまり _派生クラス_ の例外がリストされている except 節は基底クラスの例外と互換ではない. => もし基底クラスをexceptの最初に記述した場合, その派生クラスの例外が全て基底クラスでハンドルされる. 基底クラスのハンドラーは最後に記述.  
- 例外ハンドラは, try 節の直接内側で発生した例外を処理するだけではなく, その try 節から (たとえ間接的にでも) 呼び出された _関数の内部で発生した例外_ も処理.
### 8.6. クリーンアップ動作を定義する
- finally 節は常に発動される. これは, (ファイルやネットワーク接続などの) 外部リソースを、利用が成功したかどうかにかかわらず解放するために便利. 
- errorが発生した場合, 基本的にはfinally が先に呼ばれて, その後にerror messageが表示される. `@tutorial/error.py`
