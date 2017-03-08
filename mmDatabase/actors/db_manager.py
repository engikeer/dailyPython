import pymysql


class DBManager(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "", "mmdata")
        self.cursor = self.db.cursor()

    def rollback(self):
        self.db.rollback()

    def disconnect(self):
        self.db.close()

    def save_data(self, res_data):
        sql = """INSERT INTO actress(name_m, name_o, name_a, act_birthday, constel,
                                blood_type, height, weight, BWH, homeplace, job, hobby)
                                VALUES('%s', '%s', '%s', str_to_date('%s', '%%Y-%%m-%%d %%H'), '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" \
              % (res_data["name_m"], res_data["name_o"], res_data["name_a"], res_data["act_birthday"],
                 res_data["constel"],
                 res_data["blood_type"],
                 res_data["height"], res_data["weight"], res_data["BWH"], res_data["homeplace"],
                 res_data["job"], res_data["hobby"])
        self.cursor.execute(sql)
        self.db.commit()
