from lib.fileGet import FileUtils
from settings import *

def set_res_data(res):
    if res:
        return res.lower().replace('":"', "=").replace('":', "=")

def create_case_file(foldname=None, template_type=None, files=None, _path = None):
    '''

    :param foldname: data 下的二级目录名
    :param template_type: auto query create三种，默认是None
    :param files: 具体的文件名
    :param _path: 指向创建testcase的具体路径
    :return:
    '''

    if template_type == 'create':
        template_file = os.path.join(TEMPLATE_PATH, 'templates_manual_create.txt')
    elif template_type == 'update':
        template_file = os.path.join(TEMPLATE_PATH, 'templates_semiautomatic_update.txt')
    elif template_type == 'query':
        template_file = os.path.join(TEMPLATE_PATH, 'templates_manual_query.txt')
    elif template_type == 'disable':
        template_file = os.path.join(TEMPLATE_PATH, 'templates_auto_disable.txt')
    elif template_type == 'delete':
        template_file = os.path.join(TEMPLATE_PATH, 'templates_auto_delete.txt')
    else:
        raise NameError
    filepath = os.path.join(DATA_PATH, foldname) if foldname is not None else DATA_PATH
    if files is not None:
        file = os.path.join(filepath, files)
        if FileUtils.isexists(file):
            case_create(files, template_file, foldname) if _path is None else case_create(files, template_file, foldname, _path)
        else:
            print("请在data目录下创建yaml或者yml文件")
    else:
        file_lists = os.listdir(DATA_PATH)        #取出data目录下的所有文件
        for file in file_lists:
            case_create(file, template_file) if _path is None else case_create(file, template_file, _path)


def case_create(file, template_file, foldname=None, _path=None):
    if file.endswith('.yaml') or file.endswith('.yml'):
        # 测试用例文件名和yaml文件名
        data_file = file.replace('.yaml', '').replace('.yml', '')
        # 测试用例方法名
        test_method_name = data_file  # 方法名按照文件名
        # 测试用例类名
        test_class_name = test_method_name.capitalize()  # 首字母大写
        with open(template_file, 'r', encoding='utf-8') as temp:
            content = temp.read() % {
                'class_name': test_class_name,
                'method_name': test_method_name,
                'data_file': data_file,
                'fold_name': foldname
            }
            test_case_file = 'test_{}.py'.format(data_file)
        # 根据模板生成测试用例文件,判断实在testcase目录下，还是在下级节点
        if _path is None:
            with open(os.path.join(CASE_PATH, test_case_file), 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            with open(os.path.join(_path, test_case_file), 'w', encoding='utf-8') as f:
                f.write(content)
        print("生成:" + test_case_file + ":文件成功")
    else:
        print("请输入yaml或者yml文件")
        return -1