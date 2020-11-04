from telegram.ext import Filters, Updater, MessageHandler, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import logging
import os

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "1459943297:AAHBVnsOjm-nPjtQbVMtIQRqZStE5_jv-dM"
START_TEXT = "Hi [{}](tg://user?id={})!\nI Am A Forward Tag Remover & Caption Changer Bot.\nSend /help To Know What I Can Do."
HELP_TEXT = "`How To Remove Forward Tag?`\nForward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back.\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media."

#Inline Keyboard Button

keyboard = [
 [
  InlineKeyboardButton("My Creator", url="https://t.me/Sasixyz")
 ],
 [
  InlineKeyboardButton("Rate Me In Telegramic", url="https://telegramic.org/")
 ]
]
reply_markup = InlineKeyboardMarkup(keyboard)

#Start Message


def start_text(u, c):
 u.message.reply_text(START_TEXT.format(u.message.from_user.full_name,u.message.chat.id),reply_markup=reply_markup,
parse_mode=ParseMode.MARKDOWN)

#Help Message
def help_text(u,c):
  u.message.reply_text(HELP_TEXT,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)

  #Send Video
def frwrd_media(u,c):
  u.message.reply_video(u.message.video.file_id)
 
#Send File
def frwrd_file(u,c): u.message.reply_document(u.message.document.file_id)

#Send Photo
def frwrd_photo(u,c):
  u.message.reply_photo(u.message.photo[-1].file_id)

#Send Text
def frwrd_text(u,c):
  u.message.reply_text(u.message.text)

#Send Sticker
def frwrd_sticker(u,c):
  u.message.reply_sticker(u.message.sticker.file_id)

#Send Voice
def frwrd_voice(u,c):
  u.message.reply_voice(u.message.voice.file_id)

#Send Audio
def frwrd_audio(u,c):
  u.message.reply_audio(u.message.audio.file_id)
  
#Reply to media file or Document
def set_caption(u,c):
 if u.message.reply_to_message is not None:
   botname= "\n @Sasixyz"
   file_caption= u.message.text + botname
   file_type=f"{u.message.reply_to_message}"
   if "document" in file_type:
    u.message.reply_document(u.message.reply_to_message.document.file_id,
  caption=file_caption)
   elif "voice" in file_type:  
    u.message.reply_voice(u.message.reply_to_message.voice.file_id,
    caption=file_caption)
   elif "video" in file_type:
    u.message.reply_video(u.message.reply_to_message.video.file_id,
    caption=file_caption)
   elif "photo" in file_type:
    u.message.reply_photo(u.message.reply_to_message.photo[-1].file_id,
    caption=file_caption)
 else:
    u.message.reply_text(u.message.text)
  
def main():
 updater=Updater(TOKEN,use_context=True)
 dp=updater.dispatcher
 print("Bot Started...")

 #/start
 dp.add_handler(CommandHandler('start',start_text))
 #/help
 dp.add_handler(CommandHandler('help',help_text))

 #Files
 dp.add_handler(MessageHandler(Filters.document,frwrd_file))

 #Media
 dp.add_handler(MessageHandler(Filters.video,frwrd_media))

 #Photos
 dp.add_handler(MessageHandler(Filters.photo,frwrd_photo))

 #Text & Caption
 dp.add_handler(MessageHandler(Filters.text,set_caption))

 #Stickers
 dp.add_handler(MessageHandler(Filters.sticker,frwrd_sticker))

 #Voice
 dp.add_handler(MessageHandler(Filters.voice,frwrd_voice))

 #Audio
 dp.add_handler(MessageHandler(Filters.audio,frwrd_audio))


updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://from-where.herokuapp.com/' + TOKEN)
updater.idle()


if __name__ == '__main__':
    main()
