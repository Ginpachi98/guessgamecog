from .guessgame import GuessGame

async def setup(bot):
    cog = GuessGame(bot)
    await bot.add_cog(cog)