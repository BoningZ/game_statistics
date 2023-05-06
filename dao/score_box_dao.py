import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='zbn123ZBN456', db='metacritic')
cursor = conn.cursor()


def get_list_game_names_and_scores_top_count(count):
    sql = '''
        WITH top AS (
            SELECT game_id FROM review
            GROUP BY game_id
            ORDER BY COUNT(*) DESC
            LIMIT %s
        )
        SELECT game.name, review.score
        FROM game JOIN review ON game.id = review.game_id
        WHERE game.id IN (SELECT game_id FROM top)
    '''
    cursor.execute(sql, count)
    return cursor.fetchall()


def get_list_game_names_and_scores_like_name(name):
    sql = '''
        SELECT game.name, review.score
        FROM game JOIN review ON game.id = review.game_id
        WHERE game.name like %s
        ORDER BY game.date
    '''
    cursor.execute(sql, ('%' + name + '%'))
    return cursor.fetchall()


def get_list_media_names_and_scores_top_count(count):
    sql = '''
        WITH top AS (
            SELECT media_id FROM review
            GROUP BY media_id
            ORDER BY COUNT(*) DESC
            LIMIT %s
        )
        SELECT media.name, review.score
        FROM media JOIN review ON media.id = review.media_id
        WHERE media.id IN (SELECT media_id FROM top)
    '''
    cursor.execute(sql, count)
    return cursor.fetchall()


def get_list_ratings_and_scores():
    sql = '''
        SELECT game.rating, review.score
        FROM game JOIN review ON game.id = review.game_id
    '''
    cursor.execute(sql)
    return cursor.fetchall()


def get_descriptors_and_scores():
    sql = '''
        SELECT e.name, review.score
        FROM game 
        JOIN review ON game.id = review.game_id 
        JOIN game_esrb ge on game.id = ge.game_id
        JOIN esrb e on e.id = ge.esrb_id
    '''
    cursor.execute(sql)
    return cursor.fetchall()
