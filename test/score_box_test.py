import matplotlib.pyplot as plt
import seaborn as sns

import service.score_box_service as game_score_service

if __name__ == '__main__':
    df = game_score_service.get_descriptors_and_scores()
    # df = game_score_service.get_list_ratings_and_scores()
    # df = game_score_service.get_list_media_names_and_scores_top_count(50)
    # df = game_score_service.get_list_game_names_and_scores_like_name('RESIDENT EVIL')
    # df = game_score_service.get_list_game_names_and_scores_top_count(30)
    sns.set(style='ticks')
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.boxplot(data=df, x='name', y='score', ax=ax)
    ax.set_title('Distribution of Game Ratings')
    ax.set_xlabel('Game Name')
    ax.set_ylabel('Score')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.tick_params(axis='x', labelsize=8)
    sns.despine(trim=True)
    plt.tight_layout()
    plt.show()
