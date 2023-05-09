import dao.count_bar_dao as count_bar_dao
import util.draw_util as draw_util


def get_counts_and_years_by_platform_names(names):
    data = count_bar_dao.get_counts_and_years_by_platform_names(names)
    return draw_util.draw_year_label_bars(data, 'Number of Games Released by Year and Platform')


def get_counts_and_years_by_all_ratings():
    data = count_bar_dao.get_counts_and_years_by_all_ratings()
    return draw_util.draw_year_label_bars(data, 'Number of Games Released by Year and Rating')


def get_counts_and_years_by_publisher_names(names):
    data = count_bar_dao.get_counts_and_years_by_publisher_names(names)
    return draw_util.draw_year_label_bars(data, 'Number of Games Released by Year and Publisher')


def get_counts_and_years_by_genre_range(btm, cnt):
    data = count_bar_dao.get_counts_and_years_by_genre_range(btm, cnt)
    return draw_util.draw_year_label_bars(data, 'Number of Games Released by Year and Genre')
