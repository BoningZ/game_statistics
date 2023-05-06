import matplotlib.pyplot as plt

import service.wordcloud_service as wordcloud_service

if __name__ == '__main__':
    wordcloud = wordcloud_service.get_wordcloud_by_score_range(0, 100)
    # wordcloud = wordcloud_service.get_wordcloud_by_game_name_like("CREED")
    # wordcloud = wordcloud_service.get_wordcloud_by_publisher_name_like("Origin")
    # wordcloud = wordcloud_service.get_wordcloud_by_media_name("IGN")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
