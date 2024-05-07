import discord
from discord.ext import commands
import os

if __name__ == '__main__':
   
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='>', intents=intents, case_insensitive=True)
    bot.remove_command('help')

    @bot.event
    async def on_ready():
        try:
            print('Cargando cogs...')
            await bot.load_extension('cogs.commands_cog')
        except Exception as e:
            print(e)
        print(f'{bot.user} se ha conectado ha Discord!')
    
    bot.run(os.getenv('TOKEN'))