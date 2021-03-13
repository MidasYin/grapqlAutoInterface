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
    @allure.title("职别（调试用）-单个Create验证")
    def test_createPositionCategory(self, login, getUserInfo):
        logging.info("create interface 开始测试....")
        with allure.step("准备数据"):
            reqList = Common.cre_data('createPositionCategory.yaml', 'Position')
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
            querySqlResult = Common.getSqlResult('position', 'querypositionCategory', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            pytest.assume(sorted(querySqlResult).__ne__([]))

        with allure.step("传递数据到下个接口..."):
            # 设置需要传递下去的值 X
            positionCategoryId = [SqlResult for SqlResult in querySqlResult]
            checkDictlist = [{'id': SqlResult} for SqlResult in querySqlResult]
            Glob.set_value("positionCategoryDict", {'positionCategoryId': positionCategoryId[0]})
            Glob.set_value("creatPosition", checkDictlist)
            logging.info(positionCategoryId[0])
        logging.info("create interface 结束测试....")

    @allure.story('create 接口验证')
    @allure.title("职位-单个Create验证")
    def test_createPosition(self, login, getUserInfo):
        logging.info("create interface 开始测试....")
        positionCategoryDict = Glob.get_value('positionCategoryDict')
        with allure.step("准备数据"):
            reqList = Common.cre_data('createPosition.yaml', 'Position', positionCategoryDict, mode='create')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info("返回值为：%s" % ids)
                # 以下填入取值x
                checkData = ids['createPosition']
                assert checkData == "INSTANCE"

        with allure.step("与数据库数据进行对比..."):
            # 以下填入数据库的node 以及 key
            querySqlResult = Common.getSqlResult('position', 'queryCheckSql', "fetchall", \
                             datapositionCategoryDict = positionCategoryDict['positionCategoryId'], \
                             datatenant_id=getUserInfo)
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
    @allure.title("职位-单个update验证")
    def test_updatePosition(self, login, getUserInfo):
        logging.info("update interface 开始测试....")
        positionCategoryDict = Glob.get_value('positionCategoryDict')
        checkDatalist = Glob.get_value('updateCheckPoint')
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx
            data = Glob.get_value('createPosition')
            newlist = [{**dataDict, **positionCategoryDict} for dataDict in data]
            reqList = Common.cre_data('updatePosition.yaml', 'Position', newlist, SpecialtyInput='input')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            # 开始进行接口请求，并取到返回值
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下根据返回值取key,替换X
                pytest.assume(result['updatePosition'], "INSTANCE")
        with allure.step("与数据库数据进行对比..."):
            updateCheckPoint = Glob.get_value("QueryCheck")
            # 以下传入查询的node，key
            querySqlResult = Common.getSqlResult('position', 'updateCheckSql', "fetchall", \
                             datapositionCategoryDict = positionCategoryDict['positionCategoryId'], \
                             datatenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(checkDatalist)))
        logging.info("update interface 结束测试....")

    @allure.story('query 接口验证')
    @allure.title("职位-query全验证")
    def test_positionStructQuery(self, login, getUserInfo):
        positionCategoryDict = Glob.get_value('positionCategoryDict')
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
            checkPositionList = [checkData["positions"] for checkData in resultList if checkData["id"] == positionCategoryDict['positionCategoryId']][0]
            checkDataList = [checkid['id'] for checkid in checkPositionList]
        with allure.step("与数据库数据进行对比..."):
            # 查询sql的node,key值
            querySqlResult = Common.getSqlResult('position', 'queryAllIds', "fetchall", datapositionCategoryDict = positionCategoryDict['positionCategoryId'], \
                             datatenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(checkDataList))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(checkDataList)))
        with allure.step("传递数据到下个接口..."):
            # 替换下方的x
            Glob.set_value('QueryResult', checkPositionList)
            Glob.set_value("allIds", checkDataList)
            logging.info(resultList)
        logging.info("query interface 结束测试....")

    @allure.story('disable 接口测试')
    @allure.title("职位-多个disable验证")
    def test_disablePosition(self, login, getUserInfo):
        logging.info("disable interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx，yy
            data = Glob.get_value('QueryResult')
            allIds = Glob.get_value('allIds')
            positionCategoryDict = Glob.get_value('positionCategoryDict')
            reqList = Common.cre_data('disablePosition.yaml', 'Position', data,
                                      idAndVersions='idAndVersions')
            Auth = login
        with allure.step("开始第一次进行disable请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                with allure.step("执行第一次disable请求，校验置为disable"):
                    result = Common.getResult(Common.requestManual(reqlist, Auth))
                    logging.info("返回值为：%s" % result)
                    # 输入返回值的key x
                    pytest.assume(result['changePosition'], "INSTANCE")
            with allure.step("第一次执行完整后与数据库数据进行对比..."):
                # 查询输入node 以及 key
                querySqlResult = Common.getSqlResult('position', 'disableCheck', "fetchall", \
                                                     datapositionCategoryDict=positionCategoryDict['positionCategoryId'], \
                                                     datatenant_id=getUserInfo)
                logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
                logging.info("接口返回并sort排序的数据为：%s" % sorted(allIds))
                pytest.assume(sorted(querySqlResult).__eq__(sorted(allIds)))

        with allure.step("进行query查询"):
            with allure.step("准备数据"):
                reqList = Common.cre_data('positionStructQuery.yaml', 'Position', None)
            with allure.step("开始进行接口请求，并取到返回值"):
                for reqlist in reqList:
                    logging.info("这里对接口返回的值进行json取值")
                    ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    logging.info("返回值为：%s" % ids)
                    # 以下是取数，根据返回key取值，替换其中X部分为后续命名
                    resultList = ids['struct']
                    checkPositionList = [checkData["positions"] for checkData in resultList if
                                         checkData["id"] == positionCategoryDict['positionCategoryId']][0]

            with allure.step("开始第二次进行disable接口请求，并取到返回值"):
                reqList = Common.cre_data('disablePosition.yaml', 'Position', checkPositionList,
                                          idAndVersions='idAndVersions')
            for reqlist in reqList:
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info("返回值为：%s" % result)
                # 返回KEY X替换
                pytest.assume(result['changePosition'], "INSTANCE")
            with allure.step("与数据库数据进行对比..."):
                # 查询输入node 以及 key
                querySqlResult = Common.getSqlResult('position', 'ableCheck', "fetchall", \
                                                     datapositionCategoryDict=positionCategoryDict['positionCategoryId'], \
                                                     datatenant_id=getUserInfo)
                logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
                logging.info("接口返回并sort排序的数据为：%s" % sorted(allIds))
                pytest.assume(sorted(querySqlResult).__eq__(sorted(allIds)))
            logging.info("disable interface 结束测试....")

    @allure.story('delete接口测试')
    @allure.title("中文接口名-单个delete验证")
    def test_deletePosition(self, login, getUserInfo):
        logging.info("delete interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据,以及登录获取当前version"):
            # 获取从create接口获取到的数据 xx
            data = Glob.get_value('createPosition')
            positionCategoryDict = Glob.get_value('positionCategoryDict')
            Auth = login
            # 再次登录，查询当前的version情况：
            with allure.step("进行query查询"):
                with allure.step("准备数据"):
                    reqList = Common.cre_data('positionStructQuery.yaml', 'Position', None)
                with allure.step("开始进行接口请求，并取到返回值"):
                    for reqlist in reqList:
                        logging.info("这里对接口返回的值进行json取值")
                        ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    # 以下是取数，根据返回key取值,替换x
                    resultList = ids['struct']
                    checkPositionList = [checkData["positions"] for checkData in resultList if
                                         checkData["id"] == positionCategoryDict['positionCategoryId']][0]

            reqList = Common.cre_data('deletePosition.yaml', 'Position', data, checkPositionList,
                                      idAndVersions='idAndVersions')

        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info(result)
                # 替换下面的key x
                pytest.assume(result['deletePosition'], 'INSTANCE')
        with allure.step("与数据库数据进行对比..."):
            # 替换下面的查询数据库 替换node key
            querySqlResult = Common.getSqlResult('position', 'queryAllIds', "fetchall",  datapositionCategoryDict=positionCategoryDict['positionCategoryId'], \
                                                     datatenant_id=getUserInfo)
            updateSqlResult = Common.getSqlResult('position', 'queryAllIds', "fetchall",  datapositionCategoryDict=positionCategoryDict['positionCategoryId'], \
                                                     datatenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s"% querySqlResult)
            pytest.assume(sorted(querySqlResult).__eq__([]))
            pytest.assume(sorted(updateSqlResult).__eq__([]))
        logging.info("delete interface 结束测试....")

    @allure.story('delete接口测试')
    @allure.title("职别-单个delete验证")
    def test_deletePositionCategory(self, login, getUserInfo):
        logging.info("delete interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据,以及登录获取当前version"):
            # 获取从create接口获取到的数据 xx
            data = Glob.get_value('creatPosition')
            Auth = login
            # 再次登录，查询当前的version情况：
            with allure.step("进行query查询"):
                with allure.step("准备数据"):
                    reqList = Common.cre_data('positionStructQuery.yaml', 'Position', None)
                with allure.step("开始进行接口请求，并取到返回值"):
                    for reqlist in reqList:
                        logging.info("这里对接口返回的值进行json取值")
                        ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    # 以下是取数，根据返回key取值,替换x
                    resultList = ids['struct']

            reqList = Common.cre_data('deletePositionCategory.yaml', 'Position', data, resultList,
                                      idAndVersions='idAndVersions')

        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info(result)
                # 替换下面的key x
                pytest.assume(result['deletePositionCategory'], 'INSTANCE')
        with allure.step("与数据库数据进行对比..."):
            # 替换下面的查询数据库 替换node key
            querySqlResult = Common.getSqlResult('position', 'querypositionCategory', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % querySqlResult)
            pytest.assume(sorted(querySqlResult).__eq__([]))
        logging.info("delete interface 结束测试....")





