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

class TestcreateSpecialtyType():
    @allure.story('create 接口验证')
    @allure.title("专业设置-单个Create验证")
    def test_createSpecialtyType(self, login, getUserInfo):
        logging.info("create interface 开始测试....")
        with allure.step("准备数据"):
            reqList = Common.cre_data('createSpecialtyTypes.yaml', 'specialtyTypesSetting')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下填入取值x
                checkData = ids['mergeSpecialty']
                checkDatalist.append(checkData)
                checkDictlist.append({'id': checkData})
        with allure.step("与数据库数据进行对比..."):
            # 以下填入数据库的node 以及 key
            querySqlResult = Common.getSqlResult('specialtyTypesSetting', 'queryCheckSql', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(checkDatalist))
            pytest.assume(sorted(querySqlResult), sorted(checkDatalist))
        with allure.step("传递数据到下个接口..."):
            # 设置需要传递下去的值 X,Y
            Glob.set_value("QueryCheck", checkDatalist)
            Glob.set_value("createSpecialtyType", checkDictlist)
            logging.info(checkDictlist)
        logging.info("create interface 结束测试....")

    @allure.story('update 接口测试')
    @allure.title("专业设置-单个update验证")
    def test_updateSpecialtyType(self, login, getUserInfo):
        logging.info("update interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx
            data = Glob.get_value('createSpecialtyType')
            logging.info(data)
            reqList = Common.cre_data('updateSpecialtyType.yaml', 'specialtyTypesSetting', data, SpecialtyInput='input')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            # 开始进行接口请求，并取到返回值
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下根据返回值取key,替换X
                pytest.assume(result['mergeSpecialty'], Glob.get_value("QueryCheck"))
        with allure.step("与数据库数据进行对比..."):
            updateCheckPoint = Glob.get_value("QueryCheck")
            querySqlResult = Common.getSqlResult("specialtyTypesSetting", "updateCheckSql", "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(updateCheckPoint))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(updateCheckPoint)))
        logging.info("update interface 结束测试....")


    @allure.story('query 接口验证')
    @allure.title("专业设置-query全验证")
    def test_SpecialtyQuery(self, login, getUserInfo):
        with allure.step("准备数据"):
            reqList = Common.cre_data('SpecialtyQuery.yaml', 'specialtyTypesSetting')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
            # 以下是取数，根据返回key取值，替换其中X,Y部分为后续命名
            resultList = ids['specialtyTypes']
            checkDataList = [checkData["id"] for checkData in resultList]

        with allure.step("与数据库数据进行对比..."):
            # 查询sql的node,key值
            querySqlResult = Common.getSqlResult('specialtyTypesSetting', 'queryAllIds', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(checkDataList))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(checkDataList)))
        with allure.step("传递数据到下个接口..."):
            Glob.set_value("specialtyTypesData", resultList)
            Glob.set_value("allIds", checkDataList)
            logging.info(resultList)
        logging.info("query interface 结束测试....")

    @allure.story('disable 接口测试')
    @allure.title("专业设置-多个disable验证")
    def test_disableSpecialtyType(self, login, getUserInfo):
        logging.info("disable interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx
            data = Glob.get_value("specialtyTypesData")
            allIds = Glob.get_value("allIds")
            reqList = Common.cre_data('disableSpecialtyType.yaml', 'specialtyTypesSetting', data, SpecialtyInput='input')
            Auth = login

        with allure.step("开始第一次进行disable请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                with allure.step("执行第一次disable请求，校验置为disable"):
                    result = Common.getResult(Common.requestManual(reqlist, Auth))
                    pytest.assume(result['mergeSpecialty'], reqlist[1]['input']['id'])
            with allure.step("第一次执行完整后与数据库数据进行对比..."):
                querySqlResult = Common.getSqlResult('specialtyTypesSetting', 'disableCheck', "fetchall", tenant_id=getUserInfo)
                logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
                logging.info("接口返回并sort排序的数据为：%s" % sorted(allIds))
                pytest.assume(sorted(querySqlResult).__eq__(sorted(allIds)))

        with allure.step("进行query查询"):
            with allure.step("准备数据"):
                reqList = Common.cre_data('SpecialtyQuery.yaml', 'specialtyTypesSetting')
            with allure.step("开始进行接口请求，并取到返回值"):
                for reqlist in reqList:
                    logging.info("这里对接口返回的值进行json取值")
                    ids = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下是取数，根据返回key取值，替换其中X,Y部分为后续命名
                resultList = ids['specialtyTypes']

        with allure.step("开始第二次进行disable接口请求，并取到返回值"):
            reqList = Common.cre_data('disableSpecialtyType.yaml', 'specialtyTypesSetting', resultList, SpecialtyInput='input')
            for reqlist in reqList:
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                pytest.assume(result['mergeSpecialty'], reqlist[1]['input']['id'])
            with allure.step("与数据库数据进行对比..."):
                querySqlResult = Common.getSqlResult('specialtyTypesSetting', 'ableCheck', "fetchall", tenant_id=getUserInfo)
                logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
                logging.info("接口返回并sort排序的数据为：%s" % sorted(allIds))
                pytest.assume(sorted(querySqlResult).__eq__(sorted(allIds)))
        logging.info("disable interface 结束测试....")

    @allure.story('delete接口测试')
    @allure.title("专业设置-单个delete验证")
    def test_deleteSpecialtyTypes(self, login, getUserInfo):
        logging.info("delete interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据,以及登录获取当前version"):
            # 获取从上一个接口获取到的数据 xx
            data = Glob.get_value("createSpecialtyType")
            Auth = login
            # 再次登录，查询当前的version情况：
            with allure.step("进行query查询"):
                with allure.step("准备数据"):
                    reqList = Common.cre_data('SpecialtyQuery.yaml', 'specialtyTypesSetting')
                with allure.step("开始进行接口请求，并取到返回值"):
                    for reqlist in reqList:
                        logging.info("这里对接口返回的值进行json取值")
                        ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    # 以下是取数，根据返回key取值，替换其m中X,Y部分为后续命名
                    resultList = ids['specialtyTypes']
            reqList = Common.cre_data('deleteSpecialtyTypes.yaml', 'specialtyTypesSetting', data, resultList, IdAndVersionInput='idVersions')

        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info(result)
                pytest.assume(result['deleteSpecialties'], 'INSTANCE')
        with allure.step("与数据库数据进行对比..."):
            querySqlResult = Common.getSqlResult("specialtyTypesSetting", "queryCheckSql", "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" %(querySqlResult))
            pytest.assume(sorted(querySqlResult).__eq__([]))
        logging.info("delete interface 结束测试....")