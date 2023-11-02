import telebot
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telebot import types

mytoken = "6503212060:AAHo2eMVlpM9HVjqsZUIfwk2iH--5kjPOQ4"
bot = telebot.TeleBot(mytoken)
answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']

myscope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
mycreds = ServiceAccountCredentials.from_json_keyfile_name('telegram-nupodymym-bot-90c25fc59a25.json',myscope)
myclient = gspread.authorize(mycreds)
mysheet = myclient.open("Бухгалтерия UnderTK Ноябрь").get_worksheet_by_id(1653485875)


global sheet_values
global bascet
global polucheniye
global vremya
global money
global total
global user_vars


# // сделать большое описание на старте бота

user_vars = {}
bascet = []
money = []
sheet_values = mysheet.get_values('T4:U')



@bot.message_handler(commands=['start'])
def welcome(message):
    # Кнопки после /start
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    assortiment_btn = types.KeyboardButton('🛍 Оформить заказ')
    manager_btn = types.KeyboardButton('👨 Менеджер')
    
    markup.row(assortiment_btn, manager_btn)
    if message.text == '/start':
        bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n👋Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}\n🛍У меня вы сможете оформить заказ', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n👋Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}\n🛍У меня вы сможете оформить заказ', reply_markup=markup)

    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['money'] = []
    user_vars[user_id]['bascet'] = []
    user_vars[user_id]['vremya'] = []
    user_vars[user_id]['bascet_true'] = []
    user_vars[user_id]['adress'] = []
    user_vars[user_id]['time_time'] = []
    user_vars[user_id]['telephon_number'] = []
    user_vars[user_id]['bascet_true_dostavka'] = []
    user_vars[user_id]['time_yandex'] = []
    user_vars[user_id]['adress_pochta'] = []
    user_vars[user_id]['fio'] = []
    user_vars[user_id]['code_pochta'] = []
    user_vars[user_id]['telephon_number_pochta'] = []
    user_vars[user_id]['bascet_true_pochta'] = []

    

    




    


@bot.message_handler()
def handler(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    if message.text == '🛍 Оформить заказ':
        assortiment(message)
    if message.text == '👨 Менеджер':
        manager(message)


    if message.text == '↩️ Назад':
        assortiment(message)
    if message.text == '↩️ Назад⠀':
        welcome(message)
    if message.text == '↩️ Назад в каталог':
        assortiment(message)
    if message.text == '↩️ Назад в каталог⠀':
        assortiment(message)
    if message.text == '↩️ К Яндекс Доставке':
        yandex_dostavka(message)
    if message.text == '↩️ Назад к оплате':
        yandex_order_pay(message)
    if message.text == '↩️ Добавить товар':
        assortiment(message)
    if message.text == '↩️ К времени':
        samovyvoz(message)
    if message.text == '↩️ К доставке':
        dostavka(message)
    if message.text == '↩️ К почте':
        pochta(message)


    if message.text == '💨 Каталог 1/3':
        assortiment_1(message)
    if message.text == '💨 Каталог 2/3':
        assortiment_2(message)
    if message.text == '💨 Каталог 3/3':
        assortiment_3(message)
    if message.text == '🛍 Проверить заказ':
        proverka_zakaz(message)
    
    if message.text == '🛍 Дальше':
        vibor_polucheniya(message)
    
    if message.text == '❌ Очистить корзину':
        clear_bascet(message)
    if message.text == '❌ Стереть':
        clear_vremya(message)
    if message.text == '❌ Стереть⠀':
        clear_dostavka(message)
    if message.text == '❌ Стереть⠀⠀':
        time_call_yandex_clean(message)
    if message.text == '❌ Стереть⠀⠀⠀':
        clear_pochta(message)



    if message.text == '📦 Самовывоз':
        samovyvoz(message)
    if message.text == '🚌 Доставка':
        dostavka(message)
    if message.text == '🚕 Яндекс доставка':
        yandex_dostavka(message)
    if message.text == '📩 Почта':
        pochta(message)


    if message.text == '🛍 Продолжить':
        itogo(message)
    if message.text == '🛍 Продолжить⠀':
        itogo_dostavka(message)
    if message.text == '🛍 Продолжить⠀⠀':
        itogo_pochta(message)

    if message.text == '🛍 Оплатить корзину':
        yandex_order_pay(message)
    if message.text == '🛍 Вызвать Яндекс Доставку':
        yandex_order_call(message)

    if message.text == '🛍 Заказать':
        order_send(message)
        next(message)
    if message.text == '🛍 Заказать⠀':
        order_send_dostavka(message)
        next(message)      
    if message.text == '🛍 Заказать⠀⠀':
        order_send_pochta(message)
        next(message)
    if message.text == '🛍 Готово':
        next(message)  

    if message.text == '🛍 Новый заказ':
        end(message)
    


    if message.text == '🕺':
        dance_emoji(message)
    if message.text == '💃':
        dance_emoji(message)
    if message.text == '🐺':
        wolf_emoji(message)
    if message.text == '🐺🤪':
        crazy_wolf_emoji(message)
    if message.text == '😡':
        rage_emoji(message)
    if message.text == '🖤':
        love_emoji(message)
    if message.text == '💰🕎':
        secret_jew_emoji(message)
        
       

    for zhizha in sheet_values:
        if str(zhizha).strip("[]").strip("''").replace("', '", " 💰")+" руб" == message.text:
            user_vars[user_id]['money'].append(int(zhizha[1]))
            user_vars[user_id]['bascet'].append(str(zhizha).strip("[]").strip("''").replace("', '", " 💰")+" руб")


def assortiment(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    assortiment_1_btn = types.KeyboardButton('💨 Каталог 1/3')
    assortiment_2_btn = types.KeyboardButton('💨 Каталог 2/3')
    assortiment_3_btn = types.KeyboardButton('💨 Каталог 3/3')
    proverka_zakaz = types.KeyboardButton('🛍 Проверить заказ')
    markup.row(proverka_zakaz)
    markup.row(assortiment_1_btn, assortiment_2_btn, assortiment_3_btn)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n💨Выберите каталог с ассортиментом:', reply_markup=markup)



def assortiment_1(message):
    # Получение значений из Google-таблицы
    sheet_values = mysheet.get_values('T4:U')
    global sheet_length
    if len(sheet_values) > 100:
        sheet_length = 104
    else:
        sheet_length = len(sheet_values)
    MainDataArray = []
    
    # Создание списка кнопок
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Назад')
    keyboard.add(back_btn)
    
    i = -1
    for array_T in mysheet.get_values('T4'+':'+'U'+str(sheet_length)):
        MainDataArray.append(array_T)
        i+=1
        sklad_1_btn = types.KeyboardButton(str(MainDataArray[i]).strip("[]").strip("''").replace("', '", " 💰")+" руб")
        keyboard.add(sklad_1_btn)

    back_btn = types.KeyboardButton('↩️ Назад')
    keyboard.add(back_btn)
    
    # Отправка списка кнопок пользователю
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n👇Нажмите на товар, чтобы добавить в корзину', reply_markup=keyboard)



def assortiment_2(message):
    # Получение значений из Google-таблицы
    sheet_length = 104
    sheet_values2 = mysheet.get_values('T'+str(sheet_length)+':'+'U')  
    global sheet_length2
    if len(sheet_values2) > 100:
        sheet_length2 = 204
    else:
        sheet_length2 = len(sheet_values2)+104
    MainDataArray = []
    
    # Создание списка кнопок
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Назад')
    keyboard.add(back_btn)
    
    i = -1
    for array_T in mysheet.get_values('T104'+':'+'U'+str(sheet_length2)):
        MainDataArray.append(array_T)
        i+=1
        sklad_1_btn = types.KeyboardButton(str(MainDataArray[i]).strip("[]").strip("''").replace("', '", " 💰")+" руб")
        keyboard.add(sklad_1_btn)

    back_btn = types.KeyboardButton('↩️ Назад')
    keyboard.add(back_btn)
    
    # Отправка списка кнопок пользователю
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n👇Нажмите на товар, чтобы добавить в корзину', reply_markup=keyboard)


def assortiment_3(message):
    # Получение значений из Google-таблицы
    sheet_length = 204
    sheet_values3 = mysheet.get_values('T'+str(sheet_length)+':'+'U')  
    global sheet_length3
    if len(sheet_values3) > 100:
        sheet_length3 = 304
    else:
        sheet_length3 = len(sheet_values3)+204
    MainDataArray = []
    
    # Создание списка кнопок
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Назад')
    keyboard.add(back_btn)
    
    i = -1
    for array_T in mysheet.get_values('T204'+':'+'U'+str(sheet_length3)):
        MainDataArray.append(array_T)
        i+=1
        sklad_1_btn = types.KeyboardButton(str(MainDataArray[i]).strip("[]").strip("''").replace("', '", " 💰")+" руб")
        keyboard.add(sklad_1_btn)
    back_btn = types.KeyboardButton('↩️ Назад')
    keyboard.add(back_btn)
    
    # Отправка списка кнопок пользователю
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n👇Нажмите на товар, чтобы добавить в корзину', reply_markup=keyboard)







def proverka_zakaz(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    finish_buy = types.KeyboardButton('🛍 Дальше')
    clear_bascet = types.KeyboardButton('❌ Очистить корзину')
    back_btn = types.KeyboardButton('↩️ Назад')
    markup.row(back_btn, finish_buy)
    markup.row(clear_bascet)
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    user_vars[user_id]['bascet_true'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true'] = user_vars[user_id]['bascet_true'].strip("[]").strip("''").replace("', '", " 💰")
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n🛒 В корзине: \n{user_vars[user_id]["bascet_true"]}')
    bot.send_message(message.chat.id, f'💰 Сумма: {total}руб', reply_markup=markup)
    bot.send_message(message.chat.id, '❗️Проверьте корзину и жмите \n«🛍 Дальше»', reply_markup=markup)
def clear_bascet(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Назад в каталог')
    markup.row(back_btn)
    user_vars[user_id]['bascet'].clear()
    total = 0
    user_vars[user_id]['money'].clear()
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❌Корзина очищена')
    user_vars[user_id]['bascet_true'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true'] = user_vars[user_id]['bascet_true'].strip("[]").strip("''").replace("', '", " 💰")
    bot.send_message(message.chat.id, f'🛒 В корзине: \n{user_vars[user_id]["bascet_true"]}', reply_markup=markup)








def vibor_polucheniya(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    samovyvoz = types.KeyboardButton('📦 Самовывоз')
    dostavka = types.KeyboardButton('🚌 Доставка')
    yandex_dostavka = types.KeyboardButton('🚕 Яндекс доставка')
    pochta = types.KeyboardButton('📩 Почта')
    back_btn = types.KeyboardButton('↩️ Назад в каталог⠀')
    markup.row(samovyvoz, dostavka, yandex_dostavka, pochta)
    markup.row(back_btn)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❗️Выберите способ получения:', reply_markup=markup)








def samovyvoz(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n💬Самовывоз на Свиридова 69 \n\n💬С 11 до 24')
    answer = bot.send_message(message.chat.id, '❗️Напишите время, в которое подъедете забрать: \n❗️Пример: «15:20»', reply_markup=markup)
    bot.register_next_step_handler(answer, vremya)
def vremya(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['vremya'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    next = types.KeyboardButton('🛍 Продолжить')
    clear_vremya = types.KeyboardButton('❌ Стереть')
    markup.row(clear_vremya, next)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⏳Время самовывоза: {user_vars[user_id]["vremya"]}', reply_markup=markup)
def clear_vremya(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['vremya'] = ""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_time_btn = types.KeyboardButton('↩️ К времени')
    markup.row(back_time_btn)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❌Время стёрто', reply_markup=markup)



def itogo(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Добавить товар')
    next = types.KeyboardButton('🛍 Заказать')
    markup.row(back_btn, next)
    user_vars[user_id]['bascet_true'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true'] = user_vars[user_id]['bascet_true'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n🛒 В корзине: \n{user_vars[user_id]["bascet_true"]}')
    bot.send_message(message.chat.id, f'⏳ Время самовывоза: {user_vars[user_id]["vremya"]}')
    bot.send_message(message.chat.id, f'💰 Сумма: {total}руб', reply_markup=markup)
def order_send(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['user_first_name'] = message.from_user.first_name
    user_vars[user_id]['user_last_name'] = message.from_user.last_name
    user_vars[user_id]['user_username'] = message.from_user.username
    message.chat.id1 = 5482862125
    user_vars[user_id]['bascet_true'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true'] = user_vars[user_id]['bascet_true'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id1, f'Заказ от {user_vars[user_id]["user_first_name"]} {user_vars[user_id]["user_last_name"]}({user_vars[user_id]["user_username"]})\n\n🛒 В корзине: \n{user_vars[user_id]["bascet_true"]} \n\n⏳ Время самовывоза: {user_vars[user_id]["vremya"]}\n\n💰 Сумма: {total}руб')









def dostavka(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n💬Стоимость доставки 4р \n\n💬Доставка в районе города - Гомель \n\n💬Если указывайте точное время(без диапазона), то возможна доставка на 30 мин позже/раньше')
    adres_msg = bot.send_message(message.chat.id, '❗️Напишите адрес, на который нужно доставить: \n❗️Пример: «ул. Свиридова 21»',reply_markup=markup)

    bot.register_next_step_handler(adres_msg, adress)

def adress(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['adress'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    time_msg = bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❗️Напишите время, в которое можно доставить:', reply_markup=markup)
    bot.send_message(message.chat.id, '\n❗️Пример: «14:00 - 15:00»')
    bot.register_next_step_handler(time_msg, time_time)
def time_time(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['time_time'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    telephone_number_msg = bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❗️Напишите контактный номер:', reply_markup=markup)
    bot.send_message(message.chat.id, '\n❗️Пример: «+375299617485»')
    bot.register_next_step_handler(telephone_number_msg, telephon_number)
def telephon_number(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['telephon_number'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    next = types.KeyboardButton('🛍 Продолжить⠀')
    clear_dostavka = types.KeyboardButton('❌ Стереть⠀')
    markup.row(clear_dostavka, next)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n🗺Адрес доставки: {user_vars[user_id]["adress"]}')
    bot.send_message(message.chat.id, f'\n⏳Время доставки: {user_vars[user_id]["time_time"]}')
    bot.send_message(message.chat.id, f'\n📞Контактный номер: {user_vars[user_id]["telephon_number"]}', reply_markup=markup)
def clear_dostavka(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['adress'] = ""
    user_vars[user_id]['time_time'] = ""
    user_vars[user_id]['telephon_number'] = ""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_adress_btn = types.KeyboardButton('↩️ К доставке')
    markup.row(back_adress_btn)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❌Адрес стёрт \n\n❌Время стёрто \n\n❌Номер стёрт',  reply_markup=markup)



def itogo_dostavka(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Добавить товар')
    next = types.KeyboardButton('🛍 Заказать⠀')
    markup.row(back_btn, next)
    user_vars[user_id]['bascet_true_dostavka'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true_dostavka'] = user_vars[user_id]['bascet_true_dostavka'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n🛒 В корзине: \n{user_vars[user_id]["bascet_true_dostavka"]} \n⠀ \n🗺 Адрес доставки: {user_vars[user_id]["adress"]} \n⏳ Время доставки: {user_vars[user_id]["time_time"]} \n📞 Контактный номер: {user_vars[user_id]["telephon_number"]} \n⠀ \n 💰 Сумма: {total}руб + 4руб', reply_markup=markup)
def order_send_dostavka(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['user_first_name'] = message.from_user.first_name
    user_vars[user_id]['user_last_name'] = message.from_user.last_name
    user_vars[user_id]['user_username'] = message.from_user.username
    message.chat.id1 = 5482862125
    user_vars[user_id]['bascet_true_dostavka'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true_dostavka'] = user_vars[user_id]['bascet_true_dostavka'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id1, f'Заказ от {user_vars[user_id]["user_first_name"]} {user_vars[user_id]["user_last_name"]}({user_vars[user_id]["user_username"]})\n\n🛒 В корзине: \n{user_vars[user_id]["bascet_true_dostavka"]} \n\n🗺 Адрес доставки: {user_vars[user_id]["adress"]} \n⏳ Время доставки: {user_vars[user_id]["time_time"]} \n📞 Контактный номер: {user_vars[user_id]["telephon_number"]} \n\n💰 Сумма: {total}руб + 4руб')








def yandex_dostavka(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n💬Отправка Яндекс Доставкой с 12 по 24 \n\n💬Если нужно раньше/позже, то предупредите менеджера', reply_markup=markup)
    bot.send_message(message.chat.id, '\n❗️Напишите в какое время будете заказывать Яндекс Доставку на адрес:')
    call_yandex = bot.send_message(message.chat.id, '\n❗️Пример: «14:20»')
    bot.register_next_step_handler(call_yandex, time_call_yandex)
def time_call_yandex(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['time_yandex'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bascet_pay = types.KeyboardButton('🛍 Оплатить корзину')
    yandex_time_clear = types.KeyboardButton('❌ Стереть⠀⠀')
    markup.row(yandex_time_clear, bascet_pay)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⏳ Время заказа Яндекс Доставки на адрес: {user_vars[user_id]["time_yandex"]}', reply_markup=markup)
def time_call_yandex_clean(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['time_yandex'] = ""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_yandex_btn = types.KeyboardButton('↩️ К Яндекс Доставке')
    markup.row(back_yandex_btn)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❌Время заказа Яндекс Доставки стёрто',  reply_markup=markup)
def yandex_order_pay(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yandex_call_btn = types.KeyboardButton('🛍 Вызвать Яндекс Доставку')
    back_time_call_yandex_btn = types.KeyboardButton('↩️ Добавить товар')
    markup.row(back_time_call_yandex_btn, yandex_call_btn)
    user_vars[user_id]['bascet_true_dostavka'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true_dostavka'] = user_vars[user_id]['bascet_true_dostavka'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n🛒 В корзине: \n{user_vars[user_id]["bascet_true_dostavka"]} \n⠀ \n💰 Сумма: {total}руб')
    bot.send_message(message.chat.id, '\n❗️Оплатите корзину и жмите «🛍 Вызвать Яндекс Доставку» \n\n💳Номер карты: 4916 9896 9587 5962 \n📆Срок действия: 10/27 \n👨Имя/Фамилия: YAUHENIY LN', reply_markup=markup)
def yandex_order_call(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_order_pay_yandex_btn = types.KeyboardButton('↩️ Назад к оплате')
    new_order_btn = types.KeyboardButton('🛍 Готово')
    markup.row(back_order_pay_yandex_btn, new_order_btn)

    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❗️Вызовите Яндекс Доставку(когда наступит время, которое вы указали ранее)по данным ниже:')
    bot.send_message(message.chat.id, '\n🗺Адрес: Свиридова 69 \n🏠Подъезд: 1 \n📞Номер: +375259167481', reply_markup=markup)

    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['user_first_name'] = message.from_user.first_name
    user_vars[user_id]['user_last_name'] = message.from_user.last_name
    user_vars[user_id]['user_username'] = message.from_user.username
    message.chat.id1 = 5482862125
    user_vars[user_id]['bascet_true_dostavka'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true_dostavka'] = user_vars[user_id]['bascet_true_dostavka'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id1, f'Заказ от {user_vars[user_id]["user_first_name"]} {user_vars[user_id]["user_last_name"]}({user_vars[user_id]["user_username"]})\n\n🛒 В корзине: \n{user_vars[user_id]["bascet_true_dostavka"]} \n\n⏳ Время Яндекс Доставки: {user_vars[user_id]["time_yandex"]} \n\n💰 Сумма: {total}руб')
    










def pochta(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n💬Отправка белпочтой \n\n💬Почтовые сборы 5р \n\n💬Отправка на следующий день после заказа \n\n💬Отправка наложенным(оплата за товар и доставку при получении)')
    adres_msg = bot.send_message(message.chat.id, '❗️Напишите адрес: \n❗️Пример: «Минский район, аг.Осиповичи, ул.Московская 3, кв.2»',reply_markup=markup)
    bot.register_next_step_handler(adres_msg, adress_pochta)

def adress_pochta(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['adress_pochta'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    adress_pochta_msg = bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❗️Напишите ФИО:', reply_markup=markup)
    bot.send_message(message.chat.id, '\n❗️Пример: «Кузнецов Василий Иванович»')
    bot.register_next_step_handler(adress_pochta_msg, FIO)
def FIO(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['fio'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    fio_msg = bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❗️Напишите почтовый код:', reply_markup=markup)
    bot.send_message(message.chat.id, '\n❗️Пример: «247654»')
    bot.register_next_step_handler(fio_msg, code_pochta)
def code_pochta(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['code_pochta'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    space = types.KeyboardButton('⠀')
    markup.row(space)
    code_pochta_msg = bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❗️Напишите контактный номер:', reply_markup=markup)
    bot.send_message(message.chat.id, '\n❗️Пример: «+375259167485»')
    bot.register_next_step_handler(code_pochta_msg, telephon_number_pochta)
def telephon_number_pochta(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['telephon_number_pochta'] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    next = types.KeyboardButton('🛍 Продолжить⠀⠀')
    clear_dostavka = types.KeyboardButton('❌ Стереть⠀⠀⠀')
    markup.row(clear_dostavka, next)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n🗺Адрес: {user_vars[user_id]["adress_pochta"]}')
    bot.send_message(message.chat.id, f'\n👨‍🦰ФИО: {user_vars[user_id]["fio"]}')
    bot.send_message(message.chat.id, f'\n🏣Почтовый код: {user_vars[user_id]["code_pochta"]}')
    bot.send_message(message.chat.id, f'\n📞Контактный номер: {user_vars[user_id]["telephon_number_pochta"]}', reply_markup=markup)
def clear_pochta(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['adress_pochta'] = ""
    user_vars[user_id]['fio'] = ""
    user_vars[user_id]['code_pochta'] = ""
    user_vars[user_id]['telephon_number_pochta'] = ""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_tel_numb_btn = types.KeyboardButton('↩️ К почте')
    markup.row(back_tel_numb_btn)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n❌Адрес стёрт \n\n❌ФИО стёрто \n\n❌Код стёрт \n\n❌Телефон стёрт',  reply_markup=markup)



def itogo_pochta(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Добавить товар')
    next = types.KeyboardButton('🛍 Заказать⠀⠀')
    markup.row(back_btn, next)
    user_vars[user_id]['bascet_true_pochta'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true_pochta'] = user_vars[user_id]['bascet_true_pochta'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id, f'\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n🛒 В корзине: \n{user_vars[user_id]["bascet_true_pochta"]} \n⠀ \n🗺 Адрес: {user_vars[user_id]["adress_pochta"]} \n👨‍🦰 ФИО: {user_vars[user_id]["fio"]} \n🏣 Почтовый код: {user_vars[user_id]["code_pochta"]} \n📞Контактный номер: {user_vars[user_id]["telephon_number_pochta"]} \n⠀ \n💰 Сумма: {total}руб + 5руб', reply_markup=markup)
def order_send_pochta(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    user_vars[user_id]['user_first_name'] = message.from_user.first_name
    user_vars[user_id]['user_last_name'] = message.from_user.last_name
    user_vars[user_id]['user_username'] = message.from_user.username
    message.chat.id1 = 5482862125
    user_vars[user_id]['bascet_true_pochta'] = ",\n".join(user_vars[user_id]['bascet'])
    user_vars[user_id]['bascet_true_pochta'] = user_vars[user_id]['bascet_true_pochta'].strip("[]").strip("''").replace("', '", " 💰")
    total = 0
    for element in user_vars[user_id]['money']:
        if isinstance(element, int):
            total = int(total) + int(element)
    bot.send_message(message.chat.id1, f'Заказ от {user_vars[user_id]["user_first_name"]} {user_vars[user_id]["user_last_name"]}({user_vars[user_id]["user_username"]})\n\n🛒 В корзине: \n{user_vars[user_id]["bascet_true_pochta"]} \n\n🗺 Адрес: {user_vars[user_id]["adress_pochta"]} \n👨‍🦰 ФИО: {user_vars[user_id]["fio"]} \n🏣 Почтовый код: {user_vars[user_id]["code_pochta"]} \n📞Контактный номер: {user_vars[user_id]["telephon_number_pochta"]} \n\n💰 Сумма: {total}руб + 5руб')







def next(message):
    user_id = message.from_user.id
    if user_id not in user_vars:
        user_vars[user_id] = {}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ty_btn = types.KeyboardButton('🛍 Новый заказ')
    markup.row(ty_btn)
    bot.send_message(message.chat.id, "\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \nЗаказ оформлен ✅\nСпасибо, что вы с нами 🥰", reply_markup=markup)
    user_vars[user_id]['bascet'].clear()


def end(message):
    welcome(message)



def manager(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_btn = types.KeyboardButton('↩️ Назад⠀')
    markup.row(back_btn)
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n👨Евгений Менеджер «Ну, подымим!» @nupodymym1', reply_markup=markup)




def dance_emoji(message):
    bot.send_message(message.chat.id, 'ᕕ( ᐛ )ᕗ')
def rage_emoji(message):
    bot.send_message(message.chat.id, '╯⁠°⁠□⁠°⁠）⁠╯⁠︵⁠ ⁠┻⁠━⁠┻')
def love_emoji(message):
    bot.send_message(message.chat.id, '(⁠◍⁠•⁠ᴗ⁠•⁠◍⁠)⁠❤')    
def wolf_emoji(message):
    bot.send_message(message.chat.id, 'ฅ^•ﻌ•^ฅ')
def crazy_wolf_emoji(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEKpOBlQFzmGc8OPn8AAWsd5bAzCjMjNXcAAgEnAAKnUjlIQORkrOtnAZozBA')
def secret_jew_emoji(message):
    bot.send_message(message.chat.id, '⠀⠀⠀┏━┓')
    bot.send_message(message.chat.id, '━━━━━━━━━')
    bot.send_message(message.chat.id, '⠀ﾐΘc_Θ-ﾐ')




@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, '\n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \n⠀ \nЯ бот - у меня нет возможности просматривать фото :( обратитесь к менеджеру')


# Запуск бота
while True:
    try: bot.polling(none_stop=True)
    except Exception as ex: print (ex)