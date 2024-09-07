from pyrogram import Client
import logging

# logging
logging.basicConfig(level=logging.INFO)



# bot
bot = Client(name="bot", api_id=24351291, api_hash="ed3c922b4dc9f20b55911903f3fb61f3", bot_token="6926570748:AAFupOIOovpQswMaVOxIaG6mdXtuYoFfJEQ")

# message handle 
@bot.on_message()
async def test(bot, mes): 
   await mes.reply_text(f"hello {mes.from_user.mention}") 
   
   

# run
print("Bot is working")
bot.run()
