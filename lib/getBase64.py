import base64
def encry(cnf_org):
    f_org = open(cnf_org, 'r',encoding='utf-8')
    content = f_org.read()
    content1 = content.encode(encoding='utf-8')
    content2 = base64.b64encode(content1)
    f_org.close()
    with open(cnf_org, 'wb+') as f_org:
        f_org.write(content2)


def deci(cnf_now):
    f_now = open(cnf_now, 'r')
    content = f_now.read()
    content1 = base64.b64decode((content))
    with open(cnf_now, 'wb+') as f_now:
        f_now.write(content1)


if __name__ == '__main__':
    f_org = 'D:\\zentao.py'
    #encry(f_org)
    deci(f_org)
