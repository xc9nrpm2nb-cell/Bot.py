import discord
from discord.ext import commands

# ====== املأ هنا فقط ======
TOKEN = 'MTQ0ODYwNDE4MTAyNzA5NDU2OQ.GHoMlw.Yjd6jP5wwoQiPN2CevU_yWxUAuvWg1_Xl7Tz-M'
PREFIX = '!'
# ===========================

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} اونلاين!')

@bot.event
async def on_message(message):
    # ما يرد على نفسه
    if message.author == bot.user:
        return

    # ردود تلقائية
    if 'هلا' in message.content.lower():
        await message.channel.send(f'هلا حبيبي {message.author.mention}!')
    elif 'السلام' in message.content.lower():
        await message.channel.send(f'وعليكم السلام {message.author.mention} 🌙')
    elif 'شلونك' in message.content.lower():
        await message.channel.send('أنا بوت، دائمًا بألف خير 😄')
    elif 'باي' in message.content.lower():
        await message.channel.send('مع السلامة، لا تطول الغياب!')

    # عشان الأوامر تشتغل
    await bot.process_commands(message)

# أمر بسيط تجربته: !ping
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong! 🏓')

bot.run(MTQ0ODYwNDE4MTAyNzA5NDU2OQ.GHoMlw.Yjd6jP5wwoQiPN2CevU_yWxUAuvWg1_Xl7Tz-M)
