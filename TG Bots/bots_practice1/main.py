import telebot
import os.path
from random import choice
from telebot import types

config = {
    'name': 'itstep_practice_bot',
    'token': '5879283468:AAFSZVH6zDPeN2eqIoLZCpvDKS4IvbETG6c'
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton("Hello")
keyboard.add(button)
button = types.KeyboardButton("Magic Ball")
keyboard.add(button)
button = types.KeyboardButton("Calculate")
keyboard.add(button)
button = types.KeyboardButton("Stats")
keyboard.add(button)

# keyboard_stats = types.ReplyKeyboardMarkup(resize_keyboard=True)
# button = types.KeyboardButton("Words")
# keyboard_stats.add(button)
# button = types.KeyboardButton("Symbols")
# keyboard_stats.add(button)
# button = types.KeyboardButton("Digits")
# keyboard_stats.add(button)
# button = types.KeyboardButton("Vowels")
# keyboard_stats.add(button)
# button = types.KeyboardButton("Consonants")
# keyboard_stats.add(button)
# button = types.KeyboardButton("Punctuation marks")
# keyboard_stats.add(button)

bot = telebot.TeleBot(config["token"])


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "/start", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Magic Ball":
        question = bot.send_message(message.chat.id, "What's your question?")
        bot.register_next_step_handler(question, magic_ball)

    elif message.text == "Hello":
        bot.send_message(message.chat.id, f"Hello, {message.chat.first_name}")

    elif message.text == "Calculate":
        question = bot.send_message(message.chat.id, "What's your equation?")
        bot.register_next_step_handler(question, calculator)

    elif message.text == "Stats":
        # stats_choose = bot.send_message(message.chat.id, "What type of stats do you need?", reply_markup=keyboard_stats)
        # bot.register_next_step_handler(stats_choose, stats_type)
        question = bot.send_message(message.chat.id, "What's your message?")
        bot.register_next_step_handler(question, stats)

    elif message.text == "Pal":
        question = bot.send_message(message.chat.id, "What's your word?")
        bot.register_next_step_handler(question, check_palindrome)

    elif message.text == "Even":
        question = bot.send_message(message.chat.id, "What's your number?")
        bot.register_next_step_handler(question, check_even)

    elif message.text == "Login":
        question = bot.send_message(message.chat.id, "Enter your login and password: [Login Password]")
        bot.register_next_step_handler(question, auth)


def auth(message):
    try:
        log_and_pass = message.text.split(" ")
        with open("logins.txt", "r") as file:
            data = file.read()
            if message.text in data:
                bot.send_message(message.chat.id, "Login successful")
            elif log_and_pass[0] in data:
                bot.send_message(message.chat.id, "Wrong password")
            else:
                question = bot.send_message(message.chat.id, "User does not exist. Would you like to register? [y/n]")
                def reg_or_not(message):
                    if message.text == "y":
                        question2 = bot.send_message(message.chat.id, "Enter new login and password: [Login Password]")
                        def reg(message):
                            log_and_pass2 = message.text.split(" ")
                            if len(log_and_pass2) == 2:
                                with open("logins.txt", "r") as file:
                                    data = file.read()
                                with open("logins.txt", "w") as file:
                                    file.write(data)
                                    file.write(message.text + "\n")
                                bot.send_message(message.chat.id, "Register successful")
                            else:
                                bot.send_message(message.chat.id, "Wrong register form")
                        bot.register_next_step_handler(question2, reg)

                bot.register_next_step_handler(question, reg_or_not)

    except:
        bot.send_message(message.chat.id, "Error")


def check_palindrome(message):
    word = message.text
    if str(word) == "".join(reversed(word)):
        bot.send_message(message.chat.id, "Palindrome")
    else:
        bot.send_message(message.chat.id, "Not Palindrome")


def check_even(message):
    if int(message.text) % 2 == 0:
        bot.send_message(message.chat.id, "Even")
    elif int(message.text) % 2 == 1:
        bot.send_message(message.chat.id, "Odd")


def stats(message):
    with open("stat.txt", "w") as file:
        file.write(f"Words count: {len(message.text.split(' '))}\n")
        s, d, v, c, p = 0, 0, 0, 0, 0
        for i in message.text.lower():
            if i in "aeiou":
                s += 1
                v += 1
            elif i in "qwrtypsdfghjklmnbvcxz":
                s += 1
                c += 1
            elif i in "0123456789":
                s += 1
                d += 1
            elif i in "?.,'\"!&():;-":
                s += 1
                p += 1
            elif i in " ":
                s += 1
        file.write(f"Symbols count: {s}\n")
        file.write(f"Digits count: {d}\n")
        file.write(f"Vowels count: {v}\n")
        file.write(f"Consonants count: {c}\n")
        file.write(f"Punctuation marks count: {p}\n")
        file.close()
    with open("stat.txt", "r") as file:
        bot.send_document(message.chat.id, file)
        file.close()


def magic_ball(message):
    bot.send_message(message.chat.id, choice(["It is certain.", "It is decidedly so.", "Without a doubt.",
                                              "Yes definitely.", "You may rely on it.", "As I see it, yes.",
                                              "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                                              "Reply hazy, try again.", "Ask again later.", "Cannot predict now.",
                                              "Concentrate and ask again.", "Better not tell you now.",
                                              "Don't count on it.", "My reply is no.", "My sources say no.",
                                              "Outlook not so good.", "Very doubtful."]))


def calculator(message):
    equation = message.text + "!"
    list_of_nums = []
    num = ""
    for i in equation:
        if i in "1234567890.,":
            num += i
        elif i in "+-/*":
            list_of_nums.append(float(num))
            list_of_nums.append(i)
            num = ""
        elif i[-1] == "!":
            list_of_nums.append(float(num))

    if len(list_of_nums) > 3:
        for i in list_of_nums:
            if i == "*":
                index = int(list_of_nums.index(i))
                new_num = float((list_of_nums[index-1]))*float((list_of_nums[index+1]))
                list_of_nums.pop(index+1)
                list_of_nums.pop(index)
                list_of_nums.pop(index-1)
                list_of_nums.insert(index-1, new_num)
            elif i == "/":
                index = int(list_of_nums.index(i))
                new_num = float((list_of_nums[index - 1])) / float((list_of_nums[index + 1]))
                list_of_nums.pop(index + 1)
                list_of_nums.pop(index)
                list_of_nums.pop(index - 1)
                list_of_nums.insert(index - 1, new_num)

        for i in list_of_nums:
            if i == "+":
                index = int(list_of_nums.index(i))
                new_num = float((list_of_nums[index - 1])) + float((list_of_nums[index + 1]))
                list_of_nums.pop(index + 1)
                list_of_nums.pop(index)
                list_of_nums.pop(index - 1)
                list_of_nums.insert(index - 1, new_num)
            elif i == "-":
                index = int(list_of_nums.index(i))
                new_num = float((list_of_nums[index - 1])) - float((list_of_nums[index + 1]))
                list_of_nums.pop(index + 1)
                list_of_nums.pop(index)
                list_of_nums.pop(index - 1)
                list_of_nums.insert(index - 1, new_num)

        if "+" in list_of_nums:
            end_num = str(float(list_of_nums[0])+float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)
        elif "-" in list_of_nums:
            end_num = str(float(list_of_nums[0])-float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)
        elif "*" in list_of_nums:
            end_num = str(float(list_of_nums[0])*float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)
        elif "/" in list_of_nums:
            end_num = str(float(list_of_nums[0])/float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)

    elif len(list_of_nums) == 3:
        if "+" in list_of_nums:
            end_num = str(float(list_of_nums[0])+float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)
        elif "-" in list_of_nums:
            end_num = str(float(list_of_nums[0])-float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)
        elif "*" in list_of_nums:
            end_num = str(float(list_of_nums[0])*float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)
        elif "/" in list_of_nums:
            end_num = str(float(list_of_nums[0])/float(list_of_nums[2]))
            bot.send_message(message.chat.id, end_num)

bot.polling(none_stop=True, interval=0)
