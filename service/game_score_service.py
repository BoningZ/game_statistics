import dao.score_dao as game_dao


def get_list_game_names_and_scores_top_count(count=10):
    data = game_dao.get_list_game_names_and_scores_top_count(count)
    return {"name": [row[0] for row in data], "score": [row[1] for row in data]}


def get_list_game_names_and_scores_like_name(name):
    data = game_dao.get_list_game_names_and_scores_like_name(name)
    return {"name": [row[0] for row in data], "score": [row[1] for row in data]}
