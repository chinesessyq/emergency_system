import time


def record(function_name, name='', result=''):
    record_time = time.strftime('%Y-%m-%d %H-%M-%S %A')
    if name == '' and result == '':
        results = record_time + function_name + '\n\n'
    else:
        results = record_time + '   ' + function_name + '    :' + name + '    ' + result + '\n\n'
    with open('record.md', 'a+') as f:
        f.write(results)
