import pytest
from lib.get_yaml import doYaml
from settings import *
from lib.get_header import getHeader
from lib.get_postgresql import requestPostgreSQL
from lib.getLogging import Logger
import allure
import requests
import json

#实例化数据库
requestSQL = requestPostgreSQL()

#日志采集
logging = Logger("common").getlog()



class Common(object):
    @staticmethod
    def cre_data(fileName:str, foldname:str, variableParms=None, *args, **kwargs) -> list:

        '''

        :param fileName: 配置的文件名
        :param foldname: data目录下的二级目录名
        :param variableParms: 上一个接口获取的数据
        :param *args:扩展字段，用于delete方法
        :param **kwargs:扩展字段，用于构造请求体，如kwargs['input']...
        :return:
        '''

        fold_path = os.path.join(DATA_PATH, foldname)
        rs = doYaml.get_data(os.path.join(fold_path, fileName))
        url = URL + rs["url"] if rs["url"] is not None else URL
        method = rs["method"]
        mode = rs["payload"]["mode"]
        variables = rs["payload"]["variables"]
        query = rs["query"]
        operationName = rs["payload"]["operationName"]
        header = getHeader(fileName, foldname)

        if mode == 'create' or mode == 'query':
            if variables is not None and variableParms is None:
                if isinstance(variables, list):
                    list_data = [(url, variable, method, header, operationName, query) for variable in variables]
                else:
                    list_data = [(url, variables, method, header, operationName, query)]

            elif variables is None and variableParms is not None:
                variables = variableParms
                if isinstance(variables, list):
                    list_data = [(url, variable[0], method, header, operationName, query) if isinstance(variable, tuple) \
                       else (url, variable, method, header, operationName, query)\
                            for variable in variables]
                else:
                    list_data = [(url, variables, method, header, operationName, query)]

            elif variables is not None and variableParms is not None:
                responselist = variableParms
                variables = Common.spliceDict(variables, responselist, **kwargs)
                if isinstance(variables, list):
                    list_data = [(url, variable, method, header, operationName, query) for variable in variables]
                else:
                    list_data = [(url, variables, method, header, operationName, query)]

            else:
                variable = {}
                list_data = [(url, variable, method, header, operationName, query)]

        elif mode == 'disable':
            variables = variableParms
            if isinstance(variables, list):
                list_data = [(url, Common.dictDataClean(variable, True, **kwargs), method, header, operationName, query) for variable in variables]
            else:
                list_data = [(url, Common.dictDataClean(variables, True, **kwargs), method, header, operationName, query)]

        elif mode == 'delete':
            variables = variableParms
            list_data = [(url, Common.dictDataClean(variables, False, *args, **kwargs), method, header, operationName, query)]

        elif mode == 'update':
            responselist = variableParms
            variables = Common.spliceDict(variables, responselist, **kwargs)
            if isinstance(variables, list):
                list_data = [(url, variable, method, header, operationName, query) for variable in variables]
            else:
                list_data = [(url, variables, method, header, operationName, query)]
        else:
            raise NameError("mode 不能为空，或者模式不对")
        return list_data

    @staticmethod
    def getResult(response, *args, **kwargs) -> bool:
        '''
        :param response:
        :param args: 请求的接口，可选
        :param kwargs: 关键字，需要单独查询sql，来查询的，可选
        :return:
        '''
        try:
            if response.status_code == 200:
                result = response.json()
            else:
                pytest.assume("返回值不为200")
            checkData = result['data'] if 'data' in result.keys() else result
            return checkData
        except Exception as e:
            return response

    @staticmethod
    def getDataBase(sql: str, fetch: str):
        '''

        :param sql: 请求的sql语句
        :param fetch: fetchone，fetchall，fetchmany可选
        :return:
        '''
        return requestSQL.excute_select(sql, fetch)

    @staticmethod
    def returnParms(data: dict, filename: str) -> bool:

        '''
        :param data: 传入中转值，dict类型
        :param filename: 存储名称，以yml或者yaml文件
        :return: bool
        '''

        return doYaml.save_datas(data, filename)

    @staticmethod
    def requestManual(manualList:list,Auth:str) -> str:
        '''

        :param manualList:
        :param Auth:
        :return:
        '''

        url = manualList[0]
        variable = manualList[1]
        method = manualList[2]
        header = manualList[3]
        operationName = manualList[4]
        query = manualList[5]

        with allure.step("获取token，并组装成一个新的headers"):
            # 获取token，并组装成一个新的headers，便于后续调用
            Authorization = {'Authorization': Auth}
            headers = {**header, **Authorization}

        with allure.step("组装请求体"):
            # 组装请求体
            requestQueen = {'operationName': operationName, 'variables': variable} if operationName is not None else {
                'variables': variable}
            graphqlRequestDict = {'query': query}
            requestQueen = {**graphqlRequestDict, **requestQueen}

        with allure.step("执行post或者get指令"):
            # 执行post或者get指令
            try:
                if method == "post":
                    logging.info("执行post请求....")
                    response = requests.post(url, headers=headers, data=json.dumps(requestQueen))  # post请求
                    logging.info(requestQueen)
                elif method == "get":
                    logging.info("执行get请求....")
                    response = requests.get(url=url, headers=headers, data=json.dumps(requestQueen))  # get请求
                    logging.info(requestQueen)
                else:
                    logging.info("暂不支持其他的接口请求方式")

            except Exception as e:
                logging.info("接口请求出错,错误是:" + e)
                return e

        return response

    @staticmethod
    def spliceDict(getYaml:(list,dict), reponseInterface:(list,dict), **kwargs) -> (dict, list):
        '''

        :param getYaml:
        :param reponseInterface:
        :return:
        '''
        listnew = []
        logging.info('getYaml:%s' % getYaml)
        logging.info('reponseInterface:%s' % reponseInterface)
        logging.info('kwargs: %s'% kwargs)
        if isinstance(getYaml, dict) and isinstance(reponseInterface, dict) and kwargs == {}:
            return {**getYaml, **reponseInterface}
        if isinstance(getYaml, dict) and isinstance(reponseInterface, dict) and kwargs['mode'] == 'create':
            return {'input': {**getYaml['input'], **reponseInterface}}
        elif isinstance(getYaml, list) and isinstance(reponseInterface, dict) and kwargs['mode'] == {}:
            for getYamlDict in getYaml:
                listnew.append(**getYamlDict, **reponseInterface)
        elif isinstance(getYaml, list) and isinstance(reponseInterface, dict) and kwargs['mode'] == 'create':
            for getYamlDict in getYaml:
                listnew.append({'input': {**getYamlDict['input'], **reponseInterface}})
        elif isinstance(getYaml, dict) and isinstance(reponseInterface, list) and 'mode' in kwargs.keys():
            for reponse in reponseInterface:
                listnew.append({'input': {**getYaml['input'], **reponse}})
        elif isinstance(getYaml, dict) and isinstance(reponseInterface, list):
            for reponseInterfaceDict in reponseInterface:
                listnew.append({kwargs['SpecialtyInput']: {**reponseInterfaceDict, **getYaml[kwargs['SpecialtyInput']]}})
        elif isinstance(getYaml, list) and isinstance(reponseInterface, list):
            for i in range(0, Common.compareLen(getYaml, reponseInterface)):
                listnew.append({kwargs['SpecialtyInput']: {**reponseInterface[i], **getYaml[i][kwargs['SpecialtyInput']]}})
        else:
            raise NameError("不支持转换的类型")
        logging.info(listnew)
        return listnew

    @staticmethod
    def compareLen(getYamlList, reponseInterfaceList) -> int:
        '''

        :param getYamlList:
        :param reponseInterfaceList:
        :return:
        '''
        return (len(getYamlList) if len(getYamlList) - len(reponseInterfaceList) <= 0 else len(reponseInterfaceList))

    @staticmethod
    def getSqlResult(node: str, key: str, fetch: str, OneNode=None, **kwargs) -> (list, tuple):
        '''

        :param key: 取出sql语句对应的key
        :param node: 识别yaml的文件节点
        :param fetch: fetchone fetchall fetchmany
        :param OneNode: None,默认就是返回只查询一个数据的list
        :param **kwargs: kwargs扩展字段,如向后叠加的 tenant_id ,带有data的会自动加上‘’
        :return:
        '''

        rs = doYaml.get_data(os.path.join(DATA_PATH, 'sqlData.yaml'))
        sqlQuery = rs[node][key]

        #拼凑字符串，带有data前缀的会自动加上单引号
        expandTuple = tuple(["'"+str(value)+"'" if key.find("data") != -1 else value for key, value in kwargs.items()])

        #兼容sql非参数化，只需sql追加tenant_id,以及参数化动态填入%s中的数据
        if kwargs != {} and len(kwargs) == 1:
            sqlQuery = '''%s %s '%s'%s''' % (sqlQuery, 'and tenant_id =', kwargs['tenant_id'], ';')
        elif kwargs != {} and len(kwargs) > 1:
            sqlQuery = sqlQuery % expandTuple
        else:
            raise UnboundLocalError

        logging.info("开始查询...")
        logging.info("查询语句为：%s" % sqlQuery)
        queryResult = requestSQL.excute_select(sqlQuery, fetch)
        if OneNode is None:
            queryResultToList = [sigleResult[0] for sigleResult in queryResult]
            return queryResultToList
        else:
            return queryResult

    @staticmethod
    def dictDataClean(cleanData:(dict,list), is_disable = False, *args, **kwargs) -> dict:
        '''
        :param cleanData: 待清洗的dict
        :param kwargs:扩展字段，用于构造返回dict
        :return:
        '''
        # 初始化delete list
        deleteList = []
        #删除，cleanData会传list，其余都传的dict
        if is_disable == True:
            cleanData['disabled'] = True if cleanData['disabled'] == False else False
        if kwargs != {}:
            if "SpecialtyInput" in kwargs.keys() and kwargs.__len__() == 1:
                del cleanData["__typename"]
                returnDict = {kwargs['SpecialtyInput']: cleanData}
                return returnDict
            elif "SpecialtyInput" in kwargs.keys() and kwargs.__len__() > 1:
                del cleanData["__typename"]
                return {**{kwargs['SpecialtyInput']: cleanData}, **kwargs}

            elif 'idAndVersions' in kwargs.keys() and args == ():
                subdict = Common.sub_dict(cleanData, ['id', 'version'])
                return {**{kwargs['idAndVersions']: [subdict]}, **{'disabled': cleanData['disabled']}}

            elif 'idAndVersions' in kwargs.keys() and kwargs.__len__() == 1 and args != ():
                for queryDataResponDict in args[0]:
                    for cleandata in cleanData:
                        if cleandata['id'] == queryDataResponDict['id']:
                            subdict = Common.sub_dict(queryDataResponDict, ['id', 'version'])
                            deleteList.append(subdict)
                            break
                return {**{kwargs['idAndVersions']: deleteList}, **{'forever': False}}

            elif "IdAndVersionInput" in kwargs.keys() and kwargs.__len__() == 1 and args != ():
                for queryDataResponDict in args[0]:
                    for cleandata in cleanData:
                        if cleandata['id'] == queryDataResponDict['id']:
                            subdict = Common.sub_dict(queryDataResponDict, ['id', 'version'])
                            deleteList.append(subdict)
                            break
                return {kwargs['IdAndVersionInput']: deleteList}

            else:
                return None

    @staticmethod
    def sub_dict(dct: dict, keys: list, default=None):
        '''

        :param dct: 主dict
        :param keys:
        :param default:
        :return: 拆分的子字典
        '''
        return dict([(key, dct.get(key, default)) for key in keys])
