import yaml
from settings import *

class doYaml():
    def __init__(self):
        pass
    @staticmethod
    def get_data(file_path):
        # 定义一个data变量，将data.yml里面的数据读出来
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    @staticmethod
    def save_data(data):
        with open(os.path.join(TEMP_PATH, "token.yml"), 'w') as f:
            return yaml.dump(data, f, Dumper=yaml.Dumper)

    @staticmethod
    def get_datas(file_path):
        # 定义一个data变量，将data.yml里面的数据读出来
        list_d = []
        with open(file_path, encoding='utf-8') as f:
            datas = yaml.safe_load_all(f)
            for data in datas:
                list_d.append(data)
        return list_d

    @staticmethod
    def save_datas(data,filename):
        f = open(os.path.join(TEMP_PATH, filename), 'a+')
        yaml.safe_dump(data, f)
        f.close()


if __name__ == '__main__':
    file = "D:\\workspace\\autoLigo\\data\\remain2.yaml"
    print(doYaml.get_datas(file))