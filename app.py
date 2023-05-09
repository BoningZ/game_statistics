from flask import Flask, request, render_template

import service.wordcloud_service as wordcloud_service
import service.count_bar_service as bar_service
import service.count_pie_service as pie_service
import service.score_box_service as box_service
import service.score_line_service as line_service
import service.score_scatter_service as scatter_service
import util.input_util as input_util

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    value = request.form['input']
    button = request.form['button']
    plot_url = None
    if button == 'cloud_score_range':
        n1, n2 = input_util.to_two_num(value)
        plot_url = wordcloud_service.get_wordcloud_by_score_range(n1, n2)
    elif button == 'cloud_media_name':
        plot_url = wordcloud_service.get_wordcloud_by_media_name(value)
    elif button == 'cloud_game_name':
        plot_url = wordcloud_service.get_wordcloud_by_game_name_like(value)
    elif button == 'cloud_publisher_name':
        plot_url = wordcloud_service.get_wordcloud_by_publisher_name_like(value)

    elif button == 'bar_platform_name':
        plot_url = bar_service.get_counts_and_years_by_platform_names(value.split(","))
    elif button == 'bar_rating':
        plot_url = bar_service.get_counts_and_years_by_all_ratings()
    elif button == 'bar_publisher_name':
        plot_url = bar_service.get_counts_and_years_by_publisher_names(value.split(","))
    elif button == 'bar_genre':
        n1, n2 = input_util.to_two_num(value)
        plot_url = bar_service.get_counts_and_years_by_genre_range(n1, n2)

    elif button == 'pie_platform_name':
        plot_url = pie_service.get_ratio_counts_and_ratings_by_platform_names(value.split(","))
    elif button == 'pie_publisher_name':
        plot_url = pie_service.get_counts_and_ratings_by_publisher_names(value.split(","))
    elif button == 'pie_cast':
        n1, n2 = input_util.to_two_num(value)
        plot_url = pie_service.get_counts_and_ratings_by_casts_range(n1, n2)

    elif button == 'box_rating':
        plot_url = box_service.get_list_ratings_and_scores()
    elif button == 'box_descriptor':
        plot_url = box_service.get_descriptors_and_scores()
    elif button == 'box_media':
        n1, n2 = input_util.to_two_num(value)
        plot_url = box_service.get_list_media_names_and_scores_by_count_range(n1, n2)
    elif button == 'box_game_name':
        plot_url = box_service.get_list_game_names_and_scores_like_name(value)
    elif button == 'box_most_commented':
        n1, n2 = input_util.to_two_num(value)
        plot_url = box_service.get_list_game_names_and_scores_by_count_range(n1, n2)
    elif button == 'box_max_score':
        n1, n2 = input_util.to_two_num(value)
        plot_url = box_service.get_list_game_names_and_scores_by_average_score_range(n1, n2)

    elif button == 'line_platform_name':
        plot_url = line_service.get_list_dates_and_scores_by_platform_names(value.split(","))
    elif button == 'line_publisher_name':
        plot_url = line_service.get_list_dates_and_scores_by_publisher_names(value.split(","))
    elif button == 'line_game_name':
        plot_url = line_service.get_list_dates_and_scores_by_game_names(value.split(","))

    elif button == 'scatter_platform_name':
        plot_url = scatter_service.get_metascores_and_userscores_by_platform_names(value.split(","))
    elif button == 'scatter_publisher_name':
        plot_url = scatter_service.get_metascores_and_userscores_by_publisher_names(value.split(","))
    elif button == 'scatter_game_name':
        plot_url = scatter_service.get_metascores_and_userscores_by_game_names(value.split(","))

    return render_template('index.html', plot_url=plot_url)


if __name__ == '__main__':
    app.run()
