import requests
from lib.get_yaml import doYaml
from settings import *


def loginPlatform():
    rs = doYaml.get_data(os.path.join(BASE_PATH, "createFlow.yaml"))
    url = rs["url"] + rs["path"]
    method = rs["method"]
    data = rs["LoginPlatform"]
    #login登录
    try:
        result = requests.request(method, url, json=data)
        if result.status_code == 200:
            rjson = result.json()
            if rjson["MessageType"]==200:
                rsToken = rjson["Data"]["access_token"]
            else:
                print("登录失败，请稍后再试")
        print(rsToken)
        return rsToken

    except Exception as e:
        print("错误原因是：%s" % e)

def login():
    rs = doYaml.get_data(os.path.join(BASE_PATH, "createFlow.yaml"))
    url = rs["url"] + rs["path"]
    method = rs["method"]
    data = rs["Login"]
    #login登录
    try:
        result = requests.request(method, url, json=data)
        if result.status_code == 200:
            rjson = result.json()
            if rjson["MessageType"]==200:
                rsToken = rjson["Data"]["access_token"]
            else:
                print("登录失败，请稍后再试")
        print(rsToken)
        return rsToken

    except Exception as e:
        print("错误原因是：%s" % e)


def createFlow(className: str, token: str, PlatformToken:str) -> bool:
    rs = doYaml.get_data(os.path.join(BASE_PATH, "createFlow.yaml"))
    url = 'http://192.168.110.75:8086/process/' + className

    header = rs["header"]
    Authorization = {'Authorization': token}
    PlatformAuthorization = {'PlatformAuthorization': PlatformToken}
    headers = {**header, **Authorization, **PlatformAuthorization}

    req = requests.get(url=url, headers=headers)

    try:
        if req.status_code == 200:
            result = req.text
        else:
            print("请求不成功")
        return result
    except Exception as e:
        print("错误原因是：%s" % e)

if __name__ == '__main__':
    createFlow("outApplication", login(), loginPlatform())
