# Useful tips
## ヒアドキュメントを使うときの空白文字を消したい
- `str.strip()`で前後の空白文字を消去.
- \ backslashで改行文字を読み込ませない.
```python
txt = '''\
got a whiff of something special.
that\'s good \'cause you about to eat it.\
'''
```
- python scrpting を使う. `str[1:-1]` -> 前後の文字以外を取り出す.
- python のインデントを消去する. `textwrap.dedent(str)`

## textwrap is fun
- 各行の前に何か付け加えたいとき `indent` のpredicate に条件をつけることができる. 
```python
s = "\nthis is a pen\nI'm from Tokyo.\n"
m = textwrap.indent(text=s.strip(), prefix= '+ ', predicate=lambda line: 'Tokyo' in line)
>>> this is a pen
>>> + I'm from Tokyo.
```
- `textwrap.TextWrapper(width=50).fill(text=somelongtexts);` で一列の文字数を50以下に整形することができる.
- `textwrap.shorten(text=hugetext, width=100)`で100文字だけにすることができる. `placeholder="..."` みたいに隠した部分の表示方法も変えられる.
- `textwrap.TextWrapper(width=50).wrap(text=somelongtexts);` -> `wrap` メソッドはラップされた文字グループをリストにして返す. ex, `['This function returns the answer as STRING and not', 'LIST.']`

## uWSGI
- [わかりやすい記事](https://www.python.ambitious-engineer.com/archives/1959)
- ([ついでにflask入門編も楽しそう. ](https://www.python.ambitious-engineer.com/archives/1630))
- uWSGI: PythonでWebサービスを動かすための**アプリケーションサーバ**(**APサーバー**)の一種. WSGIに則ったアプリケーションを動作させるアプリケーションサーバを**WSGIアプリケーションコンテナ**や**WSGIサーバ**などと呼ぶ. uWSGIはこのWSGIアプリケーションコンテナの一種. つまり, WSGIに準拠したアプリケーションであれば, DjangoやFlask以外でも動かすことができる. WSGIサーバーにはuWSGI以外にGunicornがある.
- uWSGIは動作させたアプリケーションと**Webサーバー(ApacheやNginx)**とをUNIXドメインソケット, またはHTTPで通信させる. WebサーバーはクライアントとHTTPで通信.
- **静的ファイルがないAPI**の場合はWebサーバーを経由せずに、直接クライアントと通信するのも一つの手.
- uWSGI をファイル実行する場合は `$ uwsgi uwsgi.ini`

## gunicorn + nginx
- gunicorn 起動 `gunicorn app:app -c $(pwd)/gunicorn/config/gunicorn_settings.py`
- nginx 起動 `nginx -c $(pwd)/gunicorn/config/nginx.conf`
- nginx 停止 `nginx -s stop`
- nginx 起動確認 `ps aux | grep nginx`  `ps -ax | grep nginx`
- nigix ポートの確認 `lsof -i -P | grep nginx`

## なぜ, webサーバとアプリケーションサーバを分けるのか.
- つてはWebサーバとアプリケーションサーバの分割はされていなかった. この構成が問題となったのは、インターネットの普及に伴い、一般公開しているサービスに対するアクセス数が増えたことでサーバへの負荷が高まり、全体的にパフォーマンスが落ちるという自体に直面したときだった.
そこで、負荷を分散させることで安定稼働することを目指し、役割に応じてサーバを分割する流れになった. この思想が現代においては当たり前で、一般的にWebサービスは**Webサーバ<-->アプリケーションサーバ<-->DBサーバと**いう三層構造で作られている. 
- リバースプロキシの用途: セキュリティーの強化, 不可分散（ロードバランサ）、コンテンツをキャッシュ化するなどによる高速化.
- [わかりやすい記事参照こちら.] (https://qiita.com/mintak21/items/eeba4654a0db21abcb1c)