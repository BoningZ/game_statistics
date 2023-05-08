import service.score_scatter_service as score_scatter_service

if __name__ == '__main__':
    # score_scatter_service.get_metascores_and_userscores_by_publisher_names(["Nintendo", "Sega", "Capcom"])
    # score_scatter_service.get_metascores_and_userscores_by_platform_names(["PlayStation 5", "Xbox Series"])
    score_scatter_service.get_metascores_and_userscores_by_game_names(["Zelda", "Final Fantasy"])
