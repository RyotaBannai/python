# -*- coding: utf-8 -*-
class UnhashableInFact(object):
    def __init__(self, n):
        self.n = n

    def __hash__(self):
        return hash(self.n)

    def __eq__(self, other):
        return self.n == other.n

class Unhashable(object):
    __hash__ = None

    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return self.n == other.n

if __name__ == '__main__':
    a = UnhashableInFact(1)
    b = UnhashableInFact(2)
    mydict = {a: "value for 1", b: "value for 2"}
    print(mydict[a], mydict[b]) # (1) それぞれのバケツから値を取り出せる
    a.n = 2                     # -> ハッシュ値が変わる
    print(mydict[a], mydict[b]) # (2)
    c = UnhashableInFact(1)
    print(c in mydict)          # (3) 元のキーと等しいものを持ってきても "value for 1" が取り出せない
                                # -> hashable であれば、このようなことは起きない.  hashable -> int, frozenset, str, tuple

    # unhashable を明示的にunhashable にするには __hash__を Noneと設定することで, TypeError が送出
    d = Unhashable(1)
    # {d: "value for 1"} # >>> TypeError: unhashable type: 'Unhashable'
    """
    Python3 では、__eq__ をオーバーライドすると勝手に None にしてくれる。
    __eq__() をオーバーライドしていて __hash__() を定義していないクラスは、
    暗黙的に None に設定された __hash__() を持つ. -> つまり、__hash__ == None すら必要ない。
    
    クラスの __hash__() メソッドが　None の場合、そのクラスのインスタンスのハッシュ値を取得しようとすると
    適切なTypeError が送出され, isinstance(obj, collections.Hashable) をチェック すると
    ハッシュ不能なものとして正しく認識される.
    """

    # immutable and hashable
    """
    immutable の使いどころとして、
    辞書におけるキーが挙げられている。
    """