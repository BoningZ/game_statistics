import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='zbn123ZBN456', db='metacritic')
cursor = conn.cursor()


def get_metascores_and_userscores_by_publisher_names(names):
    format_names = " OR ".join(f"p.name LIKE '%{x}%'" for x in names)
    sql = '''
            SELECT p.name, g.metascore, g.userscore
            FROM game g JOIN publisher p on p.id = g.publisher_id
            WHERE {condition} AND g.metascore IS NOT NULL AND g.userscore IS NOT NULL
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_metascores_and_userscores_by_platform_names(names):
    format_names = " OR ".join(f"p.name LIKE '%{x}%'" for x in names)
    sql = '''
            SELECT p.name, g.metascore, g.userscore
            FROM game g JOIN platform p on p.id = g.platform_id
            WHERE {condition} AND g.metascore IS NOT NULL AND g.userscore IS NOT NULL
        '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()


def get_metascores_and_userscores_by_game_names(names):
    format_names = " OR ".join(f"name LIKE '%{x}%'" for x in names)
    sql = '''
                SELECT name, metascore, userscore
                FROM game 
                WHERE {condition} AND metascore IS NOT NULL AND userscore IS NOT NULL
            '''.format(condition=format_names)
    cursor.execute(sql)
    return cursor.fetchall()
