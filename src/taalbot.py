import discord
from cogs.greeting import Greeting
from cogs.onboarding import Onboarding


class Taalbot(discord.ext.commands.Bot):
    def __init__(self):
        # Intents of bot.
        intents = discord.Intents.all()

        # Activity and status of bot.
        activity = discord.Game(name="I'm helping 👀")
        status = discord.Status.online

        # Pass arguments to super constructor.
        super().__init__(command_prefix='??', intents=intents, activity=activity, status=status)

    async def on_ready(self):
        print('Taalbot is preparing...')
        await self.add_cogs()
        print("Taalbot is now ready.")

    async def add_cogs(self):
        await self.add_cog(Greeting(self))
        await self.add_cog(Onboarding(self))
