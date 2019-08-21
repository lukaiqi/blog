import pymysql

conn = pymysql.connect('47.106.69.171', 'root', 'mysql', 'xiaojie', charset='utf8')
cursor = conn.cursor()


class Danmu():
    def search(self, nn):
        sql = 'select * from danmu where nickname = "%s"' % (nn)
        cursor.execute(sql)
        conn.commit()
        res = cursor.fetchall()
        return list(res)


if __name__ == '__main__':
    dm = Danmu()
    dm.search('卡了个卡')
