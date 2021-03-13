from lib.getLogging import Logger
from lib.get_postgresql import requestPostgreSQL
from lib.get_yaml import doYaml
from settings import *

requestSQL = requestPostgreSQL()

# logging.info(re)


class AssertRequest():

    def __init__(self):
        pass
    @staticmethod
    def cre_data():
        rs = doYaml.get_data(os.path.join(DATA_PATH, 'allEmployees.yaml'))
        checkParams = rs["checkParams"]
        return checkParams

    @staticmethod
    def getResult(response, *args, **kwargs)->bool:
        '''

        :param response:
        :param args: 需要请求的接口
        :param kwargs: 关键字，需要单独sql查询的
        :return:
        '''


        listSingel = []
        listdict= []
        checkData = response['data']
        if response.status_code == 200:
            result = response.json()



    @staticmethod
    def getDataBase(sql:str,fetch:str):
        '''

        :param sql:
        :param fetch:
        :return:
        '''

        return requestSQL.excute_select(sql, fetch)




if __name__ == '__main__':
    parms = AssertRequest.cre_data()
    pp = [{'allEmployees': ['id', 'name', {'post': ['id', 'employeeNum']}]}, 'allEmployeesTotal', '__typename']
    ddit = {'data': {'allEmployees': [{'id': '57a1ef8f-b44c-4893-a77b-5a8be2f7fd98', 'name': '任我行',
                                       'post': {'id': '9971a9fc-9cfe-4f35-9703-7405e158f36a', 'employeeNum': 1}},
                                      {'id': '7dbad003-3316-461e-9d20-a3fd9cdd72af', 'name': '撒大大',
                                       'post': {'id': 'ca8f89e8-4a32-4799-9666-2167e9836fce', 'employeeNum': 1}},
                                      {'id': '9b99f535-9b38-4122-b346-8cc3544ed972', 'name': '娜仁花',
                                       'post': {'id': 'd49b558b-298a-4468-9e7c-7fd07155b8e7', 'employeeNum': 3}},
                                      {'id': '6bc4e615-f704-455a-bb00-58e1fcf762bc', 'name': '奥特曼',
                                       'post': {'id': 'd49b558b-298a-4468-9e7c-7fd07155b8e7', 'employeeNum': 3}},
                                      {'id': '9b0ad491-b5a3-42d3-85d9-b180c83e50d0', 'name': '金 · 牢底坐穿 · 雕',
                                       'post': {'id': 'd49b558b-298a-4468-9e7c-7fd07155b8e7', 'employeeNum': 3}},
                                      {'id': 'e92aed05-66df-492e-9257-142434c4344e', 'name': '林大大',
                                       'post': {'id': '28156103-ecfd-4533-b5b2-752914665e99', 'employeeNum': 1}},
                                      {'id': '38b88e3f-a241-4c0c-94f9-d07fced3cd74', 'name': '西瓜',
                                       'post': {'id': '4675304f-3bf7-4677-8cbe-a0d90d8eb37f', 'employeeNum': 2}},
                                      {'id': 'ca9c2353-c722-49d7-9779-7547db443e72', 'name': '大苏打',
                                       'post': {'id': '3ddd83d9-1e47-4272-aa2c-d521f42ffaf9', 'employeeNum': 1}},
                                      {'id': 'd0021871-503e-4c5d-9269-31cd7a62fe6d', 'name': '实打实打算',
                                       'post': {'id': '4675304f-3bf7-4677-8cbe-a0d90d8eb37f', 'employeeNum': 2}}],
                     'allEmployeesTotal': 9, '__typename': 'Query'}}
    yy = AssertRequest.getDataBase('''select count(*) FROM employee;''', 'fetchone')
    AssertRequest.getResult(ddit, parms, allEmployeesTotal=yy)

    zz= [('e92aed05-66df-492e-9257-142434c4344e', '林大大'), ('9b0ad491-b5a3-42d3-85d9-b180c83e50d0', '金 · 牢底坐穿 · 雕'), (
    '38b88e3f-a241-4c0c-94f9-d07fced3cd74', '西瓜')]





