from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# API token dari BotFather
TOKEN = '7533367231:AAEJd1mIQUHI4Lr4JlmDSmW2MBpdwH5AG5M'

# Daftar kata atau frasa yang ingin diblokir
blocked_words = ['di bio', 'bio', 'test']  # Tambahkan kata yang ingin diblokir

# Fungsi untuk memeriksa pesan
def block_messages(update: Update, context: CallbackContext):
    message_text = update.message.text.lower()  # Ubah pesan ke huruf kecil untuk pencocokan
    
    # Memeriksa apakah ada kata yang diblokir dalam pesan
    for word in blocked_words:
        if word in message_text:
            # Hapus pesan jika berisi kata yang diblokir
            context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            return

# Fungsi utama untuk menjalankan bot
def main():
    # Menghubungkan bot dengan token
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Menambahkan handler untuk memblokir pesan yang mengandung kata-kata tertentu
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, block_messages))

    # Memulai bot
    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()
