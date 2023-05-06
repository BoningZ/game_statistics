import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

import dao.review_dao as review_dao

stopwords = set(STOPWORDS)
with open('..\\service\\stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords.update([line.strip() for line in f])


def get_wordcloud_by_score_range(btm, top):
    data = review_dao.get_list_review_bodies_by_score_range(btm, top)
    text = " ".join(review[0] for review in data)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000).generate(text)
    return wordcloud


def get_wordcloud_by_game_name_like(name):
    data = review_dao.get_list_review_bodies_by_game_name_like(name)
    text = " ".join(review[0] for review in data)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000).generate(text)
    return wordcloud


def get_wordcloud_by_publisher_name_like(name):
    data = review_dao.get_list_review_bodies_by_publisher_name_like(name)
    text = " ".join(review[0] for review in data)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=1000).generate(text)
    return wordcloud
