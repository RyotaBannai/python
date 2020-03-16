from collections import Counter
import contextlib

if __name__ == "__main__":
    mylist = ['apple', 'microsoft', 'google', 'apple']
    myfreq_mentioned_words = Counter(mylist)
    print(myfreq_mentioned_words)
    to_dict = myfreq_mentioned_words.items()
    print(to_dict)
    # 記事に出現する単語の頻度を大きい順に並べるなどの処理に向いている.
