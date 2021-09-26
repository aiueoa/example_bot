"""
user発話とsys発話を格納しているデータから形態素解析したものも作成する。
"""
from os import listdir, path
import pandas as pd
import MeCab
mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
df = pd.read_csv('data/pattern_text.csv')
inputs = df['usr'].values

def split_text(text):
    sentence = mecab.parse(text).split("\n")
    words = []
    for w in sentence:
        if w == 'EOS':
            result = "".join(l + ' ' for l in words)[:-1]
            return result
        cols = w.split('\t')
        words.append(cols[0])
    result = ''.join(l + ' ' for l in words)[:-1]
    return result

results = []
for text in inputs:
    results.append(split_text(text))
df2 = pd.DataFrame(results, columns=['split_input'])
df_concat = pd.concat([df, df2], axis=1)

df_concat.to_csv('data/split_data.csv')