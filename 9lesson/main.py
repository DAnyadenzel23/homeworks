import telebot
from telebot import types


bot = telebot.TeleBot("6085283770:AAGIuLASO3WkuXl9NCPYGS1yBSqfMseiEjk")
num_1 = ''
num_2 = ''
sign = ''
result = ''
@bot.message_handler(commands=['start'])
def start(message):

    msg = bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + ', я бот-калькулятор\n Введите число')
    bot.register_next_step_handler(msg,proc_num1)


def proc_num1(message):
    try:
        global num_1
        num_1 = float(message.text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton('+')
        btn2 = types.KeyboardButton('-')
        btn3 = types.KeyboardButton('*')
        btn4 = types.KeyboardButton('/')
        markup.add(btn1,btn2,btn3,btn4)

        msg = bot.send_message(message.chat.id, 'Выберите операцию',reply_markup=markup)
        bot.register_next_step_handler(msg,proc_oper)
    except Exception as e:
        bot.reply_to(message, 'Ошибочка ввода0')

def proc_oper(message):
    try:
        global sign
        sign = message.text
        markup = types.ReplyKeyboardRemove(selective = False)
        msg = bot.send_message(message.chat.id, 'ведите второе число', reply_markup=markup)
        bot.register_next_step_handler(msg, proc_num_2)
    except Exception as p:
        bot.reply_to(message, 'Ошибочка ввода1')

def proc_num_2(message):
    try:
        global num_2
        num_2 = float(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Результат')
        markup.add(btn)
        msg = bot.send_message(message.chat.id, 'Показать результат?', reply_markup=markup)
        bot.register_next_step_handler(msg, proc_result)
    except Exception as e:
        bot.reply_to(message, 'Ошибочка ввода2')

def proc_result(message):
    try:
        global result
        result = eval(str(num_1) + sign + str(num_2))
        markup = types.ReplyKeyboardRemove(selective = False)
        if message.text == 'Результат':
            bot.send_message(message.chat.id, print_res(), reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'ХЗ что случилось')

def print_res():

    return 'Результат: ' + str(num_1) + ' ' + sign + ' ' + str(num_2) + '=' + str(result)


if __name__=='__main__':
    bot.polling(none_stop=True, interval=0)

