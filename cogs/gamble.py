import random

from discord.ext import commands


class Gamble(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(f'[MY ERROR] {ex}')
        await ctx.send('.please check with !help for the usage of this command or administrator.')

    @commands.command(brief='Works as a die')
    async def roll(self, ctx, arg='1'):
        if arg == '1':
            await ctx.send(random.randrange(1, 7))
            return

        outcomes = [str(random.randrange(1, 7)) for _ in range(int(arg))]
        await ctx.send('{0}\n{1}'.format(' | '.join(outcomes), sum(map(int, outcomes))))

    @commands.command(brief='Toss a coin')
    async def coin(self, ctx):
        boolean = random.randint(0, 1)
        await ctx.send('You got Tails!' if boolean == 0 else 'You got Heads!')


def setup(bot):
    bot.add_cog(Gamble(bot))
