import dao.score_scatter_dao as score_scatter_dao
import util.draw_util as draw_util


def get_metascores_and_userscores_by_publisher_names(names):
    data = score_scatter_dao.get_metascores_and_userscores_by_publisher_names(names)
    return draw_util.draw_score_scatter(data, 'Media vs. User by Publishers')


def get_metascores_and_userscores_by_platform_names(names):
    data = score_scatter_dao.get_metascores_and_userscores_by_platform_names(names)
    return draw_util.draw_score_scatter(data, 'Media vs. User by Platforms')


def get_metascores_and_userscores_by_game_names(names):
    data = score_scatter_dao.get_metascores_and_userscores_by_game_names(names)
    data = list(data)
    for i in range(len(data)):
        datum = data[i]
        for name in names:
            if name.upper() in datum[0].upper():
                data[i] = (name, datum[1], datum[2])
    return draw_util.draw_score_scatter(data, 'Media vs. User by Series')
