# coding= utf-8

#environ: Webブラウザなどのクライアントから送られたリクエストの情報など
#start_response: この二つの引数をは必須. 1. status code, 2. http response head
#return: 反復可能なオブジェクト(iterable object)を返さなければならない.
#そして反復した結果として、文字列オブジェクトを返さなければならない.
	
#iterable object: 反復可能（iterable）なオブジェクトとは, 「for n in x:」というfor文の
#x の部分に使用できるオブジェクトで, __iter__ というメソッドを持っているもの.
#反復可能なオブジェクトは,リスト,タプル,辞書,文字列など.
#また,ユーザ定義のクラスであっても, __iter__ メソッドを定義することで, #iterableオブジェクトにすることができる.

def serve(environ, start_response):
	
	start_response('200 OK', [('Content-type', 'text/plain')])	
	return ['Hello, world!'.encode("utf-8")]

from wsgiref import simple_server

if __name__ == '__main__':
	with simple_server.make_server('', 8080, serve) as httpd:
		httpd.serve_forever()