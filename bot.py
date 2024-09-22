from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from googletrans import Translator, LANGUAGES

load_dotenv()
bot_key = os.getenv('DISCORD_BOT_TOKEN')


user_languages = {}
translator = Translator()

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Channel ID to send translated messages
CHANNEL_ID = 1284633390032883742
channel = None


#connect bot to discord and get it ready to start processing events. 
@bot.event
async def on_ready():
    global channel
    channel = bot.get_channel(CHANNEL_ID)
    print(f'Logged in as {bot.user}!')


@bot.command()
async def translate(ctx, lang, *, message):
    try:
        detect_lang = translator.detect(message).lang
        translation = translator.translate(message, src=detect_lang, dest=lang)
        await ctx.send(f"Translation ({LANGUAGES[lang]}): {translation.text}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


@bot.command()
# User can type in !setlanguage en to set preferred language to English
async def set_language(ctx, language_code):
    language_code = language_code.lower()

    # Validate language code
    if language_code in LANGUAGES:
        user_languages[ctx.author.id] = language_code
        await ctx.send(f"Your preferred language has been set to `{LANGUAGES[language_code]}`.")
    else:
        await ctx.send("Invalid language code. Please try again.")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    # Detect message language
    detected_lang = translator.detect(message.content).lang
    target_lang = user_languages.get(message.author.id, 'en')  # Default to English if not set

    # Skip if message is already in the target language
    if detected_lang == target_lang:
        return

    # Try translating the message
    try:
        translation = translator.translate(message.content, src=detected_lang, dest=target_lang)
        await message.channel.send(f"**{message.author.display_name} said:** {translation.text}")
    except Exception as e:
        print(f"Translation error: {e}")
        await message.channel.send("Sorry, I couldn't translate that message.")


# Run the bot
bot.run(bot_key)
