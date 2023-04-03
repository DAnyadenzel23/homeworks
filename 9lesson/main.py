import telebot
from telebot import types


bot = telebot.TeleBot("6085283770:AAGIuLASO3WkuXl9NCPYGS1yBSqfMseiEjk")

@bot.message_handler(commands=['start'])
def start(message):
    bot.clear_step_handler(message)
    msg = bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + ', я бот-калькулятор\n Введите число')
    bot.register_next_step_handler(msg,proc_num1)


def proc_num1(message):
    try:
        num_1 = message.text
        num_1 = num_1.replace(',', '.')
        num_1 = float(num_1)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton('+')
        btn2 = types.KeyboardButton('-')
        btn3 = types.KeyboardButton('*')
        btn4 = types.KeyboardButton('/')
        markup.add(btn1,btn2,btn3,btn4)

        msg = bot.send_message(message.chat.id, 'Выберите операцию',reply_markup=markup)
        bot.register_next_step_handler(msg,proc_oper,num_1)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вводите только первое число!')
        bot.register_next_step_handler(message, proc_num1)

def proc_oper(message,num_1):

    sign = message.text
    markup = types.ReplyKeyboardRemove(selective = False)
    msg = bot.send_message(message.chat.id, 'Введите второе число', reply_markup=markup)
    bot.register_next_step_handler(msg, proc_num_2,num_1, sign)

def proc_num_2(message,num_1,sign):
    try:
        num_2 = message.text
        num_2 = num_2.replace(',', '.')
        num_2 = float(num_2)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Показать результат!')
        markup.add(btn)
        msg = bot.send_message(message.chat.id, 'Показать результат?', reply_markup=markup)
        bot.register_next_step_handler(msg, proc_result,num_1, sign, num_2)
    except ValueError:
        bot.reply_to(message, 'Внимательнее, дружище! Вводи именно числа.')
        bot.clear_step_handler(message)
        msg = bot.send_message(message.chat.id, 'Введите второе число')
        bot.register_next_step_handler(msg, proc_num_2,num_1, sign)

def proc_result(message,num_1,sign,num_2):

    result = eval(str(num_1) + sign + str(num_2))
    markup = types.ReplyKeyboardRemove(selective = False)
    if message.text == 'Показать результат!':
        bot.send_message(message.chat.id, print_res(num_1,sign,num_2,result), reply_markup=markup)
        start(message)

def print_res(num_1,sign,num_2,result):

    return 'Результат: ' + str(num_1) + ' ' + sign + ' ' + str(num_2) + '=' + str(result)


if __name__=='__main__':
    bot.polling(none_stop=True, interval=0)