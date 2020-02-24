# coding= utf-8

#>>> instance = someclass() # __call__ メソッドを持ったsomeclass 
#>>> instance(argument)     # instance.__call__(argument) と等価な処理

import datetime, io #, cgi
import urllib.parse
from xml.sax import saxutils
from wsgiref import simple_server, util


#ミドルウェアを使用すれば, もっと再利用性のある__call__を実装をすることができる.

class Server(object):
	def __init__(self):
		self.messages = []
		
	#self: Pythonでは, C++やRubyなどと違い, 呼び出し元インスタンスを明示的に引数として取る
	def __call__(self, environ, start_response):
		method = environ['REQUEST_METHOD']
		if method == 'GET':
			return self.listMessages(environ, start_response)
		elif method == 'POST':
			return self.addMessage(environ, start_response)
		else:
			start_response('501 NotImplemented', [('Content-type', 'text/plain')])
			return '501 NotImplemented'
			
	def addMessage(self, environ, start_response):
		inpt = environ['wsgi.input']
		length = int(environ.get('CONTENT_LENGTH', 0))
		
		#取得したデータをパースして辞書オブジェクトに変換
		#wsgi.inputの読み込みの長さを指定しないと、read関数の呼び出しが終わらず、実行がブロックされてしまうので注意.
		
		#postされたデータのパースには、cgiモジュールのparse_qsl, parse_qsを使う. -> cgi module is deprecated from python3.2 or older
		#query = dict(cgi.parse_qs(inpt.read(length))) #dict([(key, value), (key, value)])
		query = dict(urllib.parse.parse_qs(inpt.read(length))) #dict([(key, value), (key, value)])
		tmp = {}
		for k, v in query.items():
			#print(k, v)
			tmp[k.decode('utf-8')] = v[0].decode('utf-8')
		query = tmp
		msg = {
			'name': query['name'],
			'title': query['title'],
			'body': query['body'],
			'date': datetime.datetime.now()}
		self.messages.append(msg)
		
		# Redirect
		# 直接listMessagesを呼び出してもいいが、その場合、書き込んだ後にリロードすると、二重で書き込みをしてしまうため、redirectの方がいい.
		start_response('303 See Other', [
			('Content-type', 'text/plain'), 
			('Location', util.request_uri(environ))])
		
		return ''

	def	listMessages(self, environ, start_response):
		#レスポンス本文の生成には、StringIOクラスを利用.
		#StringIO: メモリ上のバッファに対してファイルオブジェクトのような入出力操作を提供するオブエクト.このStringIOに, レスポンスとしてHTMLをwriteメソッドを使用して書き出していく.
		fp = io.BytesIO()
		head = r'''<html>
<head><title>Message Board</title>
<meta http-equiv="Content-type" content="text/html; charset=utf-8">
</head>
<body>
'''
		fp.write(head.encode('utf-8'))
		for msg in reversed(self.messages):
		
			esc = saxutils.escape #投稿内容にあるHTMLタグを無効化. XSS対策.
			tmp={}
			for key, value in msg.items():
				value = str(value)
				tmp[key] = str(esc(value))
				print(key, str(esc(value)))
			data = '''<dl>
<dt>title</dt>
<dd>{title}</dd>
<dt>name</dt>
<dd>{name}</dd>
<dt>date</dt>
<dd>{date}</dd>
<dt>message</dt>
<dd>{body}</dd>
</dl><hr />'''.format(**tmp)
			fp.write(data.encode('utf-8'))

		data = '''<form action="{}" method="POST" AcceptEncoding="utf-8">
<dl>
<dt>name</dt>
<dd><input type="text" name="name"/></dd>
<dt>title</dt>
<dd><input type="text" name="title"/></dd>
<dt>body</dt>
<dd><textarea name="body"></textarea></dd>
</dl>
<input type="submit" name="save" value="Post" />
</form>
</body></html>'''.format(util.request_uri(environ))
		fp.write(data.encode('utf-8'))
		
		#シークの位置を先頭にしておく
		fp.seek(0)

		start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
		return fp 
		# ファイルオブジェクト同様、StringIOもiterable なので, WSGIappの返り値をして利用可能. ただし, write()で文字列を出力した後は、バッファの読み出し位置が変わってしまうため、seekメソッドで読み出し位置を先頭に設定した後で返り値として使用する.

if __name__ == '__main__':
	server = simple_server.make_server('', 8080, Server())
	server.serve_forever()