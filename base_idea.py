# -*- coding: utf-8 -*-
__author__ = 'Liu_100'

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func
    return wrapper

@log
def now():
    print('2015-3-25')


print(now.__name__)
print(now().__name__)