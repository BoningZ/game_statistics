import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='zbn123ZBN456', db='metacritic')
cursor = conn.cursor()


def get_counts_and_ratings_by_platform_names(names):
    format_names = "(" + " OR ".join(f"p.name LIKE '%{x}%'" for x in names) + ")"
    sql = '''
            SELECT p.name, g.rating, COUNT(*)
            FROM game g JOIN platform p on p.id = g.platform_id
            WHERE {condition} AND g.rating IS NOT NULL 
            GROUP BY g.rating, p.name
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_counts_and_ratings_by_publisher_names(names):
    format_names = "(" + " OR ".join(f"p.name LIKE '%{x}%'" for x in names) + ")"
    sql = '''
            SELECT p.name, g.rating, COUNT(*)
            FROM game g JOIN publisher p on p.id = g.publisher_id
            WHERE {condition} AND g.rating IS NOT NULL 
            GROUP BY g.rating, p.name
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_counts_and_ratings_by_casts_range(btm, cnt):
    sql = '''            
            WITH top_casts AS (
                SELECT cast_id
                FROM game_cast
                GROUP BY cast_id
                ORDER BY COUNT(*) DESC
                LIMIT %s,%s   
            )
            SELECT c.name, g.rating, COUNT(*)
            FROM game g 
                JOIN game_cast gc on g.id = gc.game_id
                JOIN cast c on c.id = gc.cast_id
            WHERE g.rating IS NOT NULL AND c.id IN (SELECT * from top_casts)
            GROUP BY g.rating, c.name
            '''
    cursor.execute(sql, (btm, cnt))
    return cursor.fetchall()
