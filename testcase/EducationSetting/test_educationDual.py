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

class TestEducationtypes():
    @allure.story('create 接口验证')
    @allure.title("学历设置-多个create测试")
    def test_createEducationTypes(self, login, getUserInfo):
        logging.info("create interface 开始测试....")
        with allure.step("准备数据"):
            reqList = Common.cre_data('createEducationS.yaml', 'EducationSetting')
            Auth = login
            logging.info("getuserinfo:%s" % getUserInfo)
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下填入取值x
                checkData = ids['mergeEducation']
                checkDatalist.append(checkData)
                checkDictlist.append({'id': checkData})
        with allure.step("与数据库数据进行对比..."):
            # 以下填入数据库的node 以及 key
            querySqlResult = Common.getSqlResult('educationSetting', 'queryCheckSqlS', "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(checkDatalist))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(checkDatalist)))
        with allure.step("传递数据到下个接口..."):
            # 设置需要传递下去的值 X,Y
            Glob.set_value("QueryCheck", checkDatalist)
            Glob.set_value("createEducationTypes", checkDictlist)
            logging.info(checkDictlist)
        logging.info("create interface 结束测试....")

    @allure.story('update 接口测试')
    @allure.title("学历设置-多个update测试")
    def test_updateEducationType(self, login, getUserInfo):
        logging.info("update interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据"):
            # 获取从上一个接口获取到的数据 xx
            data = Glob.get_value('createEducationTypes')
            logging.info(data)
            reqList = Common.cre_data('updateEducationS.yaml', 'EducationSetting', data, SpecialtyInput='input')
            Auth = login
        with allure.step("开始进行接口请求，并取到返回值"):
            # 开始进行接口请求，并取到返回值
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                # 以下根据返回值取key,替换X
                pytest.assume(result['mergeEducation'], Glob.get_value("QueryCheck"))
        with allure.step("与数据库数据进行对比..."):
            updateCheckPoint = Glob.get_value("QueryCheck")
            querySqlResult = Common.getSqlResult("educationSetting", "updateCheckSqlS", "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" % sorted(querySqlResult))
            logging.info("接口返回并sort排序的数据为：%s" % sorted(updateCheckPoint))
            pytest.assume(sorted(querySqlResult).__eq__(sorted(updateCheckPoint)))
        logging.info("update interface 结束测试....")


    @allure.story('delete接口测试')
    @allure.title("学历设置-多个测试")
    def test_deleteEducationTypes(self, login, getUserInfo):
        logging.info("delete interface 开始测试....")
        with allure.step("获取从上一个接口获取到的数据,以及登录获取当前version"):
            # 获取从上一个接口获取到的数据 xx
            data = Glob.get_value("createEducationTypes")
            Auth = login
            # 再次登录，查询当前的version情况：
            with allure.step("进行query查询"):
                with allure.step("准备数据"):
                    reqList = Common.cre_data('educationQuery.yaml', 'EducationSetting')
                with allure.step("开始进行接口请求，并取到返回值"):
                    for reqlist in reqList:
                        logging.info("这里对接口返回的值进行json取值")
                        ids = Common.getResult(Common.requestManual(reqlist, Auth))
                    # 以下是取数，根据返回key取值，替换其m中X,Y部分为后续命名
                    resultList = ids['educations']
            reqList = Common.cre_data('deleteEducations.yaml', 'EducationSetting', data, resultList, IdAndVersionInput='idVersions')

        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                result = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info(result)
                pytest.assume(result['deleteEducations'], 'INSTANCE')
        with allure.step("与数据库数据进行对比..."):
            querySqlResult = Common.getSqlResult("educationSetting", "queryCheckSql", "fetchall", tenant_id=getUserInfo)
            logging.info("数据库查询并sort排序的结果为：%s" %(querySqlResult))
            pytest.assume(sorted(querySqlResult).__eq__([]))
        logging.info("delete interface 结束测试....")