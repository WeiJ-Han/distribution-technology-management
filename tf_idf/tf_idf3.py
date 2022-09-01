import jieba.analyse
news = open("news.txt","r",encoding="utf-8").read()
tags = jieba.analyse.extract_tags(news, topK=5, withWeight=True)

for tag in tags:
    print('word:', tag[0], 'tf-idf:', tag[1])