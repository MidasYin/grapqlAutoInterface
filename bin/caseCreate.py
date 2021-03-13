import sys
from settings import *
from lib.create_cases import create_case_file

#将当前项目的目录加入零时环境变量，避免在其他地方运行时会出现引入错误
base_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(base_path)
#testcase创建目录
path = os.path.join(CASE_PATH, "temp")

#查询yml文件的目录
foldname = "Position"

#yml文件的二级目录为

if __name__ == '__main__':
    # 首先调用生成用例函数
    # create_case_file(_path=path, files="deleteEducations.yaml") #指定路径，创建指定文件的测试代码
    create_case_file(foldname=foldname, _path=path, files="createPosition.yaml", template_type='create') # 指定路径，生成create接口
    create_case_file(foldname=foldname, _path=path, files="deletePosition.yaml", template_type='delete') # 指定路径，生成delete接口
    create_case_file(foldname=foldname, _path=path, files="positionStructQuery.yaml", template_type='query')  # 指定路径，生成query接口
    create_case_file(foldname=foldname, _path=path, files="disablePosition.yaml", template_type='disable')  # 指定路径，生成disable接口
    create_case_file(foldname=foldname, _path=path, files="updatePosition.yaml", template_type='update')  # 指定路径，生成update接口
    #create_case_file(_path=path) #所有case都建立在path路径下
    #create_case_file() #所有case都建立在testcase下

