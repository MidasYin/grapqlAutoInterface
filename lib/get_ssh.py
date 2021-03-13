# -*- coding:UTF-8 -*-
import paramiko

class requestSSH(object):
    # init
    def __init__(self, host, user, passwd):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, 22, user, passwd)

    def execute(self, command):
        try:
            execute_cmd = self.ssh.exec_command(command)
            return execute_cmd
        except Exception as e:
            print("%s" % e)

    def get_sms(self, command):
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            # time.sleep(10)
            # print(stdout.readlines())
            return stdout.readlines()
        except Exception as e:
            print("%s" % e)

    def __del__(self):
        self.ssh.close()