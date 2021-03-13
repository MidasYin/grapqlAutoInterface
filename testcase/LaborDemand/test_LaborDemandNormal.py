#接口自动化模板
import allure
from settings import *
from lib.getLogging import Logger
from lib.laborDemandCommon import laborDemandcommon
from lib.common import Common
import lib.globalSetting as Glob
import pytest

#生成filename.log文件
filename = os.path.basename(__file__)
logging = Logger(filename).getlog()
featureName = filename.split(".")[0].split("_")[1] + "接口测试"
checkDatalist = []
checkDictlist = []
responseOrgPost = []
@allure.feature(featureName)
class Testlabordemand():
    @allure.story('create 接口验证')
    @allure.title("用工需求-多个Create验证")
    def test_createPost(self, login, getUserInfo):
        logging.info("create interface 开始测试....")
        responseDepartmentList = laborDemandcommon.getDepartmentList(login, 'autoTestOrganization', 'autoTestOrg')
        responseOrgPost = laborDemandcommon.getOrgPost(login, 'autoTest', 'autoTest2', 'AutoTest1', 'AutoTest2', 'atest')

        #取出AutoPublic 部门id
        departmentDict = [{'departmentId': Department[0]} for Department in responseDepartmentList if Department[1] == 'AutoPublic'][0]
        #创建 AutoPublic部门下,AutoTest1 AutoTest2 atest 的岗位
        CreatePostList = [{'input': {**departmentDict, **{'postId': AutoId[0]}, **{'requireNum': 1}, **{'version': 1}}}\
                          for post in responseOrgPost \
                          for AutoId in post]
        checkPostTuple= tuple([AutoId[0] for post in responseOrgPost for AutoId in post])
        logging.info('---------------------------------')
        logging.info('checkPosttuple:%s' % (checkPostTuple,))
        logging.info('departmentId is:%s' % departmentDict['departmentId'])
        logging.info('----------------------------------')
        logging.info("构造创建用工需求数据为：%s" % CreatePostList)

        with allure.step("准备数据"):
            reqList = Common.cre_data('createLaborDemand.yaml', 'LaborDemand', CreatePostList)
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info("返回值为：%s" % ids)
                # 以下填入取值x
                checkData = ids['mergeJobRequire']
                checkDatalist.append(checkData)
                checkDictlist.append({'id': checkData})

        with allure.step("与数据库数据进行对比..."):
            # 以下填入数据库的node 以及 key
            querySqlResult = Common.getSqlResult('laborDemand', 'queryCheckSqlS', "fetchall",\
                                                 dataDepartmentid=departmentDict['departmentId'],\
                                                 checkPosttuple=checkPostTuple,\
                                                 datatenantid=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(checkDatalist))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(checkDatalist)))
        with allure.step("传递数据到下个接口..."):
            # 设置需要传递下去的值 X
            Glob.set_value("QueryCheck", checkDatalist)
            Glob.set_value('createPost', checkDictlist)
            logging.info(checkDictlist)
        logging.info("create interface 结束测试....")


    @allure.story('update 接口测试')
    @allure.title("用工需求-单个update验证")
    def test_updateLaborDemand(self, login, getUserInfo):
        logging.info("update interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx,并反转数据

            data = Glob.get_value('createPost')[::-1]
            responseDepartmentList = laborDemandcommon.getDepartmentList(login, 'autoTestOrganization', 'autoTestOrg')
            responseOrgPost = laborDemandcommon.getOrgPost(login, 'autoTest', 'autoTest2', 'AutoTest1', 'AutoTest2','atest')

            # 取出AutoTestOrg 部门id
            departmentDict = [{'departmentId': Department[0]} for Department in responseDepartmentList if Department[1] == 'AutoTestOrg'][0]

            #动态构造请求数据
            CreatePostList = [
                {**departmentDict, **{'postId': AutoId[0]}} \
                for post in responseOrgPost\
                for AutoId in post]
            requestData = [{**data[i], **CreatePostList[i]} for i in range(0, Common.compareLen(data, CreatePostList))]

            checkPostTuple = tuple([AutoId[0] for post in responseOrgPost for AutoId in post])

            reqList = Common.cre_data('updateLaborDemand.yaml', 'LaborDemand', requestData, SpecialtyInput='input')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            # 开始进行接口请求，并取到返回值
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下根据返回值取key,替换X
                pytest.assume(result['mergeJobRequire'], Glob.get_value("QueryCheck"))
        with allure.step("与数据库数据进行对比..."):
            updateCheckPoint = Glob.get_value("QueryCheck")
            # 以下传入查询的node，key
            querySqlResult = Common.getSqlResult('laborDemand', 'updateCheckSql', "fetchall",\
                                                 dataDepartmentid=departmentDict['departmentId'],\
                                                 checkPosttuple=checkPostTuple,\
                                                 datatenantid=getUserInfo, \
                                                 require_num='2'
                                                 )
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(updateCheckPoint))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(updateCheckPoint)))
        logging.info("update interface 结束测试....")


    @allure.story('query 接口验证')
    @allure.title("用工需求-query全验证")
    def test_LaborDemandQuery(self, login, getUserInfo):
        with allure.step("准备数据"):
            reqList = Common.cre_data('laborDemandQuery.yaml', 'LaborDemand')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
            logging.info("返回值为：%s" % ids)
            # 以下是取数，根据返回key取值，替换其中X
            resultList = ids['jobRequires']
            checkDataList = [checkData["id"] for checkData in resultList]

        with allure.step("与数据库数据进行对比..."):
            # 查询sql的node,key值
            querySqlResult = Common.getSqlResult('laborDemand', 'queryAllIds', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(checkDataList))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(checkDataList)))
        with allure.step("传递数据到下个接口..."):
            #替换下方的x
            Glob.set_value('LaborDemandQueryResult', resultList)
            Glob.set_value("allIds", checkDataList)
            logging.info(resultList)
        logging.info("query interface 结束测试....")

    @allure.story('delete接口测试')
    @allure.title("用工需求-单个delete验证")

    def test_deleteLaborDemand(self, login, getUserInfo):
        logging.info("delete interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据,以及登录获取当前version"):
            # 获取从create接口获取到的数据 xx
            data = Glob.get_value('createPost')
            Auth = login
            # 再次登录，查询当前的version情况：
            with allure.step("进行query查询"):
                with allure.step("准备数据"):
                    reqList = Common.cre_data('laborDemandQuery.yaml', 'LaborDemand')
                with allure.step("开始进行接口请求，并取到返回值"):
                    for reqlist in reqList:
                        logging.info("这里对接口返回的值进行json取值")
                        ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    # 以下是取数，根据返回key取值,替换x
                    resultList = ids['jobRequires']

            reqList = Common.cre_data('deleteLaborDemand.yaml', 'LaborDemand', data, resultList,
                                      IdAndVersionInput='idVersions')

        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info(result)
                # 替换下面的key x
                pytest.assume(result['deleteJobRequires'], 'INSTANCE')
        with allure.step("与数据库数据进行对比..."):
            # 替换下面的查询数据库 替换node key
            querySqlResult = Common.getSqlResult('laborDemand', 'queryAllIds', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % querySqlResult)
            pytest.assume(sorted(querySqlResult).__eq__([]))
        logging.info("delete interface 结束测试....")

