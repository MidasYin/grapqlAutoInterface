import pytest
from lib.get_yaml import doYaml
from settings import *
from lib.get_header import getHeader
from lib.get_postgresql import requestPostgreSQL
from lib.getLogging import Logger
from lib.common import Common
import allure
import requests
import json

#实例化数据库
requestSQL = requestPostgreSQL()

#日志采集
logging = Logger("laborDemandcommon").getlog()

class laborDemandcommon(object):
    def __init__(self):
        pass

    @staticmethod
    def getDepartmentList(Auth:str, OrgNameOne:str, OrgNameTwo:str) ->list:
        '''

        :param Auth:
        :param OrgNameOne: 组织名1 如 autoTestOrganization
        :param OrgNameTwo: 组织名2 如 autoTestOrg
        :return: 部门列表
        '''

        logging.info("开始准备请求，获取待创建的机构列表..")
        with allure.step("准备访问组织的数据"):
            reqList = Common.cre_data('allOrganization.yaml', 'LaborDemand', None)
        with allure.step("开始进行allOrg接口请求，并取到组织名为 入参 'OrgNameOne' 和 'OrgNameTwo' 返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
            logging.info("返回值为：%s" % ids)
            # 获取name为 'autoTestOrganization'和 'autoTestOrg'的组织,返回下面的AutoPublic 和 AutoTestOrg
            resultList = ids['organizations'][0]['subOrganizations']
            responseDepartmentList = [(checkData['subOrganizations'][0]["id"], \
                                       checkData['subOrganizations'][0]["name"]) \
                                      for checkData in resultList\
                                      if checkData['name'] == OrgNameOne or checkData['name'] == OrgNameTwo]
        logging.info("返回的待请求的部门列表为：%s" % responseDepartmentList)
        return responseDepartmentList

    @staticmethod
    def getOrgPost(Auth:str, positionOne:str, positionTwo:str, OrgPostOne:str, OrgPostTwo:str, OrgPostThree:str) -> list:
        '''

        :param Auth:
        :param positionOne: autoTest
        :param positionTwo: autoTest2
        :param OrgPostOne: AutoTest1
        :param OrgPostTwo: AutoTest2
        :param OrgPostThree: atest
        :return: PostList
        '''
        responseOrgPost = []
        logging.info("获取待请求的职务结构.......")
        with allure.step("准备数据"):
            reqList = Common.cre_data('positionStructQuery.yaml', 'LaborDemand', None)
        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
            logging.info("返回值为：%s" % ids)
            # 以下是取数，根据返回key取值，替换其中X
            resultList = ids['struct']
            responsePositionStruct = [
                ({"id": checkData["positions"][0]['id']}, {'name': checkData["positions"][0]['name']}) \
                for checkData in resultList \
                if checkData['name'] == positionOne or checkData['name'] == positionTwo]
        logging.info("获取待请求的职务结构的列表为: %s" % responsePositionStruct)

        logging.info("获取待请求的职位列表......")
        with allure.step("准备数据"):
            reqList = Common.cre_data('postByPositionId.yaml', 'LaborDemand', responsePositionStruct)

        with allure.step("开始进行接口请求，并取到返回值"):
            for reqlist in reqList:
                logging.info("这里对接口返回的值进行json取值")
                ids = Common.getResult(Common.requestManual(reqlist, Auth))
                logging.info("返回值为：%s" % ids)
                # 以下是取数，根据返回key取值，替换其中X
                resultList = ids['posts']
                checkDataList = [(checkData["id"], checkData["name"]) for checkData in resultList \
                                 if checkData['name'] == OrgPostOne or checkData['name'] == OrgPostTwo or checkData[
                                     'name'] == OrgPostThree]
                responseOrgPost.append(checkDataList)
        logging.info("获取到的职位列表为：%s" % responseOrgPost)
        return responseOrgPost



