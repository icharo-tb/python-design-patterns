class Singleton:
    
    __instance = None

    def __new__(cls):
        if (cls.__instance is None):
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

if __name__ == '__main__':

    err = '''
    ErrNo.05: Instances of class are not the same instance. Different instance have been created fro each variable.
    '''

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print('OK')
    else:
        raise Exception(err)