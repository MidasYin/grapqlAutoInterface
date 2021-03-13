import requests
url ='http://api.nnzhp.cn/api/user/stu_info'
session = requests.session()
# r = session.get(url,params={'stu_name':'矿泉水'})#session  get，使用params
# r2= session.post(url,data={'stu_name':'矿泉水'})#session  post,使用data
# print(r)
# print(r.json())
# print(r.cookies)




result = session.get("http://www.sina.com.cn")
result.encoding="utf-8"
print(result)
print(result.text)

