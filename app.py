import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ضع توكن البوت الذي تحصل عليه من @BotFather هنا
TOKEN = "8386512787:AAEwmMutrbXjWsvCI5KNNLn4CvuLqMtByHg"

# دالة لمعالجة أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # استخراج معرف المستخدم أو الدردشة
    chat_id = update.effective_chat.id
    # إرسال رسالة "شكراً"
    await context.bot.send_message(chat_id=chat_id, text="شكراً")

# الدالة الرئيسية لتشغيل البوت
def main():
    # إنشاء تطبيق البوت
    app = Application.builder().token(TOKEN).build()
    
    # إضافة معالج للأمر /start
    app.add_handler(CommandHandler("start", start))
    
    # بدء الاستماع للتحديثات (طريقة غير متزامنة)
    print("البوت يعمل...")
    app.run_polling()

if __name__ == "__main__":
    main()