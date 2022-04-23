import datetime

import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'Could not unload the cog\n{e}')
            return
        await ctx.send('Cog unloaded')

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'Could not load the cog\n{e}')
            return
        await ctx.send('Cog loaded')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'Could not reload the cog\n{e}')
            return
        await ctx.send('Cog reloaded')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(f'[MY ERROR] {ex}')
        await ctx.send('.please check with !help for the usage of this command or ask administrator.')

    @commands.command()
    @commands.check_any(commands.is_owner(), commands.has_role('Managers'))
    async def server(self, ctx):
        guild = ctx.guild
        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)

        embed = discord.Embed(
            description="Server Status",
            colour=discord.Colour.dark_blue()
        )

        embed.set_thumbnail(
            url="https://www.pinclipart.com/picdir/big/354-3546720_his-2013-helpdesk-support-2x-references-icon-png.png")

        embed.set_image(
            url="https://patchbot.io/images/games/call_of_duty_black_ops_4_md.jpg")

        # emoji_string = ""
        # for e in guild.emojis:
        #     if e.is_usable():
        #         emoji_string += str(e)
        #
        # embed.add_field(
        #     name="Custom Emoji",
        #     value=emoji_string or "No emoji available",
        #     inline=False
        # )

        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        embed.add_field(name="# Voice Channels", value=str(no_voice_channels))
        embed.add_field(name="# Text Channels", value=str(no_text_channels))
        embed.add_field(name="AFK Channel:", value=guild.afk_channel)
        embed.set_footer(text=str(datetime.datetime.now()))

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
