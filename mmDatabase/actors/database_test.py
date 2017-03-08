# -*- coding: utf-8 -*-
# 测试数据
import pymysql

data1 = dict(name_m="橋本ありな", name_o="桥本有菜", name_a="Arina Hashimoto", act_birthday="1996-12-15", constel="射手座",
             blood_type="A", height="166CM", weight="", BWH="B83(C) W56 H83", homeplace="日本 东京都", job="艾薇女优",
             debut="2016", hobby="遛狗")
data2 = dict(name_m="樋井紅陽", name_o="樋井红阳", name_a="Hinoi Asahi", act_birthday="2000-06-16", constel="双子座",
             blood_type="O", height="169CM", weight="", BWH="B88(E) W60 H86", homeplace="日本 大阪府", job="模特、写真偶像",
             debut="2016", hobby="高尔夫、自拍")
dataCache = []
dataCache.append(data1)
dataCache.append(data2)


# 数据库操作器
class SqlManager(object):
    def __init__(self):
        # 链接数据库
        self.db = pymysql.connect("localhost", "root", "", "mmdata")
        self.cursor = self.db.cursor()


sqlM = SqlManager()
for dat in dataCache:
    sql = """INSERT INTO actress_copy(name_m, name_o, name_a, act_birthday, constel,
        blood_type, height, weight, BWH, homeplace, job, debut, hobby)
        VALUES('%s', '%s', '%s', str_to_date('%s', '%%Y-%%m-%%d %%H'), '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" \
          % (dat["name_m"], dat["name_o"], dat["name_a"], dat["act_birthday"], dat["constel"], dat["blood_type"],
             dat["height"], dat["weight"], dat["BWH"], dat["homeplace"], dat["job"], dat["debut"], dat["hobby"])
    print("sql: %s" % sql)

    try:
        sqlM.cursor.execute(sql)
        sqlM.db.commit()
    except Exception as e:
        sqlM.db.rollback()
        print("插入数据失败")
        print(str(e))
sqlM.db.close()
