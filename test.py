from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.error import BadRequest

# API Token dari BotFather
TOKEN = '7533367231:AAEJd1mIQUHI4Lr4JlmDSmW2MBpdwH5AG5M'

# Fungsi untuk menandai semua anggota yang memiliki username
def tag_all(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    members = context.bot.get_chat_administrators(chat_id)
    tagged_users = []

    for member in members:
        user = member.user
        if user.username:
            tagged_users.append(f"@{user.username}")
    
    if tagged_users:
        tag_message = ' '.join(tagged_users)
        try:
            context.bot.send_message(chat_id=chat_id, text=tag_message)
        except BadRequest as e:
            update.message.reply_text("Terjadi kesalahan saat menandai pengguna.")
    else:
        update.message.reply_text("Tidak ada anggota dengan username untuk ditandai.")

# Fungsi utama untuk memulai bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Menambahkan handler untuk perintah /tagall
    dp.add_handler(CommandHandler("tagall", tag_all))

    # Memulai polling untuk menerima pesan dari Telegram
    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()
