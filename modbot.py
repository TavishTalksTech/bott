import discord
from discord.ext import commands

client = commands.Bot(command_prefix='>')

@client.command(description="Mutes the specified user.")
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")


@client.command()
async def hi(ctx):
    await ctx.send("howdy there")
  
rulesvar = ["#1: No Swearing", "#2: No NSFW", "#3: Don't Try To Act Like Mods", "#4: Text in the channel catered to your message"]

@client.command()
async def rules(ctx):
    await ctx.send(rulesvar[0])
    await ctx.send(rulesvar[1])
    await ctx.send(rulesvar[2])
    await ctx.send(rulesvar[3])

client.run('ODUwNzQxOTY1NjU0MDY1MjAz.YLuJMg.F83-A_KtWROEJqvEFV8H-SbiH2w')

##1. No nsfw stuff
# 2. Dont try to act like mods
# 3.Text in the channel related to ur message
# 4.If any nsfw or stuff instant ban.
# 5. Enjoy
