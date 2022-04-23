from discord.ext import commands


class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(f'[MY ERROR] {ex}')
        await ctx.send('.please check with !help for the usage of this command or administrator.')

    @commands.command(brief='poke\'s the mentioned one')
    async def poke(self, ctx, arg):
        await ctx.send('poke {0} :laughing:'.format(arg))

    @commands.command(brief='deletes latest 5 messages')
    @commands.check_any(commands.is_owner(), commands.has_role('Managers'))
    async def clear(self, ctx, arg=5):
        await ctx.channel.purge(limit=arg)

    @commands.command(brief='generate an invite link')
    @commands.check_any(commands.has_role('Managers'), commands.has_role('Participants'))
    async def invite(self, ctx, arg='1'):
        link = await ctx.channel.create_invite(max_age=int(arg))
        await ctx.send(f'Hey bud burst into this Server\n{link}')


def setup(bot):
    bot.add_cog(Basic(bot))
