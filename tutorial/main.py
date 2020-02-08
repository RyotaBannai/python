def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# if __name__ == "__main__": を挿入すると, このファイルが import できるモジュールであると同時にスクリプトとしても使えるようになる. なぜならモジュールが "main" ファイルとして起動されたときだけ、コマンドラインを解釈するコードが実行されるからです. コマンドライン からこのファイルを実行すると, __name__ に __main__が設定される.

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))