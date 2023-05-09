import service.wordcloud_service as wordcloud_service

if __name__ == '__main__':
    wordcloud_service.get_wordcloud_by_score_range(0, 100)
    # wordcloud_service.get_wordcloud_by_game_name_like("CREED")
    # wordcloud_service.get_wordcloud_by_publisher_name_like("Origin")
    # wordcloud_service.get_wordcloud_by_media_name("IGN")

