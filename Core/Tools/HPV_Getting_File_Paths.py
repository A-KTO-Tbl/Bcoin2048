from os import path
from json import load



def HPV_Get_Accounts() -> dict:
    '''Получение списка аккаунтов'''

    PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Account.json')

    with open(PATH, 'r') as HPV:
        return load(HPV)



def HPV_Get_Proxy() -> list:
    '''Получение списка proxy'''

    PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Proxy', 'HPV_Proxy.txt')
    PROXY = []

    with open(PATH, 'r') as HPV:
        for Proxy in HPV.read().split('\n'):
            if Proxy:
                try:
                    Proxy = Proxy.split(':')
                    PROXY.append({'IP': Proxy[0], 'Port': Proxy[1], 'Login': Proxy[2], 'Password': Proxy[3]})
                except:
                    pass

        return PROXY


