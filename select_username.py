import databases_get

def mqtt(title='传感器'):
    sql = f"select * from mqtt where title='{title}';"
    data = databases_get.data_select(sql)
    list_ = []
    for i in data.values:
        list_.append(i[1])
    return list_

def information_login(username, password=''):
    sql = f"select * from information where username ='{username}' and password='{password}';"
    data = databases_get.data_select(sql)
    print(data.values[0])
    return len(data.values)


def information_register(username, password, token=''):
    sql = f"insert into information(username,password,token) values ('{username}','{password}','{token}');"
    databases_get.data_change(sql)
    sql = f"select * from information where username='{username}'"
    data = databases_get.data_select(sql)
    print(data.values[0])
    return data.values[0]


def information_save(username, token):
    sql = f"update information set token='{token}' where username='{username}';"
    databases_get.data_change(sql)
    sql = f"select * from information where username='{username}'"
    data = databases_get.data_select(sql)
    print(data.values[0])
    return data.values[0]


def information_remove(token):
    sql = f"update information set token='' where token='{token}';"
    databases_get.data_change(sql)


def information_select(token='MTY4MTQ3Njk4NS4wNzg4ODU2Ojg5NzMzZTBiZjgyOTkzZjUxNDRhYmQ1YmMwMDk0NDU3MDQ5NTM0MTQ='):
    sql = f"select * from information where token='{token}'"
    data = databases_get.data_select(sql)
    return data.values


# information_select()
