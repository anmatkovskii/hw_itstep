import telebot
import os.path
from random import choice
from telebot import types

config = {
    'name': 'ITStep Financier Bot',
    'token': '5700624482:AAFB_mD7vDK0L1017s2v0PDd51Saa5FzoFE'
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton("Add earnings")
keyboard.add(button)
button = types.KeyboardButton("Add expences")
keyboard.add(button)
button = types.KeyboardButton("See financial report")
keyboard.add(button)
button = types.KeyboardButton("Clear all data")
keyboard.add(button)

yes_no_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton("Yes")
yes_no_keyboard.add(button)
button = types.KeyboardButton("No, go back to menu")
yes_no_keyboard.add(button)


bot = telebot.TeleBot(config["token"])


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome! What would you like to do?", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Add earnings":
        question = bot.send_message(message.chat.id, "What's the amount? (Type anithyng to go back to choice menu)")
        bot.register_next_step_handler(question, add_earning)
    elif message.text == "Add expences":
        question = bot.send_message(message.chat.id, "What's the amount? (Type anithyng to go back to choice menu)")
        bot.register_next_step_handler(question, add_expence)
    elif message.text == "See financial report":
        form_report(message)
    elif message.text == "Clear all data":
        question = bot.send_message(message.chat.id, "❗️❗️❗️ALL DATA WOULD BE LOST FOREVER❗️❗️❗️\n               "
                                                     "PROCEED?",
                                    reply_markup=yes_no_keyboard)
        bot.register_next_step_handler(question, clear_table)


def clear_table(message):
    if message.text == "Yes":
        with open("report.txt", "r") as file:
            data = file.read()
            strings = data.splitlines()
        with open("report.txt", "w") as file:
            file.write(strings[0]+"\n")
            file.write(strings[1])
            bot.send_message(message.chat.id, "Done")
            bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)


def form_report(message):
    with open("report.txt", "r") as file:
        data = file.read()
        strings = data.splitlines()
        del strings[1]
        del strings[0]
        list_one = []
        for i in strings:
            x = i.split("   |   ")
            list_one.append(x)
        record_sum = 0
        for i in list_one:
            record_sum += float(i[1])
    with open("report.txt", "w") as file:
        end_report = f" Sum  |   {record_sum}   |"
        file.write(data)
        file.write("\n--------------------------------\n")
        file.write(end_report)
    with open("report.txt", "r") as file:
        bot.send_document(message.chat.id, file)
    with open("report.txt", "w") as file:
        file.write(data)
    question = bot.send_message(message.chat.id, "Do you need to delete any records?", reply_markup=yes_no_keyboard)
    def delete(msg):
        if msg.text == "Yes":
            index_question = bot.send_message(message.chat.id, "What record do you want to delete? (Enter "
                                                               "ID)\nCareful, any deleted information would be lost "
                                                               "forever!!!")
            def end_delete(msg):
                def check_int(msg):
                    try:
                        int(msg.text)
                        return True
                    except ValueError:
                        return False

                if check_int(msg):
                    delete_id = int(msg.text)
                    with open("report.txt", "r") as file:
                        data = file.read()
                        strings = data.splitlines()
                        for i in strings[2:]:
                            if i.startswith(str(delete_id)):
                                strings.remove(i)
                    with open("report.txt", "w") as file:
                        for j in strings:
                            file.write(j + "\n")
                    bot.send_message(message.chat.id, "Done")
                    bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)
                else:
                    bot.send_message(message.chat.id, f"Wrong data input, try again (Only digits(0-9) allowed)")
                    bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)
            bot.register_next_step_handler(index_question, end_delete)
        else:
            bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)
    bot.register_next_step_handler(question, delete)


def add_expence(message):
    def check_float(message):
        try:
            float(message.text)
            return True
        except ValueError:
            return False

    if check_float(message):
        with open("report.txt", "r") as file:
            data = file.read()
            strings = data.splitlines()
            file.close()

        id_list = []
        for i in strings[2:]:
            integer_id = int(i[:5])
            id_list.append(integer_id)
        new_id = 1
        while True:
            if new_id in id_list:
                new_id += 1
            elif new_id not in id_list:
                break

        end_id = ""
        if len(str(new_id)) == 1:
            end_id = f"{new_id}    "
        elif len(str(new_id)) == 2:
            end_id = f"{new_id}   "
        elif len(str(new_id)) == 3:
            end_id = f"{new_id}  "
        elif len(str(new_id)) == 4:
            end_id = f"{new_id} "
        elif len(str(new_id)) == 5:
            end_id = f"{new_id}"
        else:
            bot.send_message(message.chat.id, "You have reached the maximal amount of records")
        category = bot.send_message(message.chat.id, "What's the category of this operation?")
        def get_category(msg):
            end_report = f"{str(end_id)}|   -{message.text}   |   {msg.text}"
            with open("report.txt", "w") as file:
                file.write(data)
                file.write("\n")
                file.write(end_report)
                bot.send_message(message.chat.id, f"Successfully added a record. ID = {end_id}")
                bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)
        bot.register_next_step_handler(category, get_category)
    else:
        bot.send_message(message.chat.id, f"Wrong data input, try again (Only digits(0-9) and '.' allowed)")
        bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)


def add_earning(message):
    def check_float(message):
        try:
            float(message.text)
            return True
        except ValueError:
            return False

    if check_float(message):
        with open("report.txt", "r") as file:
            data = file.read()
            strings = data.splitlines()
            file.close()

        id_list = []
        for i in strings[2:]:
            integer_id = int(i[:5])
            id_list.append(integer_id)
        new_id = 1
        while True:
            if new_id in id_list:
                new_id += 1
            elif new_id not in id_list:
                break
        end_id = ""
        if len(str(new_id)) == 1:
            end_id = f"{new_id}    "
        elif len(str(new_id)) == 2:
            end_id = f"{new_id}   "
        elif len(str(new_id)) == 3:
            end_id = f"{new_id}  "
        elif len(str(new_id)) == 4:
            end_id = f"{new_id} "
        elif len(str(new_id)) == 5:
            end_id = f"{new_id}"
        else:
            bot.send_message(message.chat.id, "You have reached the maximal amount of records")
        category = bot.send_message(message.chat.id, "What's the category of this operation?")
        def get_category(msg):
            end_report = f"{str(end_id)}|   {message.text}   |   {msg.text}"
            with open("report.txt", "w") as file:
                file.write(data)
                file.write("\n")
                file.write(end_report)
                file.close()
                bot.send_message(message.chat.id, f"Successfully added a record. ID = {end_id}")
                bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)
        bot.register_next_step_handler(category, get_category)
    else:
        bot.send_message(message.chat.id, f"Wrong data input, try again (Only digits(0-9) and '.' allowed)")
        bot.send_message(message.chat.id, "What would you like to do?", reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)