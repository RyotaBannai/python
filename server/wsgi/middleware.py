# coding= utf-8

import app
from wsgiref import simple_server, util


def notFound(environ, start_response):

  start_response('404 NotFound', [('Content-type', 'text/plain')])

  return '%s is not found' % util.request_uri(environ)

class SelectApp(object):
  def __init__(self, table, notFound=notFound):
    tmp = sorted(table, key=lambda x: len(x), reverse=True)
    table = [(x, table[x]) for x in tmp]

    self.table = table
    self.notfound = notFound
    
  def __call__(self, environ, start_response):
    
    name = 'SCRIPT_NAME'
    info = 'PATH_INFO'
    
    # SCRIPT_NAME : URL上でアプリケーションのルートがどの位置にあるかを表す. たとえば，http://localhost/app/pathにあるならば, SCRIPT_NAME は "/app/path" 
    # PATH_INFO : アプリケーション上の仮想的な URL を表す. http://localhost/app/pathがアプリケーションのある位置で, http://localhost/app/path/extraとアクセスした場合，PATH_INFOには"/extra"

    scriptname = environ.get(name, '')
    pathinfo = environ.get(info, '')

    for p, app in self.table:

      if p == '' or p == '/' and pathinfo.startswith(p):
        return app(environ, start_response)

      # 同じパスならそのまま
      # 同じパスで始まっていて、その後にスラッシュがある
      if pathinfo == p or pathinfo.startswith(p) and pathinfo[len(p)] == '/':

        '''
        判定で一致した場合は, PATH_INFOの先頭からlen(p)分だけ文字を取り除き, SCRIPT_NAMEの末尾にpをそのまま加えて, environ辞書を更新したうえでアプリケーションを呼び出す.
        こうしておくことで, SelectAppを再帰的に適用して振り分けを行うことできる.
        '''
        scriptname = scriptname + p
        pathinfo = pathinfo[len(p):]

        # リクエスト情報を書き換える
        environ[name] = scriptname
        environ[info] = pathinfo

        return app(environ, start_response)

if __name__ == "__main__":

  import app, wsgi2
  # /message に MessageBoard を、 /hello に Hello, world を割り当て
  table = {
    '/message': app.Server(), 
    '/hello': wsgi2.Server()
    }
  application = SelectApp(table)
  server = simple_server.make_server('', 8080, application)
  server.serve_forever()