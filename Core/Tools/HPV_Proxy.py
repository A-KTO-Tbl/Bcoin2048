from requests import get
from threading import Thread
from colorama import Fore
from datetime import datetime

from Core.Tools.HPV_Getting_File_Paths import HPV_Get_Proxy



def HPV_Request(proxy: dict) -> bool:
    try:
        get('https://ipecho.net/plain', proxies=proxy)
        return True
    except:
        return False



def HPV_Checker(proxy):
    PROXY = f"{proxy['Login']}:{proxy['Password']}@{proxy['IP']}:{proxy['Port']}"
    PROXY_HTTPS = {'http': f'http://{PROXY}', 'https': f'https://{PROXY}'}
    PROXY_SOCKS5 = {'http': f'socks5://{PROXY}', 'https': f'socks5://{PROXY}'}

    if HPV_Request(PROXY_HTTPS):
        return PROXY_HTTPS
    elif HPV_Request(PROXY_SOCKS5):
        return PROXY_SOCKS5



def HPV_Proxy_Checker():
    '''Проверка HTTPS, SOCKS5 проксей на валидность'''

    PROXY_LIST = HPV_Get_Proxy()
    VALID_PROXY = []
    THREADS = []

    if PROXY_LIST:
        DIVIDER = Fore.BLACK + ' | '
        Time = Fore.BLUE + f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        Text = Fore.GREEN + 'Проверка прокси на работоспособность...'
        print(Time + DIVIDER + '🌐' + DIVIDER + Text)

    def _HPV_Checker(proxy):
        HPV = HPV_Checker(proxy)
        if HPV:
            VALID_PROXY.append(HPV)

    for proxy in PROXY_LIST:
        THREAD = Thread(target=_HPV_Checker, args=(proxy,))
        THREAD.start()
        THREADS.append(THREAD)

    for THREAD in THREADS:
        THREAD.join()

    return VALID_PROXY


