from lib.get_yaml import doYaml
from settings import *
import json
from lib.get_header import getHeader
from lib.get_postgresql import requestPostgreSQL
import requests
import inspect
#from lib.get_sql import requestSQL
# rSql = requestPostgreSQL()
# # list_data = []
# from lib.getLogging import Logger
# filename = os.path.basename(__file__)
# logging = Logger(filename).getlog()
# filepath = os.path.join(DATA_PATH,"specialtyTypesSetting")
# import pytest
# import decorator-args
# def cre_data():
#     rs = doYaml.get_data(os.path.join(filepath, 'SpecialtyQuery.yaml'))
#     #print(rs)
#     # url = URL + rs["url"] if rs["url"] is not None else URL
#     # method = rs["method"]
#     # payload = rs["payload"]
#     # query = rs["query"]
#     #
#     #
#     # header = getHeader('updateEducation.yaml')
#     return rs
#
# checkParams = cre_data()

# for Params in checkParams:
#     url = URL + Params["url"] if Params["url"] is not None else URL
#     method = Params["method"]
#     payload = Params["payload"]
#     print(Params["query"])


# print(checkParams["variables"])
# print(checkParams)
# listSingel = []
# listdict = []
# for checkParm in checkParams:
#     if isinstance(checkParm, str):
#         listSingel.append(checkParm)
#     elif isinstance(checkParm, dict):
#         listdict.append(checkParm)
#     else:
#         print("错误")
# print(listSingel)
# print(listdict)





# def add(x:int, y:int)->int:
#     '''
#     @param x:
#     @param y:
#     @return:
#     '''
#
#
#     return x+y
#
# print(add(1.232132131,1.3232313123134141))
#
# filename = 'test_allEmployees.py'
# featureName = filename.split(".")[0].split("_")[1] + "接口c"
# print(filename.split(".")[0].split("_")[1])
# print(featureName)
#
# print(requests.get('https://www.howsmyssl.com/a/check',verify=False).json()['tls_version'])
#
# requestSQL = requestSQL()
# re = requestSQL.excute_select('''select * FROM employee;''', 'fetchall')
# ddit = {'data': {'allEmployees': [{'id': '57a1ef8f-b44c-4893-a77b-5a8be2f7fd98', 'name': '任我行', 'post': {'id': '9971a9fc-9cfe-4f35-9703-7405e158f36a', 'employeeNum': 1}}, {'id': '7dbad003-3316-461e-9d20-a3fd9cdd72af', 'name': '撒大大', 'post': {'id': 'ca8f89e8-4a32-4799-9666-2167e9836fce', 'employeeNum': 1}}, {'id': '9b99f535-9b38-4122-b346-8cc3544ed972', 'name': '娜仁花', 'post': {'id': 'd49b558b-298a-4468-9e7c-7fd07155b8e7', 'employeeNum': 3}}, {'id': '6bc4e615-f704-455a-bb00-58e1fcf762bc', 'name': '奥特曼', 'post': {'id': 'd49b558b-298a-4468-9e7c-7fd07155b8e7', 'employeeNum': 3}}, {'id': '9b0ad491-b5a3-42d3-85d9-b180c83e50d0', 'name': '金 · 牢底坐穿 · 雕', 'post': {'id': 'd49b558b-298a-4468-9e7c-7fd07155b8e7', 'employeeNum': 3}}, {'id': 'e92aed05-66df-492e-9257-142434c4344e', 'name': '林大大', 'post': {'id': '28156103-ecfd-4533-b5b2-752914665e99', 'employeeNum': 1}}, {'id': '38b88e3f-a241-4c0c-94f9-d07fced3cd74', 'name': '西瓜', 'post': {'id': '4675304f-3bf7-4677-8cbe-a0d90d8eb37f', 'employeeNum': 2}}, {'id': 'ca9c2353-c722-49d7-9779-7547db443e72', 'name': '大苏打', 'post': {'id': '3ddd83d9-1e47-4272-aa2c-d521f42ffaf9', 'employeeNum': 1}}, {'id': 'd0021871-503e-4c5d-9269-31cd7a62fe6d', 'name': '实打实打算', 'post': {'id': '4675304f-3bf7-4677-8cbe-a0d90d8eb37f', 'employeeNum': 2}}], 'allEmployeesTotal': 9}}
# print(ddit['data'])
#variables = {'name': '', 'limit': 10, 'offset': 0}
# variables = [{'name': '', 'limit': 10, 'offset': 0}, {'name': '', 'limit': 10, 'offset': 0}]
# url = "xxx.xx.xx.xx"
# if isinstance(variables, list):
#     list1 = [(url, variable) for variable in variables]
#
#
# if variables is not None:
#     for variable in variables:
#         print(variable)
#
# print(list1)
# sd=[{"id": "xx1","name": "sd1"},{"id": "xx2","name": "sd2"}]
# data = {"id": ["xx1,xx2"]}
# doYaml.save_datas(data, 'test.yaml')
# rs = doYaml.get_data(r"C:\Users\Terry\PycharmProjects\citicguoanAutoInterface\temp\test.yaml")
# print(rs)
# #
# def demo(*args):
#     listdemo = [{arg:sd[arg]} for arg in args]
#     for Dict in listdemo:
#
#
# print(demo("id","name"))
# list22 = []
# l1 = [{'id':1,'name':'xx'}, {'id':2,'name':'xx'}]
# l2 = [{'des':'4'},{'des':'5'},{'des':'6'}]
# print(len(l1))
# print(len(l2))
# def compareLen(LenA,LenB):
#
#     return (LenA if LenA-LenB<=0 else LenB)
#
# for i in range(0,compareLen(len(l1),len(l2))):
#     list22.append({**l1[i],**l2[i]})
#
# print(list22)
# requestSQL = requestPostgreSQL()
# path = os.path.join(DATA_PATH, "specialtyTypesSetting")
# rs = doYaml.get_data(os.path.join(path, 'updateSpecialtyType.yaml'))
# var = rs['payload']['variables']
# print(var)
# id = {'id': 'XXXXSDSD'}
# ww = {'input': {**var['input'], **id}}
# tt= {**ww,**id}
# id2 = {'id2': 'XXXXSDSD'}
# print(tt)
# tt2 = {**tt, **id2}
#
# print(tt2)
# #
#
# list1 = ['de16bf21-dc88-4287-8eaf-b9d9f32406b6', '978eb2bf-3748-41ff-9fee-9b7341cddab6']
# list2 = ['978eb2bf-3748-41ff-9fee-9b7341cddab6', 'de16bf21-dc88-4287-8eaf-b9d9f32406b6']
#
# print(sorted(list1) == sorted(list2))


#qq={'Data': [{'id': 'e5dd4e1c-1fd1-4bcf-91fd-6049eee72caa', 'displayOrder': 1, 'name': '内部支撑', 'fullName': '内部支撑职务', 'subPositionNum': 1, 'deleted': False, 'disabled': False, 'positions': [{'id': 'a46e365d-dcc6-442f-97ec-93c485566226', 'name': '人事招聘', 'fullName': '人事招聘', 'displayOrder': 1, 'positionCategory': {'id': 'e5dd4e1c-1fd1-4bcf-91fd-6049eee72caa', 'name': '内部支撑', '__typename': 'PositionCategory'}, 'disabled': False, 'version': 1, '__typename': 'Position'}], 'version': 2, '__typename': 'PositionCategory'}, {'id': 'a25d9233-093e-4d80-8ced-da02ffd7f0b4', 'displayOrder': 1, 'name': '职能部门', 'fullName': '职能部门', 'subPositionNum': 1, 'deleted': False, 'disabled': False, 'positions': [{'id': '44af1467-8138-4e6b-8bd1-58a437299138', 'name': '高级工程师', 'fullName': '高级技术工程师', 'displayOrder': 1, 'positionCategory': {'id': 'a25d9233-093e-4d80-8ced-da02ffd7f0b4', 'name': '职能部门', '__typename': 'PositionCategory'}, 'disabled': False, 'version': 1, '__typename': 'Position'}], 'version': 1, '__typename': 'PositionCategory'}, {'id': '0c5306a9-4124-4a88-bd64-c2bbc16ef847', 'displayOrder': None, 'name': '管理部门', 'fullName': '管理部门', 'subPositionNum': 1, 'deleted': False, 'disabled': False, 'positions': [{'id': '8a90145a-8cb1-4dd7-a590-2a2aaaf3f32c', 'name': '董事会', 'fullName': '董事会', 'displayOrder': None, 'positionCategory': {'id': '0c5306a9-4124-4a88-bd64-c2bbc16ef847', 'name': '管理部门', '__typename': 'PositionCategory'}, 'disabled': False, 'version': 1, '__typename': 'Position'}], 'version': 1, '__typename': 'PositionCategory'}, {'id': 'a6a6cd3f-1780-473a-9521-905cc3174a62', 'displayOrder': None, 'name': 'autoTest', 'fullName': '自动化测试数据', 'subPositionNum': 1, 'deleted': False, 'disabled': False, 'positions': [{'id': '8bbf6745-f695-424d-a97a-20e432bf4a50', 'name': 'AutoTest', 'fullName': 'AutoTest', 'displayOrder': None, 'positionCategory': {'id': 'a6a6cd3f-1780-473a-9521-905cc3174a62', 'name': 'autoTest', '__typename': 'PositionCategory'}, 'disabled': False, 'version': 1, '__typename': 'Position'}], 'version': 1, '__typename': 'PositionCategory'}, {'id': '99a8c70e-232a-4004-b5d4-5d8b7459d4de', 'displayOrder': None, 'name': 'autoTest2', 'fullName': 'autoTest2', 'subPositionNum': 1, 'deleted': False, 'disabled': False, 'positions': [{'id': 'a7ba7d9c-dd6d-4b49-9ee9-371108d57bfd', 'name': 'AutoTest2', 'fullName': 'AutoTest2', 'displayOrder': None, 'positionCategory': {'id': '99a8c70e-232a-4004-b5d4-5d8b7459d4de', 'name': 'autoTest2', '__typename': 'PositionCategory'}, 'disabled': False, 'version': 1, '__typename': 'Position'}], 'version': 1, '__typename': 'PositionCategory'}, {'id': '7e239a61-6faa-42ae-9e0b-953a5a06bc63', 'displayOrder': 0, 'name': 'test1', 'fullName': 'test1', 'subPositionNum': None, 'deleted': False, 'disabled': True, 'positions': [], 'version': 3, '__typename': 'PositionCategory'}]}
#qq= {'rr':[{'id': 'd688f2f5-082c-49ad-be78-8b7f79eb4eb6', 'name': '计算机科学与技术', 'describe': '"这是一个快乐的事情，"这是一个快乐的事情，"这是一个快乐的事情，"这是一个快乐的事情，"这是一个快乐的事情，"这是一个快乐的事情，"这是一个快乐的事情，"这是一个快乐的事情，"这是一个快乐的事情，"', 'disabled': False, 'version': 67, '__typename': 'Specialty'}, {'id': 'ce70c3e4-42a0-4d6f-b7d1-51d077c7c342', 'name': '法学专业', 'describe': '这是一个快乐的事情，这是一个快乐的事情，这是一个快乐的事情，这是一个快乐的事情，这是一个快乐的事情，这是一个快乐的事情，这是一个快乐的事情，这是一个快乐的事情，这是一个快乐的事情，', 'disabled': False, 'version': 65, '__typename': 'Specialty'}, {'id': '15825e65-8ccf-47e7-ad5d-671eb517e757', 'name': 'modify one', 'describe': 'modify one', 'disabled': False, 'version': 4, '__typename': 'Specialty'}]}

# print(type(lll))
# ddd = json.dumps(qq, ensure_ascii=False)
# print(ddd)
#
# def Multdata(file,name, inonname=None, *args, **kwargs):
#     print(inonname)
#     print(args)
#     print(kwargs)
#
#
# print(Multdata('hm','you name',wo = 23))
#
#
# dd={'id': '1'}
# cc={'cc': '2'}
# aa = {'ss': '3'}
#
# cleanDict = {'disable':'true'}
# cleanDict['disable'] = 'true' if cleanDict['disable'] == 'false' else 'false'
# # if cleanDict['disable'] == 'false':
# #     cleanDict['disable'] = '11'
# # elif cleanDict['disable'] == 'true':
# #     cleanDict['disable'] = 'false'
#
# print(cleanDict)
#
# sss=['id','vesion']
# for si in sss:
#     print(si)
#
#
# def dede(**kwargs):
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(type(key))
#     #     print(key.find('data'))
#
#     str2 = ' '.join(["'"+str(value)+"'" if key.find("data") != -1 else value for key, value in kwargs.items()])
#     return str2
# stro = 'dsdsadasdasda'
# str3 = dede(name='and tenant_id =', Sex = 'and M=', dataclass1 = '3', datastro = stro)
# print(str3)
# sqlQuery = " select id from specialty where name = 'xx' and describe = 'xxxx' and is_delete = 'f'"
#
# str1 = '''%s %s %s''' % (sqlQuery, str3, ';')
# print(str1)
#
#
#
# list1 = [{'name':'xxx','sex':'m'},{'name':'xxxx','sex':'mm'}]
# list2 = [{'id':'xxx','class':'m'},{'id':'xxxx','class':'mm'}]
#
# list3 = [{**l1,**l2} for l1 in list1 for l2 in list2]
# print(list3)
# list1 = ['a', 'b', 'c', 'd']
# list2 = ['apple', 'boy', 'cat','x','y']
# for x, y in zip(list1, list2):
#     print(x, 'is', y)

# def ret(par):
#     if isinstance(par, int):
#         if par == 1 or par == 0:
#             return par  # 阶乘为1的时候，结果为1,返回结果并退出
#         if par < 0:
#             print("输入不能是负数")
#             raise SyntaxError
#         par = par * ret(par - 1)  # n! = n*(n-1)!
#         return par  # 返回结果并退出
#     else:
#         print("输入类型只能是整数")

# def ret2(par):

#     m=1
#     if par > 0 and par == 1:
#         return par
#     elif par <= 0:
#         return ("shuru budui")
#     for i in range(par, 1, -1):
#         m = m*i
#     return m

# class Request:
#     def __init__(self, url='', method='get'):
#         self.num_calls = 0
#         self.url = url
#         self.method = method
#         self.session = requests.session()

#     def __call__(self, func):
#         self.num_calls += 1
#         self.func = func

#         def fun_wrapper(*args, **kwargs):
#             rst = self.requestMethod()
#             self.func(*args, **kwargs)
#             self.closeSession()
#             return rst    
#         return fun_wrapper

#     def requestMethod(self, *args, **kwargs):
#         rst = self.session.request(self.method, self.url, *args, **kwargs)
#         rst.encoding = 'utf-8'
#         return rst.text

#     def closeSession(self):
#         return self.session.close()
    
# @Request(url="http://www.jd.com")
# def getJd():
#     print("开始请求京东:")



# class Request:

#     def __init__(self, url='', method='get'):
#         ''''''
#         self.url = url  # 请求路径
#         self.method = method # 请求方法
#         self.func_return = None # 被装饰器标记的方法的返回参数
#         self.func_im_self = None  # 被装饰器标记的方法的类的实例
#         self.session = None # 当前使用的会话对象

#     def __call__(self, func):
#         self.func = func
#         self.is_class = False
#         try:
#             if inspect.getfullargspec(self.func).args[0] == 'self':
#                 self.is_class = True
#         except IndexError:
#             pass

#         def fun_wrapper(*args, **kwargs):
#            # 调用被装饰标记的方法，这个方法会返回请求接口所需要的返回值
#             self.func_return = self.func(*args, **kwargs) or {}
#             self.func_im_self = args[0] if self.is_class else object
#             self.create_url()
#             self.create_session()
#             self.session.headers.update(getattr(self.func_im_self, 'headers', {}))
#             self.decorator_args.update(getattr(self.func_im_self, 'common_params', {}))
#             self.decorator_args.update(self.func_return)
            
#             return Request(self.method, self.url, self.session)
#         return fun_wrapper

#     def create_url(self):
#     """
#     生成http请求的url，跟路径和接口路由进行拼接
#     """
#     base_url = getattr(self.func_im_self, 'base_url', '')
#     self.url = self.func_return.pop('url', None) or self.url
#     self.url = ''.join([base_url, self.url])

# class AdvertService:

#     def __init__(self):
#         self.common_params = {} # 定义接口请求的公共参数
#         self.headers = {} # 定义请求的header
#         self.base_url = self._config.AD_ADMIN_ROOT_URL
        
#     @Request(url=“/v3/advert/create”, method='post')
#     def _create_ad(self, advert: Advert):
#         return dict(json=advert)

def countStr(parms: str) -> int:
    if isinstance(parms,str):
        count = 0
        for i in parms:
            count = count + 1
        return count
    else:
        return("请输入字符串类型")



if __name__ == '__main__':

    print(countStr("abc"))
