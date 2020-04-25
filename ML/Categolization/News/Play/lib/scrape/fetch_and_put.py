import csv
import json
import os
from datetime import datetime as dt, timedelta as td
from pprint import pprint as pp

from lib.workers.yahoo import Scraper, RSSScraper


def fetch_news(rss_dic, time, filetype):
    chunk_dic = scrape(rss_dic, time)
    for k, v in chunk_dic.items():
        timestr = time.strftime('%Y-%m-%d')
        targetdir = '../../data/{0}/{1}'.format(filetype, k)
        if not os.path.isdir(targetdir):
            os.makedirs(targetdir)

        filename = '{0}/{1}_{2}.{3}'.format(targetdir, k, timestr, filetype)
        write_news_file(filename, v, filetype)


def scrape(rss_dic, time, oneline=True) -> list:
    scraper = Scraper()
    chunk_dic = {}
    for rss_url in rss_dic.values():
        result = scraper.scrape_news(rss_url, sleep=1, date=time, oneline=oneline)
        #print("url is:", rss_url)
        #pp(result)
        for k, v in result.items():
            if k in chunk_dic:
                chunk_dic[k].extend(v)
            else:
                chunk_dic[k] = v
        #pp(chunk_dic)

    return chunk_dic


def write_news_file(filename, chunks, filetype):
    if filetype == 'json':
        if not os.path.isfile(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

        # あまり賢いやり方ではないが、せいぜい数回なのでこのやり方で我慢
        with open(filename, 'r', encoding='utf-8') as f:
            feeds = json.load(f)

        with open(filename, 'w', encoding='utf-8') as f:
            feeds.extend(chunks)
            json.dump(feeds, f, ensure_ascii=False)

    elif filetype == 'csv':
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f,  lineterminator='\n')
            for chunk in chunks:
                writer.writerow([chunk['category'], chunk['title'],
                                 chunk['text_len'], chunk['text']])


def main(time, filetype):
    rss = RSSScraper()

    jp = rss.scrape_jp_newslist()
    print(jp)
    jp = {'47NEWS': 'https://headlines.yahoo.co.jp/rss/yonnana-dom.xml',
          'ABCテレビ': 'https://headlines.yahoo.co.jp/rss/asahibc-dom.xml',
          }
    fetch_news(jp, time, filetype) #time よりあとの記事を取得

if __name__ == '__main__':
    main(dt.now()-td(days=7), 'csv')