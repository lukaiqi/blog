import pymysql


class Danmu():
    def search(self, nn):
        conn = pymysql.connect('47.106.69.171', 'root', 'mysql', 'xiaojie', charset='utf8')
        cursor = conn.cursor()
        sql = 'select * from danmu where nickname = "%s"' % (nn)
        cursor.execute(sql)
        conn.commit()
        res = cursor.fetchall()
        return list(res)


if __name__ == '__main__':
    dm = Danmu()
    dm.search('卡了个卡')
