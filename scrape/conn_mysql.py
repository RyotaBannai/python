import pymysql


class db(object):
    def __init__(self):
        self.value = None

    def __enter__(self):
        self.conn = pymysql.connect(
            host='localhost', unix_socket='/tmp/mysql.sock', user='ryota', passwd='bannai', db='mysql')
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, type, value, traceback):
        """
        If the context was exited without an exception, all three arguments will be None.
        value is an Exception instance.
        and, presumably traceback is a Python traceback object.
        """
        self.cur.close()
        self.conn.close()
        print('connection closed... avoiding connection leak')

    def __del__(self):
        """
        destructor: called when deleted.
        for example, when using class instance with With statement, exiting it __del__ method will be called.
        and as another example, when using del method like, del db 
        """
        print('db object is deleted for safety.')


if __name__ == "__main__":
    with db() as cur:
        cur.execute('USE scraping')
        cur.execute('SELECT * FROM pages WHERE id=1')
        print(cur.fetchone())
