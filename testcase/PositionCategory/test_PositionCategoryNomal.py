#接口自动化模板
import allure
from settings import *
from lib.getLogging import Logger
from lib.common import Common
import lib.globalSetting as Glob
import pytest

#生成filename.log文件
filename = os.path.basename(__file__)
logging = Logger(filename).getlog()
featureName = filename.split(".")[0].split("_")[1] + "接口测试"
checkDatalist = []
checkDictlist = []

@allure.feature(featureName)
class Testpositioncategory():
    @allure.story('create 接口验证')
    @allure.title("职别-单个Create验证")
    def test_createPositionCategory(self, login, getUserInfo):
        logging.info("create interface 开始测试....")
        with allure.step("准备数据"):
            reqList = Common.cre_data('createPositionCategory.yaml', 'PositionCategory')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info("返回值为：%s" % ids)
                # 以下填入取值x
                checkData = ids['createPositionCategory']
                assert(checkData == "INSTANCE")
        with allure.step("与数据库数据进行对比..."):
            # 以下填入数据库的node 以及 key
            querySqlResult = Common.getSqlResult('positionCategory', 'queryCheckSql', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            pytest.assume(sorted(querySqlResult).__ne__([]))

        with allure.step("传递数据到下个接口..."):
            # 设置需要传递下去的值 X
            checkDictlist = [{'id': SqlResult} for SqlResult in querySqlResult]
            checkDatalist = [SqlResult for SqlResult in querySqlResult]
            Glob.set_value("createPosition", checkDictlist)
            Glob.set_value("updateCheckPoint", checkDatalist)
            logging.info(checkDictlist)
        logging.info("create interface 结束测试....")

    @allure.story('update 接口测试')
    @allure.title("职别- 单个update验证")
    def test_updatePositionCategory(self, login, getUserInfo):
        logging.info("update interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx
            data = Glob.get_value('createPosition')
            reqList = Common.cre_data('updatePositionCategory.yaml', 'PositionCategory', data, SpecialtyInput='input')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            # 开始进行接口请求，并取到返回值
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下根据返回值取key,替换X
                pytest.assume(result['updatePositionCategory'], "INSTANCE")
        with allure.step("与数据库数据进行对比..."):
            # 以下传入查询的node，key
            querySqlResult = Common.getSqlResult('positionCategory', 'updateCheckSql', "fetchall", tenant_id=getUserInfo)
            updateCheckPoint = Glob.get_value('updateCheckPoint')
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(updateCheckPoint)))
        logging.info("update interface 结束测试....")

    @allure.story('query 接口验证')
    @allure.title("职别-query全验证")
    def test_positionStructQuery(self, login, getUserInfo):
        with allure.step("准备数据"):
            reqList = Common.cre_data('positionStructQuery.yaml', 'PositionCategory', None)
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
            logging.info("返回值为：%s" % ids)
            # 以下是取数，根据返回key取值，替换其中X
            resultList = ids['struct']
            checkDataList = [checkData["id"] for checkData in resultList]

        with allure.step("与数据库数据进行对比..."):
            # 查询sql的node,key值
            querySqlResult = Common.getSqlResult('positionCategory', 'queryAllIds', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(checkDataList))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(checkDataList)))
        with allure.step("传递数据到下个接口..."):
            # 替换下方的x
            Glob.set_value('QueryResult', resultList)
            Glob.set_value("allIds", checkDataList)
            logging.info(resultList)
        logging.info("query interface 结束测试....")

    @allure.story('disable 接口测试')
    @allure.title("职别-多个disable验证")
    def test_disablePositionCategory(self, login, getUserInfo):
        logging.info("disable interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx，yy
            data = Glob.get_value('QueryResult')
            allIds = Glob.get_value('allIds')
            reqList = Common.cre_data('disablePositionCategory.yaml', 'PositionCategory', data, idAndVersions='idAndVersions')
            Auth = login

        with allure.step("开始第一次进行disable请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                with allure.step("执行第一次disable请求，校验置为disable"):
                    result = Common.getResult(Common.requestManual(reqlist, Auth))
                    logging.info("返回值为：%s" % result)
                    # 输入返回值的key x
                    pytest.assume(result['changePositionCategory'], "INSTANCE")
            with allure.step("第一次执行完整后与数据库数据进行对比..."):
                # 查询输入node 以及 key
                querySqlResult = Common.getSqlResult('positionCategory', 'disableCheck', "fetchall", tenant_id=getUserInfo)
                logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
                logging.info("接口返回并sort排序的数据为：%s" % sorted(allIds))
                pytest.assume(sorted(querySqlResult).__eq__(sorted(allIds)))

        with allure.step("进行query查询"):
            with allure.step("准备数据"):
                reqList = Common.cre_data('positionStructQuery.yaml', 'PositionCategory', None)
            with allure.step("开始进行接口请求，并取到返回值"):
                for reqlist in reqList:
                    logging.info("这里对接口返回的值进行json取值")
                    ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    logging.info("返回值为：%s" %ids)
                    # 以下是取数，根据返回key取值，替换其中X部分为后续命名
                    resultList = ids['struct']

            with allure.step("开始第二次进行disable接口请求，并取到返回值"):
                reqList = Common.cre_data('disablePositionCategory.yaml', 'PositionCategory', resultList, idAndVersions='idAndVersions')
            for reqlist in reqList:
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info("返回值为：%s" % result)
                # 返回KEY X替换
                pytest.assume(result['changePositionCategory'], "INSTANCE")
            with allure.step("与数据库数据进行对比..."):
                # 查询输入node 以及 key
                querySqlResult = Common.getSqlResult('positionCategory', 'ableCheck', "fetchall", tenant_id=getUserInfo)
                logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
                logging.info("接口返回并sort排序的数据为：%s" % sorted(allIds))
                pytest.assume(sorted(querySqlResult).__eq__(sorted(allIds)))
            logging.info("disable interface 结束测试....")

    @allure.story('delete接口测试')
    @allure.title("职别-单个delete验证")
    def test_deletePositionCategory(self, login, getUserInfo):
        logging.info("delete interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据,以及登录获取当前version"):
            # 获取从create接口获取到的数据 xx
            data = Glob.get_value('createPosition')
            Auth = login
            # 再次登录，查询当前的version情况：
            with allure.step("进行query查询"):
                with allure.step("准备数据"):
                    reqList = Common.cre_data('positionStructQuery.yaml', 'PositionCategory', None)
                with allure.step("开始进行接口请求，并取到返回值"):
                    for reqlist in reqList:
                        logging.info("这里对接口返回的值进行json取值")
                        ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    # 以下是取数，根据返回key取值,替换x
                    resultList = ids['struct']

            reqList = Common.cre_data('deletePositionCategory.yaml', 'PositionCategory', data, resultList, idAndVersions='idAndVersions')

        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info(result)
                #替换下面的key x
                pytest.assume(result['deletePositionCategory'], 'INSTANCE')
        with allure.step("与数据库数据进行对比..."):
            #替换下面的查询数据库 替换node key
            querySqlResult = Common.getSqlResult('positionCategory', 'queryCheckSql', "fetchall", tenant_id=getUserInfo)
            querySqlUpdateResult = Common.getSqlResult('positionCategory', 'updateCheckSql', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % querySqlResult)
            pytest.assume(sorted(querySqlResult).__eq__([]))
        logging.info("delete interface 结束测试....")
