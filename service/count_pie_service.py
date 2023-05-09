import dao.count_pie_dao as count_pie_dao
import util.draw_util as draw_util


def get_ratio_counts_and_ratings_by_platform_names(names):
    data = count_pie_dao.get_counts_and_ratings_by_platform_names(names)
    draw_util.draw_count_pie(data, "Platform Ratings")


def get_counts_and_ratings_by_publisher_names(names):
    data = count_pie_dao.get_counts_and_ratings_by_publisher_names(names)
    draw_util.draw_count_pie(data, "Publisher Ratings")


def get_counts_and_ratings_by_casts_range(btm, cnt):
    data = count_pie_dao.get_counts_and_ratings_by_casts_range(btm, cnt)
    draw_util.draw_count_pie(data, "Cast Ratings")
