from lib.get_postgresql import requestPostgreSQL
from lib.common import Common
tablesql = '''select table_name from information_schema.columns where "column_name" = 'tenant_id' '''
concatsql ="update \"%s\" set tenant_id = '%s' where tenant_id = '%s';"
table_name_list = [tablename[0] for tablename in Common.getDataBase(tablesql, 'fetchall')]
requestSQL = requestPostgreSQL()

def switchTalentId(newTenantId:str,oldTenantId:str) -> list:
    '''

    :param newTenantId:
    :param oldTenantId:
    :return:
    '''
    table_name_list = [tablename[0] for tablename in Common.getDataBase(tablesql, 'fetchall')]
    querylist = [concatsql % (table, newTenantId, oldTenantId) for table in table_name_list]
    try:
        for sql in querylist:
            requestSQL.execute(sql)
        requestSQL.__del__()
        return True
    except Exception as e:
        print("异常问题是：%s" % e)
        return False

# print(switchTalentId('1187270239060271104','1187309314467209216'))
# print(switchTalentId('1187309314467209216','1187270239060271104'))
print(switchTalentId('9999','1187270239060271104'))