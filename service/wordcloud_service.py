import dao.review_dao as review_dao
import util.draw_util as draw_util


def get_wordcloud_by_score_range(btm, top):
    data = review_dao.get_list_review_bodies_by_score_range(btm, top)
    return draw_util.draw_word_cloud(data)


def get_wordcloud_by_game_name_like(name):
    data = review_dao.get_list_review_bodies_by_game_name_like(name)
    return draw_util.draw_word_cloud(data)


def get_wordcloud_by_publisher_name_like(name):
    data = review_dao.get_list_review_bodies_by_publisher_name_like(name)
    return draw_util.draw_word_cloud(data)


def get_wordcloud_by_media_name(name):
    data = review_dao.get_list_review_bodies_by_media_name(name)
    return draw_util.draw_word_cloud(data)
