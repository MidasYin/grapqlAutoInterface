# -*- coding: utf-8 -*-
import glob
import os
import platform
import shutil
import sys
import logging


class FileUtils(object):
    def __init__(self):
        pass
    @staticmethod
    def isfile(path):
        '''判断路径是否为文件'''
        if os.path.isfile(path):
            return True
        else:
            return False

    @staticmethod
    def isexists(path):
        '''检验给出的路径是否真地存'''
        if os.path.exists(path):
            return True
        else:
            return False

    def isdir(self, path):
        '''检验给出的路径是否是一个目录'''
        if os.path.isdir(path):
            return True
        else:
            return False

    def makedirs(self, path):
        '''创建文件或文件夹'''
        os.makedirs(path)

    def chdir(self, path):
        '''切换目录'''
        os.chdir(path)

    def rmdir(self, path):
        '''删除目录'''
        os.rmdir(path)

    def remove(self, path):
        '''删除文件'''
        os.remove(path)

    def removedirs(self, path):
        '''删除多个目录'''
        os.removedirs(path)

    def split(self, path):
        '''返回一个路径的目录名和文件名'''
        return os.path.split(path)

    def getFileList(self, path, fileList):
        '''遍历文件夹'''
        newDir = path
        if os.path.isfile(path):
            fileList.append(path)
        elif os.path.isdir(path):
            for s in os.listdir(path):
                newDir = os.path.join(path, s)
                self.getFileList(newDir, fileList)
        return fileList

    def execmd(self, shellstr):
        '''
        执行shell语句
        仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息
        '''
        os.system(shellstr)

    def popen(self, shellstr):
        '''执行shell语句,返回值是一个list'''
        return os.popen(shellstr).readlines()

    def call(self, shellstr):
        '''执行shell语句,返回值是一个list'''
        os.subprocess.call(shellstr)
        p = os.subprocess.Popen('ls', shell=True, stdout=os.subprocess.PIPE, stderr=os.subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        p.wait()

    def mkdir(self, path):
        """
        判断目录是否存在，不存在就创建目录
        :param path:   目录路径
        """
        if self.isexists(path):
            if self.isfile(path):
                self.makedirs(path)
        else:
            self.makedirs(path)

    def write(self, filepath, sb):
        # 写入文件,不会换行，需要自己写入换行 ,文件不存在时自动生成文件
        if 'Windows' in platform.system():
            filepath = filepath.replace('/', '\\')
        fp = open(filepath, 'w', encoding='utf8')
        for s in sb:
            fp.write(s)
        fp.close()

    def open(self, filepath):
        #打开文件，文件不存在时创建文件
        if 'Windows' in platform.system():
            filepath = filepath.replace('/', '\\')
        fp = open(filepath, 'a', encoding='utf8')
        fp.close()

    def read(self, filepath):
        # 一次性读取文件
        if 'Windows' in platform.system():
            filepath = filepath.replace('/', '\\')
        fp = open(filepath, 'w', encoding='utf8')
        sb = fp.read()
        fp.close()
        return sb

    def readline(self, filepath):
        # 一次只读取一行，占内存小，速度慢
        if 'Windows' in platform.system():
            filepath = filepath.replace('/', '\\')
        f = open(filepath, 'r', encoding='utf8')
        result = list()
        for line in f.readlines():  # 依次读取每行
            line = line.strip()  # 去掉每行头尾空白
            if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                continue  # 是的话，跳过不处理
            result.append(line)  # 保存
        result.sort()  # 排序结果
        f.close()  # 关闭文件
        return result

    def shutil(self,path1,path2):
        shutil.copyfile(path1,path2)

    def move(self,path1,path2):
        shutil.move(path1,path2)

    def glob(self,str):
        #从目录通配符搜索中生成文件列表
        return glob.glob(str)

    def getFilePath(self):
        # 获得的是当前执行脚本的位置
        return sys.argv[0]

    def getcwd(self):
        '''获取当前目录'''
        return os.getcwd()

    def getWorkPath(self):
        #获得当前工作目录
        return os.path.abspath(os.curdir)

    def getWorkParentPath(self):
        #获得当前工作目录的父目录
        return os.path.abspath('..')

    def getFileName(self,path):
        #去掉目录路径, 返回文件名
        return os.path.basename(path)

    def getFiledirname(self,path):
        #去掉文件名, 返回目录路径
        return os.path.dirname(path)

    def filejoin(self,path,filename):
        #将分离的各部分组合成一个路径名
        return os.path.join(path,filename)

    def filesplit(self,path):
        #返回 (dirname(), basename()) 元组
        return os.path.split(path)

    def samefile(self,path1,path2):
        #两个路径名是否指向同个文件
        return os.path.samefile(path1,path2)

    def readfile(self,path):
        body = []
        with open(path, 'rb') as f:
            for line in f.read():
                body.append(line)
        return  body

    @staticmethod
    def rmtree(foldname: str) -> bool:
        '''

        @param foldname: 文件夹的名字
        @return: bool
        '''

        try:
            shutil.rmtree(foldname)
            os.mkdir(foldname)
        except FileNotFoundError as e:
            logging.info("当前文件未找到")
            return False
        except Exception as e:
            logging.info("异常是：%s" % e)
            return False
        return True

# if __name__ == "__main__":
#     tt = FileUtils()
#     print(tt.getcwd())
#     print(tt.getWorkPath())
#     print(tt.getWorkParentPath())
#     print(tt.getFilePath())
