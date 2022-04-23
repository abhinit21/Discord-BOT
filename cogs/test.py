from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(f'[MY ERROR] {ex}')
        await ctx.send('.please check with !help for the usage of this command or ask administrator.')

    @commands.command(brief='Try it out')
    async def ping(self, ctx):
        await ctx.send('pong')


def setup(bot):
    bot.add_cog(Test(bot))
