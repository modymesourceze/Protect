from config import Config
from pyrogram import Client
from pyrogram import  filters,enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup as mk, InlineKeyboardButton as btn
from pyrogram.types import ChatPermissions

from asSQL import Client as cl


data = cl("protect")
db = data['data']
db.create_table()
db.set("botname",['مارسلين' , 'مارسي' , 'بوت' ,'مارسل' , 'مارسيلين'])
db.set("bad_words",['كس','عير','طيز','زب','كسمك','كسختك','طيزك','مص'])

plugins = dict(root="plugins")

Client("x",
api_id=Config.APP_ID,
api_hash=Config.API_HASH,
bot_token=Config.TG_BOT_TOKEN, plugins=plugins).run()