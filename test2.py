from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt


with open('a.txt', 'r', encoding='utf-8') as f:
    text = f.read()

okt = Okt()
nouns = okt.nouns(text)

words = [n for n in nouns if len(n) > 1]

c = Counter(words)

wc = WordCloud(font_path='/Users/caelis/Library/Fonts/MaruBuri-Regular.ttf', width=400, height=400, scale=2.0, max_font_size=250,).generate_from_frequencies(c) 
# font_path='/Library/Fonts/Menlo.ttc'
# family="AppleGothic"
wc.to_file('./static/아어오.jpg')
# plt.figure(figsize = (6, 6)) # 최종 워드 클라우드 사이즈 지정
# a = plt.imshow(wc)
plt.axis('off') # 그래프 축 제거