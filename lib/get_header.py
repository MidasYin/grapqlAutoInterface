from lib.get_yaml import doYaml
from settings import *

def getHeader(fileName:str,foldname:str) ->str:
    '''

    :param fileName: yaml文件名
    :param foldname: data目录下的二级目录
    :return:
    '''

    fold_path = os.path.join(DATA_PATH, foldname)
    rs = doYaml.get_data(os.path.join(fold_path, fileName))
    header = rs["header"]
    if header == None:
        return None
    else:
        return header
    #
    # result = {**header, **rt}
    # return result
