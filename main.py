from telebot import types
import telebot
import time
import math
from math import sqrt


bot = telebot.TeleBot("5102595283:AAHnkE5Xl_9T0Oph0Jw54qyRiuopXkHmVhs")
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Калькулятор 🧮")
    btn2 = types.KeyboardButton("Алгебра 🔢")
    btn3 = types.KeyboardButton("Геометрия 📏")
    btn4 = types.KeyboardButton("Информатика 🖥")
    btn5 = types.KeyboardButton("Физика ⚛️")
    bot.send_message(message.chat.id, text="Привет!Я умный бот, способный быстро помогать тебе с решением различных заданий.Внимательно ознакомься с командами, на которые я откликаюсь и можем начинать.")
    time.sleep(5)
    bot.send_message(message.chat.id, text=f"Список команд:\n /menu - выход в любой момент в главное меню\n /help - различные подсказки в случае незнание команд\n /calc - быстро перейти в раздел калькулятора\n /give_calc - получить программу калькулятор, для работы без интернета\n ")
    time.sleep(3)
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text=f"{message.from_user.first_name}, а вот ты и в главном меню.Спасибо, что ознакомился с правилами.Можем начинать работать!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def command(message):
    if(message.text == "/menu"):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton("Калькулятор 🧮")
        btn2 = types.KeyboardButton("Алгебра 🔢")
        btn3 = types.KeyboardButton("Геометрия 📏")
        btn4 = types.KeyboardButton("Информатика 🖥")
        btn5 = types.KeyboardButton("Физика ⚛️")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Вы в главном меню", reply_markup=markup)
    
    elif (message.text == "Калькулятор 🧮") or (message.text == "/calc"):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton("Сложение чисел: a+b")
        btn2 = types.KeyboardButton("Вычитание чисел: a−b")
        btn3 = types.KeyboardButton("Деление чисел: a÷b")
        btn4 = types.KeyboardButton("Умножение чисел: a·b")
        btn5 = types.KeyboardButton("Возведение в степень: a^i")
        btn6 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_video(message.chat.id, 'https://tenor.com/view/osita-osita-iheme-nigerian-nollywood-calculating-gif-16142281', None)
        bot.send_message(message.chat.id, text="Вы перешли в раздел: 🙶Калькулятор🙷. Для начала выберите математическую операцию, нажав на кнопку.", reply_markup=markup)
    
    # Калькулятор 
    elif (message.text == "Сложение чисел: a+b") or (message.text == "/plus"):
        a = bot.send_message(message.chat.id, text="Гуд! Самое время ввести число a:")
        bot.register_next_step_handler(a, calcA)

    elif (message.text == "Вычитание чисел: a−b") or (message.text == "/minus"):
        a = bot.send_message(message.chat.id, text="Все по плану! Самое время ввести число a:")
        bot.register_next_step_handler(a, calcA_raznost)

    elif (message.text == "Деление чисел: a÷b") or (message.text == "/division"):
        a = bot.send_message(message.chat.id, text="Сейчас посчитаем!Вводи число a:")
        bot.register_next_step_handler(a, calcA_division)

    elif (message.text == "Умножение чисел: a·b") or (message.text == "/division"):
        a = bot.send_message(message.chat.id, text="Хороший выбор!Вводи число a:")
        bot.register_next_step_handler(a, calcA_Multiplication)

    elif (message.text == "Возведение в степень: a^i") or (message.text == "/division"):
        a = bot.send_message(message.chat.id, text="ИЗИ!Число а пожалуйста:")
        bot.register_next_step_handler(a, calcA_Degree)

    elif (message.text == "/give_calc"):
        bot.send_message(message.chat.id, text="Сейчас пришлю калькулятор")
        time.sleep(2)
        bot.send_document(message.chat.id, open(r'file/Calculator.exe', 'rb'))

        bot.send_video(message.chat.id, 'https://i.gifer.com/1NCD.gif', None)
        bot.send_message(message.chat.id, text="Пользуйся на здоровье!")

    # Алгебра
    elif (message.text == "Алгебра 🔢") or (message.text == "/algebra"):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton("Найти дискириминант")
        btn2 = types.KeyboardButton("Еще что то ")
        btn3 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1, btn2, btn3)

        bot.send_video(message.chat.id, 'https://tenor.com/view/calculation-math-hangover-allen-zach-galifianakis-gif-6219070', None)
        bot.send_message(message.chat.id, text="Вы перешли в раздел: 🙶Алгебра🙷. В данном разделе я помогу вам с решением некторых уравнений, функций, а также задач.", reply_markup=markup)

    elif (message.text == "Найти дискириминант"):
        a = bot.send_message(message.chat.id, text="Сейчас найдем. Введите только коффицент a: ")
        bot.register_next_step_handler(a, coffA_discriminant)    


    # Геометрия
    elif (message.text == "Геометрия 📏") or (message.text == "/geometry"):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton("Нахождение катетов, гипотенузы.Теорема Виета")
        btn2 = types.KeyboardButton("Еще что то")   
        btn3 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1, btn2, btn3)

        bot.send_video(message.chat.id, 'https://i.gifer.com/9FGO.gif', None)
        bot.send_message(message.chat.id, text=f"Вы перешли в раздел: 🙶Геометрия🙷. В данном разделе я помогу вам с нахождением гипотенузы по теореме Виета, а также различных задач, связанные с геометрией.", reply_markup=markup)

    elif (message.text == "Нахождение катетов, гипотенузы.Теорема Виета"):
        a = bot.send_message(message.chat.id, text="Хорошо.Что нужно найти?(гипотенузу, катет): ")
        bot.register_next_step_handler(a, pifagor_Proverka)    

    elif (message.text == "Гипотенуза") or (message.text == "Гипотенузы"):
        bot.send_message(message.chat.id, text="Хорошо")



    # Ифнорматика
    elif (message.text == "Информатика 🖥") or (message.text == "/info"):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton("Типы данных")
        btn2 = types.KeyboardButton("Еще что то")   
        btn3 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1, btn2, btn3)

        bot.send_video(message.chat.id, 'https://i.gifer.com/V4WN.gif', None)
        bot.send_message(message.chat.id, text=f"Вы перешли в раздел: 🙶Информатикка🙷. В данном разделе вы можете переводить числа, в различные системы измерения", reply_markup=markup)

    elif (message.text == "Типы данных") or (message.text == "/type_data"):
        global type_but
        type_but = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton("Бит")
        btn2 = types.KeyboardButton("Байт")   
        btn3 = types.KeyboardButton("КилоБайт")
        btn4 = types.KeyboardButton("МегаБайт")      
        btn5 = types.KeyboardButton("Назад 🔙")
        type_but.add(btn1, btn2, btn3, btn4, btn5)

        a = bot.send_message(message.chat.id, text="Выберите тип данных 1-ого числа: ", reply_markup=type_but)
        bot.register_next_step_handler(a, typeData_info)  



    elif message.text == "Назад 🔙":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        btn1 = types.KeyboardButton("Калькулятор 🧮")
        btn2 = types.KeyboardButton("Алгебра 🔢")
        btn3 = types.KeyboardButton("Геометрия 📏")
        btn4 = types.KeyboardButton("Информатика 🖥")
        btn5 = types.KeyboardButton("Физика ⚛️")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Вы в главном меню", reply_markup=markup)

    elif (message.text == "/help"):
        bot.send_message(message.chat.id, text=f"Что-то ты запутался. Хочу просвятить тебя.\n /menu - выход в любой момент в главное меню\n /help - различные подсказки в случае незнание команд\n /calc - быстро перейти в раздел калькулятора\n /give_calc - получить программу калькулятор, для работы без интернета\n")




# сложение 
def calcA(message):
    global a
    a = float(message.text)
    b = bot.send_message(message.chat.id, text="Хорошо, продолжаем! Теперь введите число b:")
    bot.register_next_step_handler(b, calcB_summa)

def calcB_summa(message):
    global b
    b = float(message.text)
    global c
    c = a + b

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Вернутся назад 🔙")
    markup.add(btn1)

    bot.send_message(message.chat.id, text=f"Посчитав, я выяснил.Ответ будет: {c}")
    time.sleep(1.5)
    bot.send_message(message.chat.id, text=f"Хотите узнать решение?1) действие: определил коффицент a. Он равен = {a}.\n2) действие: определил коффицент b. Данный коффицент будет равнятся = {b}\n3) действие: сложил данный коффиценты: {a} + {b} = {c}.\nОтвет: {c}", reply_markup=markup)
    bot.send_video(message.chat.id, 'https://tenor.com/view/pointing-laughing-you-lol-youre-funny-gif-7517608', None)
# -------------------------

# минус
def calcA_raznost(message):
    global a
    a = float(message.text)
    b = bot.send_message(message.chat.id, text="Зафиксировал! Теперь введите число b:")
    bot.register_next_step_handler(b, calcB_raznost)

def calcB_raznost(message):
    global b
    b = float(message.text)
    global c
    c = a - b    
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Вернутся назад 🔙")
    markup.add(btn1)

    bot.send_message(message.chat.id, text=f"Я плохо сооброжаю в последнее время плохо, но это я смог посчитать.Ответ будет: {c}")
    time.sleep(1.5)
    bot.send_message(message.chat.id, text=f"Хотите узнать решение?1) действие: определил коффицент a. Он равен = {a}.\n2) действие: определил коффицент b. Данный коффицент будет равнятся = {b}\n3) действие: вычтел данный коффиценты: {a} - {b} = {c}.\nОтвет: {c}", reply_markup=markup)
    bot.send_video(message.chat.id, 'https://tenor.com/view/pointing-laughing-you-lol-youre-funny-gif-7517608', None)
# ----------------

# Деление
def calcA_division(message):
    global a
    a = float(message.text)
    b = bot.send_message(message.chat.id, text="Принял! Теперь введите число b:")
    bot.register_next_step_handler(b, calcB_division)    

def calcB_division(message):
    global b
    b = float(message.text)
    global c
    c = a / b    
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Вернутся назад 🔙")
    markup.add(btn1)    

    bot.send_message(message.chat.id, text=f"Мне кажется.Ответ будет: {c}")
    time.sleep(1.5)
    bot.send_message(message.chat.id, text=f"Хотите узнать решение?1) действие: определил коффицент a. Он равен = {a}.\n2) действие: определил коффицент b.Коффицент будет равнятся = {b}\n3) действие: разделил данный коффиценты: {a} ÷ {b} = {c}.\nОтвет: {c}", reply_markup=markup)
    bot.send_video(message.chat.id, 'https://tenor.com/view/pointing-laughing-you-lol-youre-funny-gif-7517608', None)
# ----------------

# Уможение
def calcA_Multiplication(message):
    global a
    a = float(message.text)
    b = bot.send_message(message.chat.id, text="Записал! Введите число b:")
    bot.register_next_step_handler(b, calcB_Multiplication)    

def calcB_Multiplication(message):
    global b
    b = float(message.text)
    global c
    c = a * b    
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Назад 🔙")
    markup.add(btn1)    

    bot.send_message(message.chat.id, text=f"I'm ready.Ответ будет: {c}")
    time.sleep(1.5)
    bot.send_message(message.chat.id, text=f"Может решение? 1) действие: определил коффицент a. Он равен = {a}.\n2) действие: определил коффицент b.Коффицент будет равнятся = {b}\n3) действие: умножил данный коффиценты: {a} · {b} = {c}.\nОтвет: {c}", reply_markup=markup)        
    bot.send_video(message.chat.id, 'https://tenor.com/view/pointing-laughing-you-lol-youre-funny-gif-7517608', None)
# ----------------

# Степень
def calcA_Degree(message):
    global a
    a = float(message.text)
    b = bot.send_message(message.chat.id, text="Супер! Введите в какую степень хотите возвести:")
    bot.register_next_step_handler(b, calcB_Degree)

def calcB_Degree(message):
    global b
    b = float(message.text)
    global c
    c = a ** b    
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("Назад 🔙")
    markup.add(btn1)    

    bot.send_message(message.chat.id, text=f"Ответ в студию, будет: {c}")
    time.sleep(1.5)
    bot.send_message(message.chat.id, text=f"Как это считается?! Легко: 1) действие: определил коффицент a. Он равен = {a}.\n2) действие: определил коффицент b.Коффицент, позволяющий понять, сколько раз нужно умножить коффицент: а, на само себя.Коффицент: b будет равнятся = {b}\n3) действие: возвел в степень: {a} ^ {b} = {c}.\nОтвет: {c}", reply_markup=markup)                
    bot.send_video(message.chat.id, 'https://tenor.com/view/pointing-laughing-you-lol-youre-funny-gif-7517608', None)
# ----------------

# Алгебра. Коффиценты
def coffA_discriminant(message):
    global a
    a = int(message.text)
    b = bot.send_message(message.chat.id, text="Теперь коффицент b: ")
    bot.register_next_step_handler(b, coffB_discriminant)


def coffB_discriminant(message):
    global b
    b = int(message.text)
    c = bot.send_message(message.chat.id, text="Шикарно! Теперь хочу увидеть коффицент c: ")
    bot.register_next_step_handler(c, coffC_discriminant)

def coffC_discriminant(message):
    c = int(message.text)

    discr = b ** 2 - (4 * a * c)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        bot.send_message(message.chat.id, text=f"Дискриминант равен = {discr}\nx1 = {x1}\n x2 = {x2}")
    elif discr == 0:
        x = -b / (2 * a)
        bot.send_message(message.chat.id, text=f"Дискриминант равен = {discr}\nДискриминант равен 0, значит корень будет один:\n x = {x}")
        time.sleep(2)
        bot.send_video(message.chat.id, 'https://tenor.com/view/pointing-laughing-you-lol-youre-funny-gif-7517608', None)


# Геометрия
def pifagor_Proverka(message):
    request = message.text

    if (request == "Гипотенуза") or (request == "Гипотенузу") or (request == "гипотенуза") or (request == "гипотенузу"):
        a = bot.send_message(message.chat.id, text="Вы хотите найти гипотенузу.Введите сторону первого катета: ")
        bot.register_next_step_handler(a, pifagor_katet)

def pifagor_katet(message):
    global katet1
    katet1 = message.text
    b = bot.send_message(message.chat.id, text="Уловил. Теперь сторону второго катета: ")
    bot.register_next_step_handler(b, pifagor_katet)

def pifagor_Katet2(message):
    katet2 = message.text    
    gip2= (katet1 ** 2) + (katet2 ** 2)
    gip1 = sqrt(gip2)
    print(gip1)

# Информатика
def typeData_info(message):
    global a
    a = message.text
    global b
    b = bot.send_message(message.chat.id, text="GOOD! Во что хотите переевести?", reply_markup=type_but)
    bot.register_next_step_handler(b, typeData_infoAns)

def typeData_infoAns(message):
    if (a == "Бит") and (b == "Байт"):
        bot


bot.polling(none_stop=True)