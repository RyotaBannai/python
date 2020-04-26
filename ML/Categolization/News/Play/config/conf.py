import os
import pathlib
NEOLOGD_DIR = '/usr/local/lib/mecab/dic/mecab-ipadic-neologd'
PACKAGE_DIR = pathlib.Path(os.path.dirname(__file__)).parents[0]
DATA_DIR = PACKAGE_DIR / 'data/csv'
TOKEN_DIR = PACKAGE_DIR / 'data/token/csv'
TFIDF_DIR = PACKAGE_DIR / 'data/tfidf'
#CATEGORIES = ['社会', '国際総合']
MINIMUM_TOKEN_LENGTH = 50
PCA_DIMENSION = 100
PCA_BATCH_DATA_LENGTH = 50

