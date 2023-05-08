import dao.score_line_dao as score_line_dao
import util.draw_util as draw_util


def get_list_dates_and_scores_by_publisher_names(names):
    data = score_line_dao.get_list_dates_and_scores_by_publisher_names(names)
    draw_util.draw_score_date_line(data, 'Metascore over Time by Publishers')


def get_list_dates_and_scores_by_platform_names(names):
    data = score_line_dao.get_list_dates_and_scores_by_platform_names(names)
    draw_util.draw_score_date_line(data, 'Metascore over Time by Platforms')


def get_list_dates_and_scores_by_game_names(names):
    data = score_line_dao.get_list_dates_and_scores_by_game_names(names)
    data = list(data)
    for i in range(len(data)):
        datum = data[i]
        for name in names:
            if name.upper() in datum[0].upper():
                data[i] = (name, datum[1], datum[2])
    draw_util.draw_score_date_line(data, 'Metascore over Time by Series')
