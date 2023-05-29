#Biblioteki
import nextcord
from nextcord.ext import commands
import asyncio

#Token
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Token pod ŻADNYM pozorem go nie udpostępniaj

#Prefix bota
bot = commands.Bot(command_prefix="!")

#Powiadomienie o uruchomieniu bota
@bot.event
async def on_ready():
    print(f"Login in as {bot.user.name} ({bot.user.id})")
    await send_fact()

#ID kanału na którym będą wysyłane wiadomości
async def send_fact():
    channel = bot.get_channel(123456789)  # Zmień na ID kanału, na którym chcesz wysyłać wiadomości

#Wysyłanie
    while True:
        try:
            with open("rank", "r") as file:
                facts = file.readlines()

            for fact in facts:
                fact = fact.strip()
                await channel.send(">>> " + fact)
                await asyncio.sleep(86400)  # Tu możesz 

        except FileNotFoundError:
            print("Oh, no i dont see 'rank' file!")
            break

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

bot.run(TOKEN)