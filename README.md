# Python_project
The record of my own learning history of Python.

#Memo
- 可変長配列や辞書などの高級な型を組込みで持つ 超高級言語(very-high-level language) 
- 標準モジュールには、ファイル I/O、システムコール、ソケットといった機能や、Tk のようなグラフィカルユーザインタフェースツールキットを使うためのインターフェイスなども提供
- 実行文のグループ化は、グループの開始や終了の括弧ではなくインデント
- 変数や引数の宣言が不要
- 拡張性: C 言語でプログラムを書く方法を知っているなら、簡単に新たな「組み込み関数やモジュール」を、簡単にインタプリタに追加可能. これによって、いちばん時間のかかる処理を高速化したり、ベンダ特有のグラフィクスライブラリなどの、 バイナリ形式でしか手に入らないライブラリを Python にリンクしたりできる
- python3 < filename のように標準入力ファイルとして指定すると、インタプリタはファイルから スクリプト を読み込んで実行
- (コマンドラインと環境)[https://docs.python.org/ja/3/using/cmdline.html#using-on-general]
- (対話モード(interactive mode))[https://docs.python.org/ja/3/tutorial/appendix.html#tut-interac] ：インタプリタが命令を端末 (tty) やコマンドプロンプトから読み取っている場合, インタプリタは 対話モード で動作している. このモードでは, インタプリタは 「一次プロンプト (primary prompt)（三つの「大なり記号」 (>>>) ） 」を表示して, ユーザにコマンドを入力するよう促す. 継続行では, インタプリタは 「二次プロンプト (secondary prompt)（デフォルトでは三つのドット (...) -> 関数宣言時など、行が複数に跨がる場合には二次プロンプト） 」を表示.
- デフォルトエンコーディング以外のエンコーディングを使用するには, ファイルの 先頭 の行に特別なコメントを追加しなければならない. 例えば、Windows-1252 エンコーディングを使用するには, ソースコードの先頭に, # -*- coding: cp1252 -*- を追加.