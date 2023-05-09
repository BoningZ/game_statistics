import dao.score_box_dao as game_dao
import util.draw_util as draw_util


def get_list_game_names_and_scores_by_count_range(btm, cnt):
    data = game_dao.get_list_game_names_and_scores_by_count_range(btm, cnt)
    draw_util.draw_score_box(data, 'Distribution of Metascore', "Game Name")


def get_list_game_names_and_scores_like_name(name):
    data = game_dao.get_list_game_names_and_scores_like_name(name)
    draw_util.draw_score_box(data, 'Distribution of Metascore', "Game Name")


def get_list_media_names_and_scores_by_count_range(btm, cnt):
    data = game_dao.get_list_media_names_and_scores_by_count_range(btm, cnt)
    draw_util.draw_score_box(data, 'Distribution of Metascore', "Media Name")


def get_list_ratings_and_scores():
    data = game_dao.get_list_ratings_and_scores()
    draw_util.draw_score_box(data, 'Distribution of Metascore', "Rating")


def get_list_media_names_and_scores_by_average_score_range(btm, cnt):
    data = game_dao.get_list_media_names_and_scores_by_average_score_range(btm, cnt)
    draw_util.draw_score_box(data, 'Distribution of Metascore', "Game Name")


def get_descriptors_and_scores():
    data = game_dao.get_descriptors_and_scores()
    draw_util.draw_score_box(data, 'Distribution of Metascore', "Descriptor")
