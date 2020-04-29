import requests
import json
from logic.core_logic import ClientWrapper

loger = dict()


def main_bot(request):
    print(request.json)
    user_name = request.json["message"]["from"]["username"]
    message = request.json['message']['text']
    date = request.json["message"]["date"]
    
    if loger.get(user_name):
        loger[user_name].append({"date": date, "message": message})
    else:
        loger[user_name] = list()
        loger[user_name].append({"date": date, "message": message})
    print()
    print(loger)
    bot = TeleWrapper(request)
    
    if bot.message_decod(message) == "board_create":
        print(bot.message_decod(message))
        bot.data_collection_board_create()

    else:
        print(loger[user_name][-2])
        if loger[user_name][-2]["message"] == "Создать доску":
            print("!")
        elif loger[user_name][-3]["message"] == "Создать доску":
            print("!!")
        
    # # bot.send_start_message()
    # # if bot.is_start():
    # bot.main_menu_keyboard()
    # command = bot.message_decod(request.json['message']['text'])
    # data = bot.qwe()
    # ClientWrapper('Bob', '123', command, data=data)
    # bot.data_collection_board_create()
    # bot.data_collection_board_create().send()
    
class TeleWrapper:
    def __init__(self, request):
        self.request = request
        self.token = r"1026862035:AAG-mBQD7TgE_yaiE3uC38-W-Q5KRQ6uy1I"
        self.method = "sendMessage"
        self.url = f"https://api.telegram.org/bot{self.token}/{self.method}"

    def is_start(self):
        messege = self.request.json['message']['text']
        chat_id = self.request.json['message']['chat']['id']
        first_name = self.request.json['message']['chat']['first_name']

        if messege.lower() == '/start':
            print('Запуск бота')
            return True

    def forse(self):
        method = "ForceReply"
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        params = {"force_reply": "True"}
        requests.post(self.url, params)


    def send_start_message(self):
        """ Сalled when the bot starts """

        chat_id = self.request.json['message']['chat']['id']
        first_name = self.request.json['message']['chat']['first_name']
        message = f'{first_name}, для начала работы введите "/start"'
        data = {"chat_id": chat_id, "text": message}
        requests.post(self.url, data=data)

    def send_message(self, messege):
        chat_id = self.request.json['message']['chat']['id']
        data = {"chat_id": chat_id, "text": messege}
        requests.post(self.url, data=data)
    
    #### кнопка со ссылкой
    def inline_keyboard(self):
        """ Link button """

        chat_id = self.request.json['message']['chat']['id']
        message_id = self.request.json["message"]["message_id"]

        reply = json.dumps({"inline_keyboard":[[{"text":"Ниги","url":"https://memepedia.ru/negry-s-grobom/"}]]})
        params = {"chat_id": chat_id, "text": "!!!", "reply_markup":reply}
        requests.post(self.url, params)
    
    #### Кнопка которая пишет текст
    def main_menu_keyboard(self):
        """ Buttons main menu """
        
        chat_id = self.request.json['message']['chat']['id']
        message_id = self.request.json["message"]["message_id"]

        reply = json.dumps({"keyboard":[[{"text": "Создать доску"}], [{"text": "Создать карточку"}], 
                                        [{"text": "Изменить карточку"}], [{"text": "Удалить доску"}],
                                        [{"text": "Удалить карточку"}], [{"text": "Список досок"}],
                                        [{"text": "Отчёт"}]]})
        params = {"chat_id": chat_id, "reply_markup": reply}
        requests.post(self.url, params)

    def message_decod(self, messege):
        commands = {"Создать доску": "board_create", "Создать карточку": "card_create",
                    "Изменить карточку": "card_update", "Удалить доску": "board_delete",
                    "Удалить карточку": "card_delete", "Список досок": "board_list",
                    "Отчёт": "cards_report"}
        return commands.get(messege)

    def data_collection_board_create(self):
        data = dict()
        messege = """*        Создание Доски* \n\nНеобходимо ввести следующие параметры:
        1. Название доски
        2. Колонки на доске\n\nВедите название доски и колонки через ";", названия колонок через запятую, как показанно в примере:
        \nПример: ( Доска разработчика;ToDo,InProgress,Done )""" 
        chat_id = self.request.json['message']['chat']['id']
        message_id = self.request.json['message']['message_id']
        params = {"chat_id": chat_id, "text": messege, "parse_mode": "Markdown", "reply_to_message": message_id}
        requests.post(self.url, params)

    def otvet():
        messege = ''
        chat_id = self.request.json['message']['chat']['id']
        message_id = self.request.json['message']['message_id']
        params = {"chat_id": chat_id, "text": messege, "parse_mode": "Markdown", "reply_to_message": message_id}
        requests.post(self.url, params)
        
        # messege = """Введите названия колонок: 
        # (названия колонок вводятся *без пробелов* и *через запятую*)""" 
        # chat_id = self.request.json['message']['chat']['id']
        # params = {"chat_id": chat_id, "text": messege, "parse_mode": "Markdown"}
        # requests.post(self.url, params)        
        # arg = yield
        # data['columns'] = arg
        # return data

    def data_collection_card_create(self):
        data = dict()

        return data
    
    def data_collection_card_update(self):
        data = dict()

        return data

    def data_collection_board_delete(self):
        data = dict()

        return data

    def data_collection_card_delete(self):
        data = dict()

        return data

    def data_collection_board_list(self):
        data = dict()

        return data

    def data_collection_cards_report(self):
        data = dict()

        return data

    def send_markdown_message(self):
        messege = """*        Создание Доски* \n\nНеобходимо ввести следующие параметры:
        1. Название доски
        2. Колонки на доске\n\nВедите название доски: """ 
        chat_id = self.request.json['message']['chat']['id']
        params = {"chat_id": chat_id, "text": messege, "parse_mode": "Markdown"}
        requests.post(self.url, params)






# { "chat_id":" <id>","text": "Жмякай", "reply_markup": { "keyboard": [ [ {"text": "Кнопка 1"}, {"text": "Кнопка 2"} ], [ {"text": "Кнопка 3"}, {"text": "Кнопка 4"} ] ] } } 
# {'update_id': 457748742, 
# 'message': {'message_id': 72, 
#                 'from': {'id': 831026568, 
#                             'is_bot': False, 
#                             'first_name': 'Виктор', 
#                             'last_name': 'Овсиенко', 
#                             'username': 'ovsienko023', 
#                             'language_code': 'ru'}, 
#                 'chat': {'id': 831026568, 
#                         'first_name': 'Виктор',
#                         'last_name': 'Овсиенко', 
#                         'username': 'ovsienko023', 
#                         'type': 'private'}, 
#                         'date': 1587888836, 
#                         'text': 'q'}}
# ###
# print(request.headers)
