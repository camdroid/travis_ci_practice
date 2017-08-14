def no():
    return False

def main():
    return True

def read_db():
    import pymysql
    db = pymysql.connect(host='localhost', user='travis', passwd='', db='test')
    cur = db.cursor()

    cur.execute('SELECT name FROM test')

    rows = cur.fetchall()
    return rows[0][0]

if __name__ == '__main__':
    main()
