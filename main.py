import telebot
import requests

ACCESS_TOKEN = ""

bot = telebot.TeleBot(ACCESS_TOKEN)


@bot.message_handler(commands=["joke"])
def start(message):
    response = requests.get(url="https://v2.jokeapi.dev/joke/Any")
    joke = response.json()
    print(joke)
    if joke["type"] == "twopart":
        bot.send_message(message.chat.id, f"{joke['setup']} \n<span class='tg-spoiler'>{joke['delivery']} </span>",
                         parse_mode="html")
    elif joke["type"] == "single":
        bot.send_message(message.chat.id, f"{joke['joke']}", parse_mode="html")
    else:
        bot.send_message(message.chat.id, f"404 Joke was not found.")


bot.polling(none_stop=True)
