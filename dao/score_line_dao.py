import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='zbn123ZBN456', db='metacritic')
cursor = conn.cursor()


def get_list_dates_and_scores_by_publisher_names(names):
    format_names = " OR ".join(f"p.name LIKE '%{x}%'" for x in names)
    sql = '''
        SELECT p.name, g.metascore, g.date
        FROM game g JOIN publisher p on p.id = g.publisher_id
        WHERE {condition}
        ORDER BY g.date
    '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_list_dates_and_scores_by_platform_names(names):
    format_names = " OR ".join(f"p.name LIKE '%{x}%'" for x in names)
    sql = '''
            SELECT p.name, g.metascore, g.date
            FROM game g JOIN platform p on p.id = g.platform_id
            WHERE {condition}
            ORDER BY g.date
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_list_dates_and_scores_by_game_names(names):
    format_names = " OR ".join(f"name LIKE '%{x}%'" for x in names)
    sql = '''
            SELECT name, metascore, date
            FROM game 
            WHERE {condition}
            ORDER BY date
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()
