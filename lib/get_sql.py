# -*- coding:UTF-8 -*-
import time
import os
import pymysql
from settings import *
import platform
from lib.getLogging import *
filename = os.path.basename(__file__)
logging = Logger(filename).getlog()

class requestSQL():
    # init
    def __init__(self):
        self.conn = pymysql.connect(
            host=ip,
            port=int(port),
            user=user,
            passwd=password,
            db=database,
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    # 须是完整的SQL语句
    def sql_exe(self, sql):
        self.cursor.execute(sql)

    # INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
    def insert(self, tbName, field, values):
        insSql = "insert into %s(%s)values %s" % (tbName, field, values)
        return self.execute(insSql)

    # select (self,表，列，where)
    def select(self, tbName, field='*', where=''):
        if where:
            where = " where "+where
        selSql = "select %s from %s %s" % (field, tbName, where)
        return self.execute(selSql)

    # UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
    def update(self, keyValues, tbName, where):
        setValue = ''
        for k,v in keyValues.items():
            setValue += '`%s`="%s",' % (k, v)
        if where:
            where = " where "+where
        updateSql = "update %s set %s %s" % (tbName, setValue[:-1], where)
        return self.execute(updateSql)

    # DELETE FROM 表名称 WHERE 列名称 = 值
    def delete(self,tbName, where):
        if where:
            where = " where "+where
        delSql = "delete from %s %s" % (tbName,where)
        return self.execute(delSql)

    # execute
    def execute(self, sql):
        try:
            if sql.find('select') != -1:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            elif sql.find('insert') != -1 or sql.find('update') != -1 or sql.find('delete') != -1:
                self.cursor.execute(sql)
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '--' + str(e))
            return False

    # __del__
    def __del__(self):
        self.cursor.close()
        self.conn.close()


    def excute_select(self,sql:str,fetch:str)->list:
        '''

        :param sql: 查询语句
        :param fetch:返回列表
        :return:
        '''

        self.cursor.execute(sql)
        if fetch == 'fetchone':
            return self.cursor.fetchone()
        elif fetch == 'fetchmany':
            return self.cursor.fetchmany()
        elif fetch == 'fetchall':
            return self.cursor.fetchall()
        else:
            return None


if __name__ == "__main__":
    # requestSQL = requestSQL()
    # re = requestSQL.sql_exe('''select * FROM mrm_type where mrm_type_id = 'basy';''')
    requestSQL = requestSQL()
    re = requestSQL.excute_select('''select * FROM mrm_type where mrm_type_id = 'basy';''','fetchone')
    print(re)
    # print(requestSQL.cursor.fetchone)
    # pass