#(©)CodeXBotz
from os import environ
import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6601011494:AAGMR0i5tlCKITms_7rr2LzZmmAieD_eQ58")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "3393749"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001693231644"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483"))

# #shortenr
# API = environ.get('API','eedc409c6457b8c783019e990dde8fd531b58eca')

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Jayanna:Jayanna2023@yash.tm1c2bd.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "New_Divya_Spandana")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "10"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1365052525 5963138883").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b><code>{filename}</code> \n\n𝐉𝐨𝐢𝐧 -> <a href='https://telegram.dog/link_serials'>𝐂𝐡𝐚𝐧𝐧𝐞𝐥</a></b>")

#shortner
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'omegalinks.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '0af17d003ce7020eb85d2a54fe0f6ef50e770e40')

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


LOG_TEXT_P =  """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
