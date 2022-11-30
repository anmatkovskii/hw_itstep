import telebot
from random import choice

config = {
    'name': 'itstep_practice_bot',
    'token': '5879283468:AAFSZVH6zDPeN2eqIoLZCpvDKS4IvbETG6c'
}

bot = telebot.TeleBot(config["token"])


@bot.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Magic Ball":
        question = bot.send_message(message.chat.id, "What's your question?")
        bot.register_next_step_handler(question, magic_ball)

    elif message.text == "Hello":
        bot.send_message(message.chat.id, f"Hello, {message.chat.first_name}")


def magic_ball(message):
    bot.send_message(message.chat.id, choice(["It is certain.", "It is decidedly so.", "Without a doubt.",
                                              "Yes definitely.", "You may rely on it.", "As I see it, yes.",
                                              "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                                              "Reply hazy, try again.", "Ask again later.", "Cannot predict now.",
                                              "Concentrate and ask again.", "Better not tell you now.",
                                              "Don't count on it.", "My reply is no.", "My sources say no.",
                                              "Outlook not so good.", "Very doubtful."]))


bot.polling(none_stop=True, interval=0)
