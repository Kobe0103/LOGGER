import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.voice_states = True

bot = commands.Bot(command_prefix="?", intents=intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'Connected as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Log bot"))

@bot.event
async def on_member_ban(guild, user):
    embed = discord.Embed(title="User Banned",
                          description=f"```User {user.name} has been banned.```",
                          color=discord.Color.red())
    target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
    await target_channel.send(embed=embed)

@bot.event
async def on_guild_role_create(role):
    embed = discord.Embed(title="Role Created",
                          description=f"```Role has been created.```",
                          color=discord.Color.green())
    target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
    await target_channel.send(embed=embed)

@bot.event
async def on_guild_role_update(before, after):
    if before.name != after.name:
        embed = discord.Embed(title="Role Name Changed",
                              description=f"```Role {before.name}` name has been changed to {after.name}`.```",
                              color=discord.Color.orange())
        target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
        await target_channel.send(embed=embed)

@bot.event
async def on_guild_role_delete(role):
    embed = discord.Embed(title="Role Deleted",
                          description=f"```Role {role.name} has been deleted.```",
                          color=discord.Color.red())
    target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
    await target_channel.send(embed=embed)

@bot.event
async def on_guild_channel_delete(channel):
    embed = discord.Embed(title="Channel Deleted",
                          description=f"```Channel {channel.name} has been deleted.```",
                          color=discord.Color.red())

    target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
    await target_channel.send(embed=embed)

@bot.event
async def on_guild_channel_create(channel):
    embed = discord.Embed(title="Channel Created",
                          description=f"```Channel {channel.name} is created.```",
                          color=discord.Color.green())

    target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
    await target_channel.send(embed=embed)

@bot.event
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        embed = discord.Embed(title="Channel Name Changed",
                              description=f"```Channel {before.name} has been changed to {after.name}.```",
                              color=discord.Color.orange())

        target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
        await target_channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return
    embed = discord.Embed(title="Message Deleted",
                          description=f"```Message from {message.author.mention} was deleted in channel {message.channel.mention}. Content: {message.content}```",
                          color=discord.Color.red())
    target_channel = bot.get_channel(1161671916243914830) # Change ID to your logging channel ID
    await target_channel.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    if before.content == after.content:
        return
    embed = discord.Embed(title="Message Edited",
                          description=f"```Message from {before.author.mention} was edited in channel {before.channel.mention}.\n\n**Original Content:** {before.content}\n**New Content:** {after.content}```",
                          color=discord.Color.orange())
    target_channel = bot.get_channel(1161671916243914830)  # Change ID to your logging channel ID
    await target_channel.send(embed=embed)

bot.run("TOKEN")
