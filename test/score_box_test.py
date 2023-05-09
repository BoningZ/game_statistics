import service.score_box_service as game_score_service

if __name__ == '__main__':
    # game_score_service.get_descriptors_and_scores()
    # game_score_service.get_list_ratings_and_scores()
    # game_score_service.get_list_media_names_and_scores_by_count_range(0, 50)
    # game_score_service.get_list_game_names_and_scores_like_name('RESIDENT EVIL')
    # game_score_service.get_list_game_names_and_scores_by_count_range(0, 30)
    game_score_service.get_list_media_names_and_scores_by_average_score_range(0, 50)
