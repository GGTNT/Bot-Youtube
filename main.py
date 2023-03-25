import discord
from discord.ext import commands
from config import token

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

class MonBot(commands.Bot):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Discord py"))
        print(f"Je suis conneté en tant que {self.user}")

bot = MonBot(command_prefix="!",help_command=None,intents=intents)


bot.run(token)