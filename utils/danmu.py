import pymysql


class Danmu():
    def searchnn(self, keyword):
        conn = pymysql.connect('47.106.69.171', 'root', 'mysql', 'xiaojie', charset='utf8')
        cursor = conn.cursor()
        sql = 'select distinct nickname from danmu where instr (nickname,"%s")' % (keyword)
        cursor.execute(sql)
        conn.commit()
        res = cursor.fetchall()
        return list(res)

    def matchnn(self, keyword):
        conn = pymysql.connect('47.106.69.171', 'root', 'mysql', 'xiaojie', charset='utf8')
        cursor = conn.cursor()
        sql = 'select nickname,content,sendtime from danmu where nickname = "%s"' % (keyword)
        cursor.execute(sql)
        conn.commit()
        res = cursor.fetchall()
        return list(res)

    def searchtxt(self, keyword):
        conn = pymysql.connect('47.106.69.171', 'root', 'mysql', 'xiaojie', charset='utf8')
        cursor = conn.cursor()
        sql = 'select nickname,content,sendtime from danmu where instr (content,"%s") ' % (keyword)
        cursor.execute(sql)
        conn.commit()
        res = cursor.fetchall()
        return list(res)


if __name__ == '__main__':
    dm = Danmu()
    dm.matchnn('卡了个卡')
