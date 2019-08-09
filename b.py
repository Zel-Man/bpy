import webbrowser
import time
import datetime
import sqlite3
import vk_api
import time
import random

token = "51eca2cce3037f212b721eebb87a3087cf574ae4e415dd857247de7e309b7fec9bd4f7b29b44952fb17da"

vk = vk_api.VkApi(token=token)

vk._auth_token()

def say(txt):
    vk.method("messages.send",
              {"peer_id": id, "message": txt, "random_id": random.randint(1, 2147483647)})

def sayb(txtd):
    vk.method("messages.send",
              {"peer_id": chat_id, "message": txtd, "random_id": random.randint(1, 2147483647)})

nam = "none"

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            nm = vk.method("users.get",
                           {"user_ids": id, "fields": "first_name" "last_name", "name_case": "nom"})

            if body.lower() == "начать":
                nam = nm[0]['first_name'] + " " + nm[0]['last_name']
                fm(str(nm))
            elif body.lower() == "привет":
                say("Привет " + nam + '!')
                sayb("Привет " + nam + '!')

            elif body.lower() == "/help":
                say("Нисего нимагу!")

            else:
                say("Я тебя не понимаю!")
    except Exception as E:
        time.sleep(1)
