

def singleton(cls):
    instance = {}

    def wrapper(*arg, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*arg, **kwargs)
        return instance[cls]
    return wrapper


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Singleton2(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance
