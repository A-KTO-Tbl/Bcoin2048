from requests import post
from threading import Thread, Lock
from os import system as sys
from platform import system as s_name
from time import sleep
from random import randint, shuffle
from colorama import Fore
from typing import Literal
from datetime import datetime, timedelta
from urllib.parse import unquote
from itertools import cycle

from Core.Tools.HPV_Getting_File_Paths import HPV_Get_Accounts
from Core.Tools.HPV_Proxy import HPV_Proxy_Checker
from Core.Tools.HPV_User_Agent import HPV_User_Agent







class HPV_Bcoin2048:
    '''
    AutoBot Ferma /// HPV
    ---------------------
    [1] - `Получение кол-ва доступных игр и запуск их прохождения`
    
    [2] - `Ожидание от 6 до 7 часов`
    
    [3] - `Повторение действий через 6-7 часов`
    '''



    def __init__(self, Name: str, URL: str, Proxy: dict) -> None:
        self.Name = Name                   # Ник аккаунта
        self.Token = self.URL_Clean(URL)   # Уникальная ссылка для авторизации в mini app
        self.Proxy = Proxy                 # Прокси (при наличии)
        self.UA = HPV_User_Agent()         # Генерация уникального User Agent
        self.Domain = 'https://pipipupu.ru/api/v2' # Домен игры



    def URL_Clean(self, URL: str) -> str:
        '''Очистка уникальной ссылки от лишних элементов'''

        try:
            return unquote(URL.split('#tgWebAppData=')[1].split('&tgWebAppVersion')[0])
        except:
            return ''



    def Current_Time(self) -> str:
        '''Текущее время'''

        return Fore.BLUE + f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'



    def Logging(self, Type: Literal['Success', 'Warning', 'Error'], Name: str, Smile: str, Text: str) -> None:
        '''Логирование'''

        with Console_Lock:
            COLOR = Fore.GREEN if Type == 'Success' else Fore.YELLOW if Type == 'Warning' else Fore.RED # Цвет текста
            DIVIDER = Fore.BLACK + ' | '   # Разделитель

            Time = self.Current_Time()     # Текущее время
            Name = Fore.MAGENTA + Name     # Ник аккаунта
            Smile = COLOR + str(Smile)     # Смайлик
            Text = COLOR + Text            # Текст лога

            print(Time + DIVIDER + Smile + DIVIDER + Text + DIVIDER + Name)



    def Random_List(self) -> list:
        '''Рандомизация листа'''

        NEW_List = ['UP', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'UP']
        shuffle(NEW_List)

        return NEW_List



    def Get_Info(self) -> dict:
        '''Получение информации о балансе и достынх играх'''

        Headers = {'Accept-Language': 'ru,en;q=0.9,uz;q=0.8', 'Connection': 'keep-alive', 'Origin': 'https://pipipupu.ru', 'Referer': 'https://pipipupu.ru/appezdish', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': self.UA, 'accept': '*/*', 'authorization': '', 'content-type': 'application/json', 'telegram-init-data': self.Token}
        Json = {'operationName': 'GetViewer', 'variables': {}, 'query': 'query GetViewer {\n  viewer {\n    id\n    energyUnits\n    nextEnergyUnitsAt\n    bicoinBalance\n    name\n    inviteesCount\n    inviteesInviteesCount\n    inviteesReward\n    inviteesInviteesReward\n    allTimeEarnedBicoins\n    photoURL\n    bestGameEver {\n      bicoinReward\n      score\n      __typename\n    }\n    bestGameDaily {\n      bicoinReward\n      score\n      __typename\n    }\n    features\n    inviterId\n    hadClaimedFirst2048Reward\n    isBot\n    deleteTileBoostersCount\n    moveBackBoostersCount\n    moveWithoutTileBoostersCount\n    adsWatchedToday\n    __typename\n  }\n}'}

        try:
            HPV = post(self.Domain, headers=Headers, json=Json, proxies=self.Proxy).json()['data']['viewer']

            Games = HPV['energyUnits'] # Кол-во доступных игр
            Balance = HPV['bicoinBalance'] * 1000 # Текущий баланс

            return {'Status': True, 'Games': Games, 'Balance': f'{Balance:,.0f}'}
        except:
            return {'Status': False}



    def Play(self) -> None:
        '''Запуск игры'''

        Headers_0 = {'Accept-Language': 'ru,en;q=0.9,uz;q=0.8', 'Connection': 'keep-alive', 'Origin': 'https://pipipupu.ru', 'Referer': 'https://pipipupu.ru/appezdish/game', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': self.UA, 'accept': '*/*', 'authorization': '', 'content-type': 'application/json', 'telegram-init-data': self.Token}
        Headers_1 = {'Accept-Language': 'ru,en;q=0.9,uz;q=0.8', 'Connection': 'keep-alive', 'Origin': 'https://pipipupu.ru', 'Referer': 'https://pipipupu.ru/appezdish', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': self.UA, 'accept': '*/*', 'authorization': '', 'content-type': 'application/json', 'telegram-init-data': self.Token}
        Headers_2 = {'Accept-Language': 'ru,en;q=0.9,uz;q=0.8', 'Connection': 'keep-alive', 'Origin': 'https://pipipupu.ru', 'Referer': 'https://pipipupu.ru/appezdish/game', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': self.UA, 'accept': '*/*', 'authorization': '', 'content-type': 'application/json', 'telegram-init-data': self.Token}
        Headers_3 = {'Accept-Language': 'ru,en;q=0.9,uz;q=0.8', 'Connection': 'keep-alive', 'Origin': 'https://pipipupu.ru', 'Referer': 'https://pipipupu.ru/appezdish/game', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': self.UA, 'accept': '*/*', 'authorization': '', 'content-type': 'application/json', 'telegram-init-data': self.Token}
        Json_0 = {'operationName': 'myLastGame', 'variables': {}, 'query': 'query myLastGame {\n  MyLastGame {\n    id\n    status\n    field\n    nextTiles\n    nextIndexes\n    deletedTiles\n    __typename\n  }\n}'}
        Json_1 = {'operationName': 'startGame', 'variables': {}, 'query': 'mutation startGame {\n  StartGame {\n    id\n    status\n    field\n    nextIndexes\n    nextTiles\n    deletedTiles\n    __typename\n  }\n}'}

        try:
            try:
                # Получение ID игры
                GID = post(self.Domain, headers=Headers_1, json=Json_1, proxies=self.Proxy).json()['data']['StartGame']['id']
            except:
                GID = post(self.Domain, headers=Headers_0, json=Json_0, proxies=self.Proxy).json()['data']['MyLastGame']['id']

            # Совершение ходов
            for _ in range(randint(17, 32)):
                try:
                    Json_2 = {'operationName': 'sendMovesButch', 'variables': {'data': {'gameId': GID, 'moves': self.Random_List(), 'addedTiles': []}}, 'query': 'mutation sendMovesButch($data: GameMovesInput!) {\n  SendMovesButch(data: $data) {\n    id\n    field\n    status\n    nextIndexes\n    nextTiles\n    deletedTiles\n    __typename\n  }\n}'}
                    post(self.Domain, headers=Headers_2, json=Json_2, proxies=self.Proxy)
                    sleep(randint(12, 23))
                except:pass

            # Завершение игры
            Json_3 = {'operationName': 'CancelGame', 'variables': {'gameID': GID}, 'query': 'mutation CancelGame($gameID: ID!) {\n  CancelGame(gameID: $gameID)\n}'}
            post(self.Domain, headers=Headers_3, json=Json_3, proxies=self.Proxy).json()['data']
            self.Logging('Success', self.Name, '🎮', 'Игра сыграна!')
        except:
            self.Logging('Error', self.Name, '🔴', 'Игра не сыграна!')



    def Run(self) -> None:
        '''Активация бота'''

        while True:
            try:
                INFO = self.Get_Info() # Получение информации о балансе и достынх играх

                if INFO['Status']: # Если аутентификация успешна
                    self.Logging('Success', self.Name, '🟢', 'Инициализация успешна!')
                    self.Logging('Success', self.Name, '💰', f'Текущий баланс: {INFO["Balance"]}')

                    # Получение кол-ва доступных игр и запуск их прохождения
                    Get_plays = INFO['Games']
                    if Get_plays > 0:
                        self.Logging('Success', self.Name, '🎮', f'Игр доступно: {Get_plays}!')
                        for _ in range(Get_plays):
                            self.Play()
                            sleep(randint(12, 23))

                        self.Logging('Success', self.Name, '💰', f'Баланс после игр: {self.Get_Info()["Balance"]}')

                    Waiting = randint(22_000, 25_000) # Значение времени в секундах для ожидания
                    Waiting_STR = (datetime.now() + timedelta(seconds=Waiting)).strftime('%Y-%m-%d %H:%M:%S') # Значение времени в читаемом виде

                    self.Logging('Warning', self.Name, '⏳', f'Игр больше нет! Следующий старт игр: {Waiting_STR}!')

                    sleep(Waiting) # Ожидание от 6 до 7 часов

                else: # Если аутентификация не успешна
                    self.Logging('Error', self.Name, '🔴', 'Ошибка инициализации!')
                    continue
            except:
                pass







if __name__ == '__main__':
    sys('cls') if s_name() == 'Windows' else sys('clear')

    Console_Lock = Lock()
    Proxy = HPV_Proxy_Checker()

    def Start_Thread(Account, URL, Proxy = None):
        Bcoin2048 = HPV_Bcoin2048(Account, URL, Proxy)
        Bcoin2048.Run()

    for Account, URL in HPV_Get_Accounts().items():
        if Proxy:
            Proxy = cycle(Proxy)
            Thread(target=Start_Thread, args=(Account, URL, next(Proxy),)).start()
        else:
            Thread(target=Start_Thread, args=(Account, URL,)).start()


