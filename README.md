# brb
Let people know that you're not online on Telegram


## Setup
1. Install the dependencies
```
$ pip install -r requirements.txt
```

2. Start the bot
```
$ python3 main.py
```

2. Login to your telegram account (type in your phone number and the code you receive on the app)

![login-terminal](login.png)

3. Go to your Saved Messages on Telegram, you should see a message saying `BRB online!`

![brb-online-message](online.jpg)

## Usage
Enable the bot when you to to sleep. Go to your Saved Messages and send `/sleep`

![enable-bot-sleep](enable.jpg)

When you wake up, disable it with `/up`

![disable-bot-up](disable.jpg)


## Customization
You can change the default sleeping message to say whatever you like by changing the string `sleeping_txt` on `main.py`
