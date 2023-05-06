import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='zbn123ZBN456', db='metacritic')
cursor = conn.cursor()


def get_list_review_bodies_by_score_range(btm, top):
    sql = "SELECT body FROM review where score>=%s and score<=%s"
    cursor.execute(sql, (btm, top))
    data = cursor.fetchall()
    return data


def get_list_review_bodies_by_media_name(name):
    sql = "SELECT body FROM review WHERE media_id IN (SELECT id FROM media WHERE name=%s)"
    cursor.execute(sql, name)
    data = cursor.fetchall()
    return data


def get_list_review_bodies_by_game_name_like(name):
    sql = "SELECT body FROM review WHERE game_id IN (SELECT id FROM game WHERE name LIKE %s)"
    cursor.execute(sql, ('%' + name + '%'))
    data = cursor.fetchall()
    return data


def get_list_review_bodies_by_publisher_name_like(name):
    sql = """
        SELECT body FROM review 
        WHERE game_id IN (
            SELECT id FROM game 
            WHERE publisher_id IN (
                SELECT id FROM publisher
                where name like %s
            )
        )
    """
    cursor.execute(sql, ('%' + name + '%'))
    data = cursor.fetchall()
    return data
