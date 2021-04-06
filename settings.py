import os

#设置目录的绝对路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH, 'data')   #yaml测试用例存放位置
CASE_PATH = os.path.join(BASE_PATH, "testcase") #测试用例存放位置
REPORT_PATH = os.path.join(BASE_PATH, 'report')  #测试报告存放位置
TEMP_PATH = os.path.join(BASE_PATH, 'testcase/temp')  #存放临时用例位置
LOG_PATH = os.path.join(BASE_PATH, 'log')  #存放日志目录
TEMPLATE_PATH = os.path.join(BASE_PATH, 'template') #存放用例生成模板文件


#设置系统的地址
URL = "http://xx"
devBackendUrl = "http://yy"

#设置pymysql相关配置
ip = 'ip'
port = '5441'  #测试数据库端口
#port = '5442'  #dev数据库端口
user = 'zz'
password = '123456'
database = 'cc'

#配置redis


