#接口自动化模板
import requests
import pytest
from lib.get_yaml import doYaml
from settings import *
from lib.getLogging import Logger
logging = Logger("conftest").getlog()
import lib.globalSetting as Glob


@pytest.fixture(scope="session", autouse=True)
def login():
    rs = doYaml.get_data(os.path.join(BASE_PATH, "login.yaml"))
    url = URL + rs["url"]
    method = rs["method"]
    data = rs["data"]
    #login登录
    try:
        result = requests.request(method, url, json=data)
        if result.status_code == 200:
            rjson = result.json()
            if rjson["MessageType"]==200:
                rsToken = rjson["Data"]["access_token"]
            else:
                logging.info("登录失败，请稍后再试")
        Glob.set_value("rsToken", rsToken)

    except Exception as e:
        logging.info("错误原因是:%s" % e)

    yield rsToken
    logging.info("开始清理临时数据...")

@pytest.fixture(scope="session")
def getUserInfo():
    rs = doYaml.get_data(os.path.join(BASE_PATH, "login.yaml"))
    url = URL + rs["urlgetUser"]
    header = rs["header"]
    Authorization = {'Authorization': Glob.get_value("rsToken")}
    headers = {**header, **Authorization}
    try:

        result = requests.get(url=url, headers=headers)

        if result.status_code == 200:
            rjson = result.json()
            if rjson["MessageType"] == 200:
                TenantId = rjson["Data"]["TenantId"]
            else:
                logging.info("获取失败，请稍后再试")
    except Exception as e:
        logging.info("错误原因是:%s" % e)
    return TenantId


if __name__ == '__main__':
    logging.info(login())
    logging.info(getUserInfo())







