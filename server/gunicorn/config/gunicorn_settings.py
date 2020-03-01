import os
from pathlib import PurePath

# nginx との接続ホスト及ポート
bind = '127.0.0.1:' + str(os.getenv('PORT', 9877))
proc_name = 'Infrastructure-Practice-Flask'
workers = 1

topdir = PurePath(os.path.dirname(__file__)).parent
# accesslog = '-' 標準出力の場合.
accesslog = str(topdir / 'logs/gunicorn_access.log')
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s'"

# daemon = True
# limit_request_line = 4049 DDos対策

# config fileから相対パスで, appと同dirを読み込み先として指定してしまえば便利.
chdir = str(topdir)

def on_starting(server):
	"""
	called just before the master process is initialized.
	"""
	print('gunicorn is running...')