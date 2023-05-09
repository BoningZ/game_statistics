import service.count_pie_service as count_pie_service

if __name__ == '__main__':
    # count_pie_service.get_ratio_counts_and_ratings_by_platform_names(["switch"])
    # count_pie_service.get_counts_and_ratings_by_publisher_names(["Nintendo", "Capcom"])
    count_pie_service.get_counts_and_ratings_by_casts_range(0, 5)
