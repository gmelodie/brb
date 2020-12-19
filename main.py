import os
from telethon import TelegramClient, events, sync
from dotenv import load_dotenv


sleeping_txt = "Estou dormindo, respondo quando acordar "
turned_on = False

if __name__ == "__main__":
    load_dotenv(override=True, verbose=True)
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv("API_HASH")
    session_name = os.getenv("SESSION_NAME")


    with TelegramClient(session_name, api_id, api_hash) as client:
        client.send_message('me' , 'BRB online!')

        # /sleep
        # TODO: fix chat
        @client.on(events.NewMessage(pattern='(?i)\/sleep$'))
        async def brb_on_off(event):
            turned_on = not turned_on
            sender = await event.message.get_sender()
            await event.reply(f"BRB on: {turned_on}")

        @client.on(events.NewMessage(incoming=True))
        async def say_brb(event):
            if turned_on == False:
                await event.reply("Não estou dormindo")
                return
            await event.reply(sleeping_txt)

        client.run_until_disconnected()
