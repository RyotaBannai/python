# coding= utf-8

class Server(object):
  def __init__(self):
    self.messages = []
  
  def __call__(self, environ, start_response):
    method = environ['REQUEST_METHOD']
    if method == 'GET':
      return self.sayHi(environ, start_response)
    else:
      start_response('501 NotImplemented', [('Content-type', 'text/plain')])
      return '501 NotImplemented'
  
  def sayHi(self, environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])	
    return ['Hello, world!'.encode("utf-8")]

from wsgiref import simple_server

if __name__ == '__main__':
	with simple_server.make_server('', 8080, Server()) as httpd:
		httpd.serve_forever()
