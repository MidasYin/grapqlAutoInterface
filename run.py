from settings import *
import pytest
import os
from lib.fileGet import FileUtils
CASE_PATH = os.path.join(os.path.join(BASE_PATH, "testcase"), "specialtyTypesSetting")


if __name__ == '__main__':
    FileUtils.rmtree(REPORT_PATH)
    pytest.main(["-s", "-v", "-q", CASE_PATH, "--reruns", "3", "--reruns-delay", "2", "--alluredir", "./report/allure-results"])  # 以alluredir运行生成报告，并保存在result文件中
    allure_cmd = "allure generate ./report/allure-results -o ./report/html --clean"  # 将报告转换成html格式文件的命令
    p = os.popen(allure_cmd, mode="r")  # 运行命令
    print(p.read())    # 打印查看结果