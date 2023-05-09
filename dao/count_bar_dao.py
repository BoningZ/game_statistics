import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='zbn123ZBN456', db='metacritic')
cursor = conn.cursor()


def get_counts_and_years_by_platform_names(names):
    format_names = " OR ".join(f"p.name LIKE '%{x}%'" for x in names)
    sql = '''
            SELECT YEAR(g.date), p.name, COUNT(*)
            FROM game g JOIN platform p on p.id = g.platform_id
            WHERE {condition}
            GROUP BY YEAR(g.date), p.name
            ORDER BY g.date
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_counts_and_years_by_all_ratings():
    sql = '''
            SELECT YEAR(date), rating, COUNT(*)
            FROM game
            WHERE rating IS NOT NULL
            GROUP BY rating, YEAR(date)
            ORDER BY date
        '''
    cursor.execute(sql)
    return cursor.fetchall()


def get_counts_and_years_by_publisher_names(names):
    format_names = " OR ".join(f"p.name LIKE '%{x}%'" for x in names)
    sql = '''
            SELECT YEAR(g.date), p.name, COUNT(*)
            FROM game g JOIN publisher p on p.id = g.publisher_id
            WHERE {condition}
            GROUP BY YEAR(g.date), p.name
            ORDER BY g.date
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_counts_and_years_by_genre_range(btm=0, cnt=9):
    sql = '''
            WITH top_genre AS (
                SELECT genre_id
                FROM game_genre
                GROUP BY genre_id
                ORDER BY COUNT(*) DESC
                LIMIT %s,%s   
            )
            SELECT YEAR(g.date), genre.name, COUNT(*)
            FROM game g
                JOIN game_genre gg ON g.id = gg.game_id
                JOIN genre ON genre.id = gg.genre_id
            WHERE genre.id IN (SELECT * FROM top_genre)
            GROUP BY YEAR(g.date), genre.name
            ORDER BY g.date
        '''
    cursor.execute(sql, (btm, cnt))
    return cursor.fetchall()
