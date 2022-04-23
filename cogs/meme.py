import aiohttp
import discord

from discord.ext import commands


class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(f'[MY ERROR] {ex}')
        await ctx.send('.please check with !help for the usage of this command or ask administrator.')

    @commands.command(brief='Get a meme to laugh!')
    @commands.has_role('Participants')
    async def meme(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://meme-api.herokuapp.com/gimme') as req:
                    response = await req.json()

                    embed = discord.Embed(
                        title=f'requested by {str(ctx.author)[:-5]}'
                    )
                    embed.set_image(url=response['url'])

                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meme(bot))
