from select_username import *
from generate_token import generate_token, certify_token
import json
import record


# username=&password=123456
def login(data):
    arr = data.split('&')
    dis = {}
    for value in arr:
        array = value.split("=")
        print(array)
        dis[array[0]] = array[1]
    print('dis', dis)
    num = information_login(dis['username'], dis['password'])
    if num == 1:
        # token_key = generate_token(dis['username'], 3600)
        token_key = generate_token('token', 3600)
        information_save(dis['username'], token_key)
        token_dir = {
            'token': token_key
        }
        print('json.dumps(token_dir)', json.dumps(token_dir))
        record.record('login', 'token', token_key)
        return json.dumps(token_dir)
    elif num > 1:
        print('数据存储有问题！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
    else:
        return_str = 'token失效'
        return json.dumps(return_str)
    # else:
    #     num = information_login(dis['username'], dis['password'])
    #     if num == 1:
    #         return json.dumps('用户名已存在')
    #     else:
    #         information_register(dis['username'], dis['password'])
    #         dis['path'] = '/login'
    #     return json.dumps(dis)


def register(data):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    print(data)


'''
1.判断路径 line / circle
2.查找当前用户订阅的传感器
3.查找订阅传感器的数据
4.返回数据
'''


def response_select(path, token):
    # 判断 token 是否过期
    if certify_token('token', token):
        # 查询该用户订阅传感器
        user = information_select(token)
        print('user', user)
        list_ = []
        series = []
        for i in user[0][3:]:
            list_.append(i)
        for i in range(len(list_)):
            if list_[i] is None:
                break
            data = mqtt(list_[i])
            series.append({})
            series[i]['name'] = list_[i]
            series[i]['data'] = data
        # print(series)
        # 折线图返回值
        if path.find('/line') != -1:
            series_line = series
            for i in range(len(series_line)):
                series_line[i]['type'] = 'line'
                series_line[i]['stack'] = 'Total'
            series_auto = series_line
            # print(series_line)
        elif path.find('circle') != -1:
            series_auto = series
        else:
            series_auto = '请求路径出错啦'
        return json.dumps(series_auto)
    else:
        return json.dumps('/index.html')


# response_select('/select/line', 'MTY4MTYxMTg0NS41ODUzOTc3OjljZmRiYjNkMmMxNTNlOGE5ZTgwY2MzMzliYmZiYjgxZWQxZjBiMjM=')
