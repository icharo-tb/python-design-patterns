# A Singleton pattern can be used to assure that only one instance is created per session, which can be useful in DB operations.

class Singleton:
    
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception('ErrNo.01: Singleton instance already exists.')
        else:
            Singleton.__instance = self

if __name__ == '__main__':

    err = '''
    ErrNo.05: Instances of class are not the same instance. Different instance have been created fro each variable.
    '''

    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    if id(s1) == id(s2):
        print('OK')
    else:
        raise Exception(err)