import unittest

# How to call unittest
"""
by calling by module
1. python -m unittest test_module1 test_module2
2. python -m unittest test_module.TestClass
3. python -m unittest test_module.TestClass.test_method

or by file name
4. python -m unittest tests/test_something.py

options:
-f : stop unittest when the First error occures
-k : run unittest only ones contains specific name ex. -k foo => test_foo(): ...

test discovery mode:
python3 -m unittest discovery advanced_usage '*unittest.py' => unittest all with files contains unittest.py
"""
"""
ref:
1. https://kite.com/python/docs/unittest.TestLoader
2. https://docs.python.org/ja/3/library/unittest.html#assert-methods
"""


class TestStringMethods(unittest.TestCase):
    """
    test 対象はtest_ で始まる関数
    """

    def setUp(self):
        # print('TestStringMethods test class has been called...')
        self.s = 'hello world'

    @unittest.expectedFailure  # => OK (expected failures=1)
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FO0')

    def test_split(self):
        self.assertEqual(self.s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # 例外が発生する事を確認するために assertRaises() を呼び出す.
        self.assertCountEqual(self.s.split(), ['world', 'hello'])
        with self.assertRaises(TypeError):
            self.s.split(2)

    def tearDown(self):
        """
        テスト終了後の後始末. destructor のようなもの.
        """
        pass


class CreateHuman:
    def __init__(self) -> None:
        self.name = None
        self.level = 0

    def name_human(self, name: str):
        self.name = name

    def grow(self, nut: int):
        self.level += nut

    def eat(self, food: object):
        energy = food.nut
        self.grow(energy)


def makeSomething(name: str) -> CreateHuman:
    human = CreateHuman()
    human.name_human(name)
    return human


def testSomething():
    myName = 'Jack'
    something = makeSomething(myName)
    assert something.name is None


def makeSomethingDB():
    pass


def deleteSomethingDB():
    pass


def suite():
    """
    ある test suiteの特定のテストだけ集めて実行したい場合...

    """
    suite = unittest.TestSuite()
    # suite.addTest(TestStringMethods('test_upper'))
    suite.addTests([TestStringMethods('test_upper'),
                    TestStringMethods('test_split')])
    return suite


if __name__ == "__main__":

    # 作成したテストをまとめて実行 => test suite
    # これを細かく設定することもできる.

    # unittest.main()

    runner = unittest.TextTestRunner()
    runner.run(suite())

    # 既存のテスト関数をラップできる
    # testSomething()
    testcase = unittest.FunctionTestCase(testSomething,
                                         setUp=makeSomethingDB,
                                         tearDown=deleteSomethingDB)

    # runner.run(testcase)  # Ding ding!!
