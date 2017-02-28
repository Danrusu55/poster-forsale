class MyException(Exception):
    pass

try:
    if True:
        raise MyException('true')


except MyException as err:
    print(err)
except Exception as err:
    print('hit Exception')
